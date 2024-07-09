# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.engineering_home, name='engineering_home'),
    #path('my_network', views.network, name='my_network'),
    # Add other paths here
]

