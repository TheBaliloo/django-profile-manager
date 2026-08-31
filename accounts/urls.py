from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('edit/<int:user_id>', views.edit, name='edit'),
]
