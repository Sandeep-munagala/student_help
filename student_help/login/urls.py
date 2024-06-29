from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('help/', views.help, name='help'),
    path('resources/', views.resources, name='resources'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
]
