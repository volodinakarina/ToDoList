from django.urls import path

from core.views import SingUpView, LoginView, ProfileView, UpdatePasswordView

# from . import views
#
# urlpatterns = [
#     path('signup', views.UserSingUpView.as_view(), name='sign_up'),
#     path('login', views.UserLoginView.as_view(), name='sign_up'),
#     path('profile', views.UserRetrieveUpdateAPIView.as_view(), name='profile'),
#     path(
#         'update_password',
#         views.UserUpdatePasswordAPIView.as_view(),
#         name='update_password',
#     ),
# ]
urlpatterns = [
    path('signup', SingUpView.as_view(), name='signup'),
    path('login', LoginView.as_view(), name='login'),
    path('profile', ProfileView.as_view(), name='profile'),
    path('update_password', UpdatePasswordView.as_view(), name='update_password'),
]
