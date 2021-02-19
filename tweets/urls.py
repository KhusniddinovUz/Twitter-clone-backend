from rest_framework import routers
from .api import TweetViewset, OwnersTweet, CommentList, CommentSingle
from django.urls import path

router = routers.DefaultRouter()
router.register('', TweetViewset, 'tweets')

urlpatterns = [
    path('own/', OwnersTweet.as_view({'get': 'list'}), ),
    path('comments/<tweet_id>', CommentList.as_view()),
    path('comment/', CommentSingle.as_view())
]

urlpatterns += router.urls
