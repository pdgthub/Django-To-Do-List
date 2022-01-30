from django.urls import path
from . import views

urlpatterns = [
path('', views.todolist, name='todolist'),
path('add_item', views.add_item, name='add_item'),
path('add_category', views.add_category, name='add_category'),
path('delete_category/<str:pk>/', views.delete_category, name="delete_category"),
path('delete_item/<str:pk>/', views.delete_item, name="delete_item")

]