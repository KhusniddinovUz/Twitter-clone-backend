from rest_framework import serializers
from .models import TweetModel, Comment


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = TweetModel
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
