from django.urls import path
from . import views

urlpatterns = [
    path('', views.crypto_purchased, name='index'),
    path('add_crypto_purchased', views.add_crypto_purchased, name='add_crypto_purchased'),
    path('api/get_api_data/', views.get_api_data, name='get_api_data'),

]