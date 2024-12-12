from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path ('', views.index, name='index'),
    path ('messager/', views.messager, name='messager'),
    path ('register/', views.sign_up, name='register'),
    path ('login/', views.sign_in, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('update_profile/', views.update_profile, name='update_profile'),
]