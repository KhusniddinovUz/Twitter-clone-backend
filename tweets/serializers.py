from rest_framework import serializers
from .models import TweetModel


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = TweetModel
        fields = '__all__'
