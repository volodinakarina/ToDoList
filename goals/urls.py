# from django.urls import path
#
# from .views import categories, comments, goals
#
# urlpatterns = [
#     path('goal_category/list', categories.CategoryListView.as_view()),
#     path('goal_category/create', categories.CategoryCreateView.as_view()),
#     path('goal_category/<int:pk>', categories.CategoryDetailView.as_view()),
#     path('goal/list', goals.GoalListView.as_view()),
#     path('goal/create', goals.GoalCreateView.as_view()),
#     path('goal/<int:pk>', goals.GoalDetailView.as_view()),
#     path('goal_comment/list', comments.CommentListView.as_view()),
#     path('goal_comment/create', comments.CommentCreateView.as_view()),
#     path('goal_comment/<int:pk>', comments.CommentDetailView.as_view()),
# ]
# from django.urls import path
#
# from goals import views
#
# urlpatterns = [
#     # Board
#     path('board/create', views.BoardCreateView.as_view(), name='create-board'),
#     path('board/list', views.BoardListView.as_view(), name='board-list'),
#     path('board/<int:pk>', views.BoardDetailView.as_view(), name='board-details'),
#
#     # Categories
#     path('goal_category/create', views.CategoryCreateView.as_view(), name='create-category'),
#     path('goal_category/list', views.CategoryListView.as_view(), name='categories-list'),
#     path('goal_category/<int:pk>', views.CategoryDetailView.as_view(), name='category-details'),
#
#     # Goals
#     path('goal/create', views.GoalCreateView.as_view(), name='create-goal'),
#     path('goal/list', views.GoalListView.as_view(), name='goal-list'),
#     path('goal/<int:pk>', views.GoalDetailView.as_view(), name='goal-details'),
#
#     # Comments
#     path('goal_comment/create', views.CommentCreateView.as_view(), name='create-comment'),
#     path('goal_comment/list', views.CommentListView.as_view(), name='comment-list'),
#     path('goal_comment/<int:pk>', views.CommentDetailView.as_view(), name='comment-details')
# ]






# from django.urls import path
#
# from goals.apps import GoalsConfig
# from goals.views.categories import CategoryCreateView, CategoryDetailView, CategoryListView
# from goals.views.comments import CommentCreateView, CommentDetailView, CommentListView
# # from goals.views.comments import (
# #     GoalCommentCreateView,
# #     GoalCommentDetailView,
# #     GoalCommentListView,
# # )
# from goals.views.goals import GoalCreateView, GoalDetailView, GoalListView
#
# app_name = GoalsConfig.name
#
#
# urlpatterns = [
#     path('goal_category/create', CategoryCreateView.as_view(), name='create-category'),
#     path('goal_category/list', CategoryListView.as_view(), name='categories-list'),
#     path(
#         'goal_category/<int:pk>', CategoryDetailView.as_view(), name='category-details'
#     ),
#     path('goal/create', GoalCreateView.as_view(), name='create-goal'),
#     path('goal/list', GoalListView.as_view(), name='goals-list'),
#     path('goal/<int:pk>', GoalDetailView.as_view(), name='goal-details'),
#     path('goal_comment/create', CommentCreateView.as_view(), name='create-comment'),
#     path('goal_comment/list', CommentListView.as_view(), name='comments-list'),
#     path('goal_comment/<int:pk>', CommentDetailView.as_view(), name='comment-details'),
# ]
from goals.apps import GoalsConfig
from django.urls import path
from goals.views.categories import CreateCategoryView, CategoryListView, CategoryDetailView
from goals.views.goals import GoalListView, GoalCreateView, GoalDetailView
from goals.views.comments import GoalCommentListView, GoalCommentCreateView, GoalCommentDetailView
from goals.views.boards import BoardListView, BoardCreateView, BoardDetailView

app_name = GoalsConfig.name
urlpatterns = [
    # boards
    path('board/create', BoardCreateView.as_view(), name='create-board'),
    path('board/list', BoardListView.as_view(), name='board-list'),
    path('board/<int:pk>', BoardDetailView.as_view(), name='board-details'),
    # categories
    path('goal_category/create', CreateCategoryView.as_view(), name='create-category'),
    path('goal_category/list', CategoryListView.as_view(), name='category-list'),
    path('goal_category/<int:pk>', CategoryDetailView.as_view(), name='category-details'),
    # goals
    path('goal/create', GoalCreateView.as_view(), name='create-goal'),
    path('goal/list', GoalListView.as_view(), name='goals-list'),
    path('goal/<int:pk>', GoalDetailView.as_view(), name='goal-details'),
    # comments
    path('goal_comment/create', GoalCommentCreateView.as_view(), name='create-comment'),
    path('goal_comment/list', GoalCommentListView.as_view(), name='comments-list'),
    path('goal_comment/<int:pk>', GoalCommentDetailView.as_view(), name='comment-details'),
]
