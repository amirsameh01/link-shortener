from django.db import models
from django.contrib.auth.models import User


class Urls(models.Model):
    url_original = models.URLField(max_length=225, null=True, blank=True)
    url_shortened = models.CharField(max_length=15)
    clicks = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
