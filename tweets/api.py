from .serializers import TweetSerializer, CommentSerializer
from .models import TweetModel, Comment
from rest_framework import viewsets, permissions, generics


# TweetViewset
class TweetViewset(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TweetSerializer

    def get_queryset(self):
        ordered = TweetModel.objects.order_by('-created_at')
        return ordered

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user, username=self.request.user.username)


# OwnersTweet
class OwnersTweet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TweetSerializer

    def get_queryset(self):
        ordered = TweetModel.objects.filter(owner=self.request.user).order_by('-created_at')
        return ordered


# Commenting System for creating and getting
class CommentList(generics.ListAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = CommentSerializer

    def get_queryset(self):
        tweet_id = self.kwargs.get('tweet_id')
        queryset = TweetModel.objects.get(pk=tweet_id).comment.all()
        return queryset


# Commenting System for deleting
class CommentSingle(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user, username=self.request.user.username)
