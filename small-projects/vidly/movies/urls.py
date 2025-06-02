# list objects that maps urlsurl endpoints to our view function

from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    # pass a refercne to the funtion
    path('', views.index, name='index'),
    path('<int:movie_id>', views.detail, name='detail')
]
