from django.urls import path
from . import views

urlpatterns = [
       path('', views.index, name='index'),
       path('login/', views.login_view, name='login'),
       path('register/', views.register_view, name='register'),
       path('dashboard/', views.dashboard, name='dashboard'),
       path('add-task/', views.add_task, name='add_task'),
       path('edit-task/<int:task_id>/', views.edit_task, name='edit_task'),
       path('toggle-task/<int:task_id>/', views.toggle_task, name='toggle_task'),
       path('delete-task/<int:task_id>/', views.delete_task, name='delete_task'),
       path('logout/', views.logout_view, name='logout'),
]