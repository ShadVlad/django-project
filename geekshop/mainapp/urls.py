from django.urls import path
import mainapp.views as mainapp

from .views import (
    index, contacts, about
)


app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.products, name='index'),
    path('category/<int:pk>/', mainapp.products, name='category'),
]
'''
urlpatterns = [
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('', index, name='index'),
]
'''