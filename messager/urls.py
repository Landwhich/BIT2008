from django.urls import path
from . import views

urlpatterns = [
    path ('', views.index, name='index'),
    path ('register/', views.sign_up, name='register'),
]