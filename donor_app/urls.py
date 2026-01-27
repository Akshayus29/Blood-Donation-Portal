from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # Main Landing Page
    path('register/', views.register, name='register_page'), # Registration Page
]