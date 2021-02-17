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


# Commenting System
class CommentSystem(generics.ListCreateAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = CommentSerializer

    def get_queryset(self):
        # queryset = TweetModel.objects.get(owner=self.request.user.id).comment.all()
        # return queryset
        print(self.request.data)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user, username=self.request.user.username)
