from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('urlcreated/', login_required(views.CreateShortUrl.as_view()), name="urlcreated"),
    path('<str:shortcode>/', views.Redirecting, name='redirecting'),
]
