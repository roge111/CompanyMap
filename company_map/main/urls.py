from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.start, name='start_page'),
    path('company_map', views.company_map, name='company_map')
]