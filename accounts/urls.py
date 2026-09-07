from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profiles/', views.profiles, name='profiles'),
    path('profile_edit/<int:user_id>/', views.profile_edit, name='profile_edit'),
    path('missions/', views.missions, name='missions'),
    path('mission_add/', views.mission_add, name="mission_add"),
    path('mission_edit/<int:mission_id>/', views.mission_edit, name="mission_edit"),
    path('mission_delete/<int:mission_id>/', views.mission_delete, name='mission_delete'),
]
