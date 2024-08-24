from django.urls import path
from . import views
urlpatterns = [
    path('myservice/', views.myservice, name='myservice'),
]