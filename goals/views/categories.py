# from django.db import transaction
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework import filters, permissions
# from rest_framework.generics import (
#     CreateAPIView,
#     ListAPIView,
#     RetrieveUpdateDestroyAPIView,
# )
# from rest_framework.pagination import LimitOffsetPagination
#
# from goals.filters import CategoryFilter
# from goals.models import Category, Goal
# from goals.permissions import CategoryPermissions
# from goals.serializers.categorises_serializers import (
#     CategoryCreateSerializer,
#     CategorySerializer,
# )
#
#
# class CategoryListView(ListAPIView):
#     serializer_class = CategorySerializer
#     permission_classes = [permissions.IsAuthenticated]
#     pagination_class = LimitOffsetPagination
#     filter_backends = [
#         DjangoFilterBackend,
#         filters.OrderingFilter,
#         filters.SearchFilter,
#     ]
#     filterset_class = CategoryFilter
#     ordering_fields = ['title', 'created']
#     ordering = ['title']
#     search_fields = ['title']
#
#     def get_queryset(self):
#         return (
#             Category.objects.select_related('user')
#             .filter(board__participants__user=self.request.user)
#             .exclude(is_deleted=True)
#         )
#
#
# class CategoryCreateView(CreateAPIView):
#     serializer_class = CategoryCreateSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#
# class CategoryDetailView(RetrieveUpdateDestroyAPIView):
#     serializer_class = CategorySerializer
#     permission_classes = [CategoryPermissions]
#
#     def get_queryset(self):
#         return Category.objects.select_related('user').exclude(is_deleted=True)
#
#     def perform_destroy(self, instance: Category):
#         with transaction.atomic():
#             instance.is_deleted = True
#             instance.save()
#             # Changes goals status in "deleted" category to "Archived"
#             Goal.objects.filter(category=instance.id).update(
#                 status=Goal.Status.archived
#             )
from django.db import transaction
from rest_framework import generics, permissions, filters

from goals.models import GoalCategory, Goal
from goals.permissions import GoalCategoryPermission
from goals.serializers import GoalCategorySerializer, GoalCategoryWithUserSerializer


class CreateCategoryView(generics.CreateAPIView):
    serializer_class = GoalCategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GoalCategoryWithUserSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['title', 'created']
    ordering = ['title']
    search_fields = ['title']

    def get_queryset(self):
        return GoalCategory.objects.filter(
            board__participants__user=self.request.user
        ).exclude(is_deleted=True)


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GoalCategoryWithUserSerializer
    permission_classes = [GoalCategoryPermission]
    queryset = GoalCategory.objects.exclude(is_deleted=True)

    def perform_destroy(self, instance: GoalCategory):
        with transaction.atomic():
            instance.is_deleted = True
            instance.save()
            instance.goal_set.update(status=Goal.Status.archived)
