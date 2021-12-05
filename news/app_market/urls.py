from django.urls import path
from app_market.views import ShopListView, ShopDetailView, CartListView, ReportSalesView
#from app_goods.views import items_list, update_news
#from . import views


urlpatterns = [
    path('shops/', ShopListView.as_view(), name='shop_list'),
    path('cart/', CartListView.as_view(), name='cart'),
    path('report_sales/', ReportSalesView.as_view(), name='report_sales'),
    path('shops/<int:pk>', ShopDetailView.as_view(), name='product_detail'),
    #path('book/', BookList.as_view(), name='book_list'),
    #path('book/<int:pk>', BookDetail.as_view(), name='book_detail'),
    #path('goods/', items_list, name='goods_list'),
    #path('upload/', update_news, name='update_news'),
]