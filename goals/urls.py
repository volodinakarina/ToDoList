from django.urls import path

from .views import categories, comments, goals

urlpatterns = [
    path('goal_category/list', categories.CategoryListView.as_view()),
    path('goal_category/create', categories.CategoryCreateView.as_view()),
    path('goal_category/<int:pk>', categories.CategoryDetailView.as_view()),
    path('goal/list', goals.GoalListView.as_view()),
    path('goal/create', goals.GoalCreateView.as_view()),
    path('goal/<int:pk>', goals.GoalDetailView.as_view()),
    path('goal_comment/list', comments.CommentListView.as_view()),
    path('goal_comment/create', comments.CommentCreateView.as_view()),
    path('goal_comment/<int:pk>', comments.CommentDetailView.as_view()),
]
