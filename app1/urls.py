from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    # add task
    path('todo/',views.add_task, name='add_task'),

    # mark as done 
    path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'),

    # mark as undone
    path('mark_as_undone/<int:pk>/', views.mark_as_undone, name='mark_as_undone'),

    # delete
    path('delete/<int:pk>/', views.delete, name='delete'),

    # edit feature
    path('edit/<int:pk>/', views.edit, name='edit')
]