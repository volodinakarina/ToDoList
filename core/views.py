import rest_framework.status as status
from django.contrib.auth import authenticate, login, logout
from drf_spectacular.utils import OpenApiResponse, extend_schema, extend_schema_view
from rest_framework import generics, exceptions, permissions
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import User
from core.serializers import CreatUserSerializer, LoginSerializer, ProfileSerializer, UpdatePasswordSerializer


#
# from .models import User
# from .serializers import (
#     UserChangePasswordSerializer,
#     UserLoginSerializer,
#     UserSerializer,
#     UserSingUpSerializer,
# )
#
#
# @extend_schema_view(
#     post=extend_schema(
#         request=UserSingUpSerializer,
#         description='Registration view for new users',
#         summary='User registration',
#         responses={
#             201: OpenApiResponse(
#                 response=UserSingUpSerializer, description='User created'
#             ),
#             400: OpenApiResponse(
#                 response=UserSingUpSerializer.errors,
#                 description='Bad Request, (something invalid)',
#             ),
#         },
#     )
# )
# class UserSingUpView(CreateAPIView):
#     serializer_class = UserSingUpSerializer
#     queryset = User.objects.all()
#
#
# class UserLoginView(APIView):
#     @extend_schema(
#         request=UserLoginSerializer,
#         description='Login view for users',
#         summary='User login',
#         responses={
#             200: OpenApiResponse(
#                 response=UserSerializer, description='Successful login'
#             ),
#             400: OpenApiResponse(description='Wrong password or username'),
#         },
#     )
#     def post(self, request, *args, **kwargs) -> Response:
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = authenticate(request, username=username, password=password)
#
#         if user is not None:
#             login(request, user)
#             return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
#         else:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
#
#
# @extend_schema_view(
#     get=extend_schema(
#         description='Get all information about user',
#         summary='User retrieve',
#         responses={
#             200: OpenApiResponse(response=UserSerializer),
#             403: OpenApiResponse(description="You don't have permission"),
#         },
#     ),
#     put=extend_schema(
#         request=UserSerializer,
#         description="Update all user's information",
#         summary='User update',
#         responses={
#             200: OpenApiResponse(response=UserSerializer),
#             400: OpenApiResponse(
#                 response=UserSerializer.errors,
#                 description='Bad Request, (something invalid)',
#             ),
#             403: OpenApiResponse(description="You don't have permission"),
#         },
#     ),
#     patch=extend_schema(
#         request=UserSerializer,
#         description="Update partial user's information",
#         summary='User update partial',
#         responses={
#             200: OpenApiResponse(response=UserSerializer),
#             400: OpenApiResponse(
#                 response=UserSerializer.errors,
#                 description='Bad Request, (something invalid)',
#             ),
#             403: OpenApiResponse(description="You don't have permission"),
#         },
#     ),
#     delete=extend_schema(
#         description='Logout user from system',
#         summary='User Logout',
#         responses={
#             204: OpenApiResponse(description='Successful logout'),
#             403: OpenApiResponse(description="You don't have permission"),
#         },
#     ),
# )
# class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
#     serializer_class = UserSerializer
#     permission_classes = [IsAuthenticated]
#
#     def get_object(self) -> User:
#         return self.request.user
#
#     def delete(self, request, *args, **kwargs) -> Response:
#         logout(request)
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# @extend_schema_view(
#     put=extend_schema(
#         request=UserChangePasswordSerializer,
#         description='Update user password',
#         summary='Password update',
#         responses={
#             200: OpenApiResponse(
#                 response=UserChangePasswordSerializer,
#                 description='Password updated successfully',
#             ),
#             400: OpenApiResponse(
#                 response=UserChangePasswordSerializer.errors,
#                 description='Bad Request, (something invalid)',
#             ),
#             403: OpenApiResponse(description="You don't have permission"),
#         },
#     )
# )
# class UserUpdatePasswordAPIView(UpdateAPIView):
#     serializer_class = UserChangePasswordSerializer
#     permission_classes = [IsAuthenticated]
#     http_method_names = ['put']
#
#     def get_object(self) -> User:
#         return self.request.user
class SingUpView(generics.CreateAPIView):
    serializer_class = CreatUserSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if not(user := authenticate(**serializer.validated_data)):
            raise exceptions.AuthenticationFailed

        login(request=request, user=user)

        return Response(ProfileSerializer(user).data)


class ProfileView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self) -> User:
        return self.request.user

    def perform_destroy(self, instance: User) -> None:
        logout(self.request)

class UpdatePasswordView(generics.GenericAPIView):
    serializer_class = UpdatePasswordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        request.user.set_password(serializer.validated_data['new_password'])
        request.user.save()

        return Response(serializer.data)
