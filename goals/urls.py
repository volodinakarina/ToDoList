from django.urls import path

from goals.apps import GoalsConfig
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
