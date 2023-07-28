from typing import Any

from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers, exceptions
from rest_framework.validators import UniqueValidator

from todolist.fields import PasswordField
from .models import User


# class UserSingUpSerializer(serializers.ModelSerializer):
#     username = serializers.CharField(
#         validators=[
#             UniqueValidator(
#                 queryset=User.objects.all(), message='Имя пользователя уже занято'
#             )
#         ]
#     )
#     password_repeat = serializers.CharField(
#         max_length=128, style={'input_type': 'password'}, write_only=True
#     )
#     email = serializers.EmailField(
#         required=False,
#         validators=[
#             UniqueValidator(
#                 queryset=User.objects.all(),
#                 message='Адрес электронной почты уже используется',
#             )
#         ],
#     )
#
#     class Meta:
#         model = User
#         fields = (
#             'username',
#             'first_name',
#             'last_name',
#             'email',
#             'password',
#             'password_repeat',
#         )
#         extra_kwargs = {'password': {'write_only': True}}
#
#     def validate_password_repeat(self, password_repeat: str) -> str:
#         cd = self.initial_data
#         if cd['password'] != cd['password_repeat']:
#             raise serializers.ValidationError('Пароли не совпадают')
#         return password_repeat
#
#     def validate_password(self, password: str) -> str:
#         try:
#             validate_password(password)
#         except ValidationError as exc:
#             raise serializers.ValidationError(str(exc))
#
#         return password
#
#     def create(self, validated_data: dict[str:Any]) -> User:
#         del validated_data['password_repeat']
#         user = super().create(validated_data)
#         user.set_password(validated_data['password'])
#         user.save()
#         return user
#
#
# class UserSerializer(serializers.ModelSerializer):
#     username = serializers.CharField(
#         validators=[
#             UniqueValidator(
#                 queryset=User.objects.all(), message='Имя пользователя уже занято'
#             )
#         ]
#     )
#
#     email = serializers.EmailField(
#         required=False,
#         validators=[
#             UniqueValidator(
#                 queryset=User.objects.all(),
#                 message='Адрес электронной почты уже используется',
#             )
#         ],
#     )
#
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'first_name', 'last_name', 'email')
#
#
# class UserChangePasswordSerializer(serializers.ModelSerializer):
#     new_password = serializers.CharField(write_only=True, required=True)
#     old_password = serializers.CharField(write_only=True, required=True)
#
#     class Meta:
#         model = User
#         fields = ('old_password', 'new_password')
#
#     def validate_new_password(self, new_password: str) -> str:
#         try:
#             validate_password(new_password)
#         except ValidationError as exc:
#             raise serializers.ValidationError(str(exc))
#
#         return new_password
#
#     def validate_old_password(self, old_password: str) -> str:
#         if self.context['request'].user.check_password(old_password):
#             return old_password
#         else:
#             raise serializers.ValidationError('Старый пароль введен неверно')
#
#     def save(self, **kwargs) -> User:
#         user = self.instance
#         user.set_password(self.validated_data['new_password'])
#         user.save()
#         return user
#
#
# class UserLoginSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username', 'password')
class CreatUserSerializer(serializers.ModelSerializer):
    password = PasswordField()
    password_repeat = PasswordField(validate=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password', 'password_repeat')

    def validate(self, attrs: dict) -> dict:

        if attrs['password'] != attrs['password_repeat']:
            raise ValidationError('Passwords must match')
        return attrs

    def create(self, validated_data: dict) -> User:
        del validated_data['password_repeat']
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = PasswordField(validate=False)

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')


class UpdatePasswordSerializer(serializers.Serializer):
    old_password = PasswordField(validate=False)
    new_password = PasswordField()

    def validate_old_password(self, old_password: str) -> str:
        request = self.context['request']

        if not request.user.is_authenticated:
            raise exceptions.NotAuthenticated
        if not request.user.check_password(old_password):
            raise exceptions.ValidationError('Corrent password is incorrect')
        return old_password
