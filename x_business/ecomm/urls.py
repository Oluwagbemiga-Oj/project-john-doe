from django.urls import path
from . import views

urlpatterns = [
    path('', views.ecomm),
    path('ecomm/', views.ecomm, name='ecomm'),
    path('welcome/', views.welcome),
    path('get_new_store_details/', views.get_new_store_details),
    path('add_new_store/', views.add_new_store, name='add_new_store'),
]