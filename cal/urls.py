# cal/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('cal/', views.cal, name='cal'),          # URL for cal.html
    path('cal_page/', views.cal_page, name='cal_page'),  # URL for cal_page.html
     path('cal_final/', views.cal_final, name='cal_final'),
]
