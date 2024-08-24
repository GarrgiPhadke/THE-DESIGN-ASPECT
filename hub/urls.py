from django.urls import path
from . import views
urlpatterns = [
    path('hub/', views.hub, name='hub'),
    path('bedroom/', views.bedroom, name='bedroom'),
    path('livingroom/', views.livingroom, name='livingroom'),
    path('bathroom/', views.bathroom, name='bathroom'),
    path('kidsroom/', views.kidsroom, name='kidsroom'),
    path('office/', views.office, name='office'),
    path('poojaroom/', views.poojaroom, name='poojaroom'),
    path('tv/', views.tv, name='tv'),
    path('kitchen/', views.kitchen, name='kitchen'),
]