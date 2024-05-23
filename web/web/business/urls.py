from django.urls import path
from .views import RegisterUserView, AuthenticateUserView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', AuthenticateUserView.as_view(), name='login'),
]