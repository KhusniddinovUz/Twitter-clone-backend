from .serializers import TweetSerializer
from .models import TweetModel
from rest_framework import viewsets, permissions


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


class OwnersTweet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TweetSerializer

    def get_queryset(self):
        ordered = TweetModel.objects.filter(owner=self.request.user).order_by('-created_at')
        return ordered
