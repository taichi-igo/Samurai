
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

# from user.views import user_list

from tweet.views import TweetViewSet, CommentViewSet
from user.views import UserViewSet

router = routers.DefaultRouter()
# router.register('user', user_list)
router.register('users', UserViewSet)
router.register('tweets', TweetViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
