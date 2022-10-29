from django.urls import path
from .import views
urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('explore/', views.explore),
    path('gallery/', views.gallery),
    path('contact/', views.contact),
    path('login/', views.login),
]
