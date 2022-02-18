from django.urls import path
from django.urls.conf import include
from . import views



urlpatterns=[
    path('home',views.index),
    path('main',views.index1)
]