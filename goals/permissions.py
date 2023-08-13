# from django.core.exceptions import BadRequest
# from rest_framework.permissions import SAFE_METHODS, BasePermission
#
# from .models import Board, BoardParticipant, Category, Comment, Goal
#
#
# class BoardPermissions(BasePermission):
#     message = "You don't have permission to edit this board"
#
#     def has_object_permission(self, request, view, obj: Board) -> bool:
#         if not request.user.is_authenticated:
#             return False
#
#         if request.method in SAFE_METHODS:
#             return BoardParticipant.objects.filter(
#                 user=request.user, board=obj
#             ).exists()
#
#         return BoardParticipant.objects.filter(
#             user=request.user, board=obj, role=BoardParticipant.Role.owner
#         ).exists()
#
#
# class CategoryPermissions(BasePermission):
#     message = "You don't have permission to edit this category"
#
#     def has_object_permission(self, request, view, obj: Category) -> bool:
#         if not request.user.is_authenticated:
#             return False
#
#         if request.method in SAFE_METHODS:
#             return BoardParticipant.objects.filter(
#                 user=request.user, board=obj.board
#             ).exists()
#
#         return (
#             BoardParticipant.objects.filter(user=request.user, board=obj.board)
#             .exclude(role=BoardParticipant.Role.reader)
#             .exists()
#         )
#
#
# class CreateCategoryPermissions(BasePermission):
#     message = "You don't have permission to create this category"
#
#     def has_permission(self, request, view) -> bool:
#         board_id = request.data.get('board')
#         if type(board_id) is not int:
#             raise BadRequest({'goal': 'Wrong board id'})
#
#         return (
#             BoardParticipant.objects.filter(user=request.user, board_id=board_id)
#             .exclude(role=BoardParticipant.Role.reader)
#             .exists()
#         )
#
#
# class GoalPermissions(BasePermission):
#     message = "You don't have permission to edit this goal"
#
#     def has_object_permission(self, request, view, obj: Goal) -> bool:
#         if not request.user.is_authenticated:
#             return False
#
#         if request.method in SAFE_METHODS:
#             return BoardParticipant.objects.filter(
#                 user=request.user, board=obj.category.board
#             ).exists()
#
#         return (
#             BoardParticipant.objects.filter(user=request.user, board=obj.category.board)
#             .exclude(role=BoardParticipant.Role.reader)
#             .exists()
#         )
#
#
# class CreateGoalPermissions(BasePermission):
#     message = "You don't have permission to create this goal"
#
#     def has_permission(self, request, view) -> bool:
#         category_id = request.data.get('category')
#
#         if type(category_id) is not int:
#             raise BadRequest({'goal': 'Wrong category id'})
#
#         return (
#             BoardParticipant.objects.filter(
#                 user=request.user, board__categories__id=category_id
#             )
#             .exclude(role=BoardParticipant.Role.reader)
#             .exists()
#         )
#
#
# class CommentPermissions(BasePermission):
#     message = "You don't have permission to edit this comment"
#
#     def has_object_permission(self, request, view, obj: Comment) -> bool:
#         if not request.user.is_authenticated:
#             return False
#
#         if request.method in SAFE_METHODS:
#             return BoardParticipant.objects.filter(
#                 user=request.user, board=obj.goal.category.board
#             ).exists()
#
#         if request.method == 'PUT':
#             return obj.user == request.user
#
#         return (
#             BoardParticipant.objects.filter(
#                 user=request.user, board=obj.goal.category.board
#             )
#             .exclude(role=BoardParticipant.Role.reader)
#             .exists()
#             or obj.user == request.user
#         )
#
#
# class CreateCommentPermissions(BasePermission):
#     message = "You don't have permission to create this comment"
#
#     def has_permission(self, request, view) -> bool:
#         goal_id = request.data.get('goal', '')
#         try:
#             goal = Goal.objects.get(id=goal_id)
#         except Goal.DoesNotExist:
#             return False
#         except (TypeError, ValueError):
#             raise BadRequest({'goal': 'Wrong goal id'})
#
#         return BoardParticipant.objects.filter(
#             user=request.user, board=goal.category.board
#         ).exists()
from typing import Any

from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from rest_framework.request import Request
from rest_framework.generics import GenericAPIView
from goals.models import GoalCategory, GoalComment, Goal, Board, BoardParticipant


class BoardPermission(IsAuthenticated):
    def has_object_permission(self, request: Request, view: GenericAPIView, obj: Board) -> bool:
        _filters: dict[str, Any] = {'user': request.user, 'board': obj}
        if request.method not in SAFE_METHODS:
            _filters['role'] = BoardParticipant.Role.owner
        return BoardParticipant.objects.filter(**_filters).exists()


class GoalCategoryPermission(IsAuthenticated):
    def has_object_permission(self, request: Request, view: GenericAPIView, obj: GoalCategory) -> bool:
        _filters: dict[str, Any] = {'user': request.user, 'board': obj.board}
        if request.method not in SAFE_METHODS:
            _filters['role__in'] = [BoardParticipant.Role.owner, BoardParticipant.Role.writer]

        return BoardParticipant.objects.filter(**_filters).exists()


class GoalPermission(IsAuthenticated):
    def has_object_permission(self, request: Request, view: GenericAPIView, obj: Goal) -> bool:
        _filters: dict[str, Any] = {'user': request.user, 'board': obj.category.board}
        if request.method not in SAFE_METHODS:
            _filters['role__in'] = [BoardParticipant.Role.owner, BoardParticipant.Role.writer]

        return BoardParticipant.objects.filter(**_filters).exists()


class GoalCommentPermission(IsAuthenticated):
    def has_object_permission(self, request: Request, view: GenericAPIView, obj: GoalComment) -> bool:
        if request.method in SAFE_METHODS:
            return True
        return request.user == obj.user

