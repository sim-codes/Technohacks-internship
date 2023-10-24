from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.todo_create_list, name='todo_create_list'),
    path('todos/<int:pk>', views.TodoDetailView.as_view(), name='todo_detail'),
    path('todos/edit/<int:pk>', views.TodoUpdateView.as_view(), name='todo_edit'),
    path('todos/delete/<int:pk>', views.TodoDeleteView.as_view(), name='todo_delete'),
    path('accounts/signup', views.register, name='signup'),
    
]