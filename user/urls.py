from django.urls import path
from django.urls.conf import include
from . import views



urlpatterns=[
    path('',views.index),
    path('main',views.index1),
    path('main1/<int:id>',views.index2),
    path('log',views.login,name="log_user"),
    path('home',views.home,name="home"),
    path('logout',views.logout,name="logout_user"),
    path('profile',views.prof,name="profile"),
    path('chpwd',views.chpwd,name="chpwd")
]