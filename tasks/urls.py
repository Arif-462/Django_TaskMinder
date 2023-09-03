from django.urls import path
from . import views

urlpatterns = [
    path('add_task/',views.added_task, name='add_task'),
    path('show_task/',views.show_task, name='show_task'),
    path('completed_task/',views.completed_task, name='completed_task'),
    path('edit/<int:id>/',views.edit_task, name = 'edit_task'),
    path('del_task/<int:id>/', views.delete_task, name = 'del_task'),
    path('complete/<int:id>/', views.complete_status, name = 'complete'),
    path('completed/', views.completed_list, name = 'completed_list'), 
    path('medium/', views.medium_ca, name = 'medium'), 
    path('high/', views.high_cat, name = 'high'), 
    path('low/', views.low_cat, name = 'low'), 
       
    
    
]
  