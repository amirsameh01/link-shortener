from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('', include('generator_app.urls')),
    path('', include('urlgenerator.urls')),

]
