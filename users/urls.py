from django.urls import path
from .views import UserLoginView, UserRegisterView,logout_view

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),
]
