from django.contrib import admin
from django.urls import path
from authApp import views
urlpatterns = [
    path('',views.index,name='authhome'),
    path('user/<choice>',views.userchoice, name='userchoice'),
]
