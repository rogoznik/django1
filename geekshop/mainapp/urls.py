from django.urls import path
from .views import products

app_name = 'mainapp'

urlpatterns = [
    path('', products, name='index'),
    path('home/', products, name='home'),
    path('office/', products, name='office'),
    path('modern/', products, name='modern'),
    path('classic/', products, name='classic'),
]