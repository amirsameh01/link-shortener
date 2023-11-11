from django.urls import path
from .views import LinkCreator

urlpatterns = [
    path('generate/', LinkCreator.as_view()),
]
