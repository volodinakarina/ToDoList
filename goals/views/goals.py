# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework import filters, permissions
# from rest_framework.generics import (
#     CreateAPIView,
#     ListAPIView,
#     RetrieveUpdateDestroyAPIView,
# )
# from rest_framework.pagination import LimitOffsetPagination
#
# from goals.filters import GoalFilter
# from goals.models import Goal
# from goals.permissions import GoalPermissions
# from goals.serializers.goals_serializers import GoalCreateSerializer, GoalSerializer
#
#
# class GoalListView(ListAPIView):
#     serializer_class = GoalSerializer
#     permission_classes = [permissions.IsAuthenticated]
#     pagination_class = LimitOffsetPagination
#     filter_backends = [
#         DjangoFilterBackend,
#         filters.OrderingFilter,
#         filters.SearchFilter,
#     ]
#     filterset_class = GoalFilter
#     ordering_fields = ['title', 'created', 'priority', 'due_date']
#     search_fields = ['title']
#
#     def get_queryset(self):
#         return (
#             Goal.objects.select_related('user')
#             .filter(
#                 category__board__participants__user=self.request.user,
#                 category__is_deleted=False,
#             )
#             .exclude(status=Goal.Status.archived)
#         )
#
#
# class GoalCreateView(CreateAPIView):
#     serializer_class = GoalCreateSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#
# class GoalDetailView(RetrieveUpdateDestroyAPIView):
#     serializer_class = GoalSerializer
#     permission_classes = [GoalPermissions]
#
#     def get_queryset(self):
#         return (
#             Goal.objects.select_related('user')
#             .filter(
#                 category__board__participants__user=self.request.user,
#                 category__is_deleted=False,
#             )
#             .exclude(status=Goal.Status.archived)
#         )
#
#     def perform_destroy(self, instance: Goal):
#         instance.status = Goal.Status.archived
#         instance.save()
# from django_filters.rest_framework import DjangoFilterBackend
# from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiResponse
# from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
# from rest_framework.permissions import IsAuthenticated
# from rest_framework import filters
#
# from ..permissions import GoalPermissions, CreateGoalPermissions
# from ..serializers.goals_serializers import GoalCreateSerializer, GoalSerializer
# from ..models import Goal
# from ..filters import GoalFilter
#
#
#
# @extend_schema_view(
#     post=extend_schema(request=GoalCreateSerializer,
#                        description='Create new goal', summary='Create goal',
#                        responses={201: OpenApiResponse(response=GoalCreateSerializer,
#                                                        description='Goal has been created'),
#                                   400: OpenApiResponse(response=GoalCreateSerializer.errors,
#                                                        description='Bad Request, (something invalid)'),
#                                   403: OpenApiResponse(description="You don't have permission")}))
# class GoalCreateAPIView(CreateAPIView):
#     serializer_class = GoalCreateSerializer
#     permission_classes = [IsAuthenticated, CreateGoalPermissions]
#
#
# @extend_schema_view(
#     get=extend_schema(description="User's goals list", summary='Goals list',
#                       responses={200: OpenApiResponse(response=GoalSerializer, description='Goals list'),
#                                  403: OpenApiResponse(description="You don't have permission")}))
# class GoalListAPIView(ListAPIView):
#     serializer_class = GoalSerializer
#     permission_classes = [IsAuthenticated]
#     filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
#     filterset_class = GoalFilter
#     ordering_fields = ['-priority', 'due_date']
#     ordering = ['-priority', 'due_date']
#     search_fields = ['title', 'description']
#
#     def get_queryset(self):
#         return Goal.objects.filter(category__board__participants__user=self.request.user).exclude(
#             status=Goal.StatusChoices.archived).select_related('user')
#
#
# @extend_schema_view(
#     get=extend_schema(request=GoalSerializer,
#                       description='Get full information about goal', summary='Goal detail',
#                       responses={200: OpenApiResponse(response=GoalSerializer, description='Goal information'),
#                                  403: OpenApiResponse(description="You don't have permission")}),
#     put=extend_schema(request=GoalSerializer,
#                       description='Update goal information', summary='Update goal',
#                       responses={200: OpenApiResponse(response=GoalSerializer, description='Goal has been updated'),
#                                  403: OpenApiResponse(description="You don't have permission")}),
#     delete=extend_schema(request=GoalSerializer,
#                          description='Delete goal and goal\'s comments', summary='Delete goal',
#                          responses={204: OpenApiResponse(response={}, description='Goal has been deleted'),
#                                     403: OpenApiResponse(description="You don't have permission")}))
# class GoalRUDAPIView(RetrieveUpdateDestroyAPIView):
#     serializer_class = GoalSerializer
#     permission_classes = [IsAuthenticated, GoalPermissions]
#     http_method_names = ['get', 'put', 'delete']
#
#     def get_queryset(self):
#         return Goal.objects.exclude(status=Goal.StatusChoices.archived).select_related('user')
#
#     def perform_destroy(self, instance: Goal) -> Goal:
#         instance.status = Goal.StatusChoices.archived
#         instance.save()
#         return instance
from django_filters.rest_framework import DjangoFilterBackend
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework import filters, generics, permissions
#
# from goals.filters import GoalFilter
# from goals.models import Goal
# from goals.permissions import GoalPermissions
# from goals.serializers.goals_serializers import GoalCreateSerializer, GoalSerializer
#
#
# class GoalCreateView(generics.CreateAPIView):
#     serializer_class = GoalSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#
# class GoalListView(generics.ListAPIView):
#     serializer_class = GoalCreateSerializer
#     permission_classes = [permissions.IsAuthenticated]
#     filter_backends = [
#         DjangoFilterBackend,
#         filters.OrderingFilter,
#         filters.SearchFilter,
#     ]
#     filterset_class = GoalFilter
#     ordering_fields = ['title', 'description']
#     ordering = ['title']
#     search_fields = ['title', 'description']
#
#     def get_queryset(self):
#         return (
#             Goal.objects.select_related('user')
#             .filter(user=self.request.user, category__is_deleted=False)
#             .exclude(status=Goal.Status.archived)
#         )
#
#
# class GoalDetailView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [GoalPermissions]
#
#     serializer_class = GoalCreateSerializer
#
#     def get_queryset(self):
#         return (
#             Goal.objects.select_related('user')
#             .filter(category__is_deleted=False)
#             .exclude(status=Goal.Status.archived)
#         )
#
#     def perform_destroy(self, instance: Goal) -> None:
#         instance.status = Goal.Status.archived
#         instance.save()
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend

from goals.filters import GoalDateFilter
from goals.models import GoalCategory, Goal
from goals.permissions import GoalCategoryPermission, GoalPermission
from goals.serializers import GoalCategorySerializer, GoalCategoryWithUserSerializer, GoalSerializer, \
    GoalWithUserSerializer


class GoalCreateView(generics.CreateAPIView):
    serializer_class = GoalSerializer
    permission_classes = [permissions.IsAuthenticated]


class GoalListView(generics.ListAPIView):
    serializer_class = GoalWithUserSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_class = GoalDateFilter
    ordering_fields = ['title', 'description']
    ordering = ['title']
    search_field = ['title', 'description']

    def get_queryset(self):
        return Goal.objects.select_related('user').filter(
            user=self.request.user, category__is_deleted=False
        ).exclude(status=Goal.Status.archived)


class GoalDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [GoalPermission]
    serializer_class = GoalWithUserSerializer

    def get_queryset(self):
        return Goal.objects.select_related('user').filter(category__is_deleted=False).exclude(status=Goal.Status.archived)

    def perform_destroy(self, instance: Goal) -> None:
        instance.status = Goal.Status.archived
        instance.save()
