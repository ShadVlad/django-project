from django.urls import path

from .views import (
    index, contacts, about
)


app_name = 'mainapp'


urlpatterns = [
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('', index, name='index'),
]
