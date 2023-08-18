# from django.urls import path
#
# from .views import VerificationView
#
# urlpatterns = [
#     path('verify', VerificationView.as_view()),
# ]
from django.urls import path

from bot import views

app_name = 'bot'

urlpatterns = [
    path('verify', views.VerificationCodeView.as_view(), name='verify'),
]
