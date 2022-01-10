from django.urls import path
from app_todo.views import ToDoListView, ToDoDeleteView, ToDoDetailView


urlpatterns = [
    path('', ToDoListView.as_view(), name='todo_list'),
    path('<int:pk>', ToDoDetailView.as_view(), name='todo_detail'),
    path('<int:pk>/delete/', ToDoDeleteView.as_view(), name='todo_delete')
]