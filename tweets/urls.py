from rest_framework import routers
from .api import TweetViewset, OwnersTweet, CommentSystem
from django.urls import path

router = routers.DefaultRouter()
router.register('', TweetViewset, 'tweets')

urlpatterns = [
    path('own/', OwnersTweet.as_view({'get': 'list'}), ),
    path('comment/', CommentSystem.as_view()),
]

urlpatterns += router.urls
