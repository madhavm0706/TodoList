from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.todo_list,name='index'),
    path('create/',views.todo_create,name='todo_create'),
     path('<id>/',views.todo_details,name='todo_details'),
      path('<id>/update/',views.todo_update,name='todo_update'),
      path('<id>/delete/',views.todo_delete,name='todo_delete'),
]
