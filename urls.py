from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user_details_registration/', views.user_details_registration, name='user_details_registration'),
    path('user_details_view/', views.user_details_view, name='user_details_view'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('product_registration/', views.product_registration, name='product_registration'),
    path('product_view/', views.product_view, name='product_view'),
]   
