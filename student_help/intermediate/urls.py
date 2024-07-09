from django.urls import path
from . import views

urlpatterns = [
    path('', views.intermediate_home, name='intermediate_home'),
    path('my_network', views.network, name='my_network'),
    path('computer_science', views.computer_science, name='computer_science'),
    path('electrical_and_communications', views.electrical_and_communications, name='electrical_and_communications'),
    path('mechanical', views.mechanical, name='mechanical'),
    path('civil', views.civil, name='civil'),
    path('chemical', views.chemical, name='chemical'),
    path('others', views.others, name='others'),
]

