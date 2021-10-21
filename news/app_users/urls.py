from django.urls import path
from app_users.views import AnotherLoginView, logout_view, register_view


urlpatterns = [
    path('login/', AnotherLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
]
