from django.urls import path
from . import views
urlpatterns = [
    # http://127.0.0.1:8000/api
    path('', views.index),
    path('register/', views.register),
    path('check_name/<str:name>/', views.check_name)
]