from django.urls import path
from app_users.views import AnotherLoginView, logout_view, register_view, UserAccountView, UserBalanceView


urlpatterns = [
    path('login/', AnotherLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('account/', UserAccountView.as_view(), name='account'),
    path('balance/', UserBalanceView.as_view(), name='balance'),
]
