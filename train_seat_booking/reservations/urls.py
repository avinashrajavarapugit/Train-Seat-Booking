from django.urls import path
from . import views

urlpatterns = [
    path('reserve/', views.reserve_seats, name='reserve_seats'),
    path('', views.home, name='home'),
]
