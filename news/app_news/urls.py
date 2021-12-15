from django.urls import path
from . import views
from app_news.views import upload_news
from .views import NewsListView, NewsDetailView, NewsUpdateView, NewsCreateView, NewsDeleteView, NewsSearchView


urlpatterns = [
    path('', NewsListView.as_view(), name='news_list'),
    path('news/search/', NewsSearchView.as_view(), name='news_search'),
    path('news/<int:pk>', NewsDetailView.as_view(), name='news_detail'),
    path('news/add/', NewsCreateView.as_view(), name='add_news'),
    path('news/<int:pk>/edit/', NewsUpdateView.as_view(), name='news_edit'),
    path('news/<int:pk>/delete/', NewsDeleteView.as_view(), name='news_delete'),
    path('post/<int:pk>/comment/', views.add_comment_to_news, name='add_comment_to_news'),
    path('news/upload/', views.upload_file, name='upload'),
    path('news/<int:pk>/upload_files/', views.upload_files, name='upload_files'),
    #path('news/uploads/', Rectangle, name='uploads'),
    path('news/uploads/', upload_news, name='uploads'),
    #path('news/<int:pk>/form_upload/', views.form_upload, name='form_upload'),
]
