"""
URL configuration for firstwebpage project.
"""
from django.contrib import admin
from django.urls import path
from flatpages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('hello/', views.home_text, name='hello'),
    path('hello-default/', views.home_text_default, name='hello-default'),
    path('static-handler/', views.static_handler, name='static-handler'),
]
