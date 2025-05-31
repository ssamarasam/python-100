# list objects that maps urlsurl endpoints to our view function

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')  # pass a refercne to the funtion

]
