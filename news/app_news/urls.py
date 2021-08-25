from django.urls import path
from . import views
from .views import NewsListView, NewsDetailView, NewsUpdateView


urlpatterns = [
    path('', NewsListView.as_view(), name='news_list'),
    path('news/<int:pk>', NewsDetailView.as_view(), name='news_detail'),
    path('news/add/', views.add_news, name='add_news'),
    path('news/<int:pk>/edit/', NewsUpdateView.as_view(), name='news_edit'),
    path('post/<int:pk>/comment/', views.add_comment_to_news, name='add_comment_to_news'),
]
