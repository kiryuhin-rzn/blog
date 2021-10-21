from django.urls import path
from app_goods.views import items_list, update_news
from . import views



urlpatterns = [
    path('goods/', items_list, name='goods_list'),
    path('upload/', update_news, name='update_news'),
]