# list objects that maps urlsurl endpoints to our view function

from django.urls import path
from . import views

urlpatterns = [
    # pass a refercne to the funtion
    path('', views.index, name='movies_index'),
    path('<int:movie_id>', views.detail, name='movies_detail')
]
