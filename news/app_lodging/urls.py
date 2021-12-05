from django.urls import path
from app_lodging.views import LodgingListView, AboutView, ContactsView, NewsListView, LodgingDetailView, NewsDetailView


urlpatterns = [
    path('lodging/', LodgingListView.as_view(), name='lodging_list'),
    path('lodging/<int:pk>', LodgingDetailView.as_view(), name='lodging_detail'),
    path('about/', AboutView.as_view(), name='about'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('news/', NewsListView.as_view(), name='news_list'),
    path('news/<int:pk>', NewsDetailView.as_view(), name='news_details'),
]
