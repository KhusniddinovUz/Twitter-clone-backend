from rest_framework import routers
from .api import TweetViewset, OwnersTweet, CommentList, CreateComment, DeleteComment, DeleteTweet
from django.urls import path

router = routers.DefaultRouter()
router.register('', TweetViewset, 'tweets')

urlpatterns = [
    path('own/', OwnersTweet.as_view({'get': 'list'}), ),
    path('delete/<int:pk>', DeleteTweet.as_view()),
    path('comments/<tweet_id>', CommentList.as_view()),
    path('comment/<int:pk>', DeleteComment.as_view()),
    path('comment/', CreateComment.as_view()),
]

urlpatterns += router.urls
