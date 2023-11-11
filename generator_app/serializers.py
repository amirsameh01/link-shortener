from rest_framework import serializers
from urlgenerator import models


class UrlsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Urls
        fields = '__all__'
