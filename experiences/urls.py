from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_experiences, name='all_experiences'),
    path('experience/<int:experience_id>/', views.view_experience_details, name='experience_details'),
    path('add/', views.add_experience, name='add_experience'),
    path('edit/<int:experience_id>/', views.edit_experience, name='edit_experience'),
    path('delete/<int:experience_id>/', views.delete_experience, name='delete_experience'),
]
