from django.urls import path
from . import views

urlpatterns = [
    #path('data/', views.getData),
    path('chart/', views.chartDemo),
    path('', views.chartDemo),
]