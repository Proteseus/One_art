from unicodedata import name
from django.urls import path
from django.contrib import admin
from . import views
from .decorators import *

urlpatterns = [
    path('', views.home, name='home'),
    path('browse/', views.browse, name='browse'),
    path('buyer/', views.buyer, name='buyer_temp'),
    path('list_art/', views.art, name='list_art'),
    path('update_art/<str:pk>', views.updateOrder, name='update_art'),
    path('delete_art/<str:pk>', views.deleteArt, name='delete_art'),
    path('signup/', views.registerUser, name='register'),
    path('signin/', views.loginPage, name='signin'),
    path('logout/', views.logoutUser, name='signout'),
    path('artist/', views.createListing, name='artist'),
    path('assets/', views.listArt, name='assets'),
    path('assets_buyer/', views.listArtBuyer, name='assets_buyer'),
]