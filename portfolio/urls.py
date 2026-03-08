from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name='projects'),
    path('profile/', views.profile, name = 'profile'),
    path('project/<int:pk>/', views.project_detail, name = 'project_detail'),
]   
