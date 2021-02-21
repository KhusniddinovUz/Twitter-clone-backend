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


# Getting comments
class CommentList(generics.ListAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


# Creating a comment
class CreateComment(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user, username=self.request.user.username)


# Deleting a comment
class DeleteComment(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
