from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('help/', views.help, name='help'),
    path('resources/', views.resources, name='resources'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login_user, name='login'),
    path('register_engineering/', views.register_engineering, name='register_engineering'),
    path('register_intermediate/',views.register_intermediate,name = 'register_intermediate')
]
