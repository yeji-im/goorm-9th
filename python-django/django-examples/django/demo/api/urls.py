from django.urls import path
from . import views

urlpatterns = [
    path('health/', views.health, name='health'),
    path('samples/', views.list_samples, name='list_samples'),
]
