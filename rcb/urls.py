from rcb.views import *
from django.urls import path

urlpatterns=[
    path('captain/',captain,name='captain'),
]