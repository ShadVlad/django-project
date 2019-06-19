from django.urls import path

from .views import (
    product_list, product_detail
)


app_name = 'products'


urlpatterns = [
    path('<int:pk>/', product_detail, name='detail'),
    path('', product_list, name='index'),
]
