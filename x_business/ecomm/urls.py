from django.urls import path
from . import views

urlpatterns = [
    path('', views.ecomm),
    path('ecomm/', views.ecomm, name='ecomm'),
    path('welcome/', views.welcome),
    path('home/', views.home, name='home'),
    path('inventory/', views.inventory, name='inventory'),
    path('search/', views.search, name='search'),
    path('store/', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('marketplace/', views.marketplace, name='marketplace'),
    path('profile', views.profile, name='profile'),
    
    path('get_new_store_details/', views.get_new_store_details),
    path('add_new_store/', views.add_new_store, name='add_new_store'),
]