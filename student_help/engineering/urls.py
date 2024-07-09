from django.urls import path
from . import views

urlpatterns = [
    path('', views.engineering_home, name='engineering_home'),
]
