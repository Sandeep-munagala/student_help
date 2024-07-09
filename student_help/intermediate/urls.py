from django.urls import path
from . import views

urlpatterns = [
    path('', views.intermediate_home, name='intermediate_home'),
    path('my_network',views.network,name = "mynetwork"),
]
