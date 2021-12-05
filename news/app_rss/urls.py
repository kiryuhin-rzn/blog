from django.urls import path
from app_rss.feeds import LatestLodgingFeed, LatestNewsFeed


urlpatterns = [
    path('latest/feed/', LatestLodgingFeed()),
    path('last/feed/', LatestNewsFeed())
]