from rest_framework import routers
from .api import TweetViewset, OwnersTweet
from django.urls import path

router = routers.DefaultRouter()
router.register('', TweetViewset, 'tweets')

urlpatterns = [
    path('own/', OwnersTweet.as_view({'get': 'list'}), )
]

urlpatterns += router.urls
