from django.urls import path
from app_goods.views import AuthorList, BookList, BookDetail
#from app_goods.views import items_list, update_news
#from . import views


urlpatterns = [
    path('author/', AuthorList.as_view(), name='author_list'),
    path('book/', BookList.as_view(), name='book_list'),
    path('book/<int:pk>', BookDetail.as_view(), name='book_detail'),
    #path('goods/', items_list, name='goods_list'),
    #path('upload/', update_news, name='update_news'),
]
