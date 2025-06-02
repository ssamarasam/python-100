from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Movie

# pipenv install pylint-django

# Create your views here.


def index(request):
    # Movie.objects.all()
    # Movie.objects.filter(release_year=1988)
    # Movie.objects.get(id=1)

    movies = Movie.objects.all()

    # output = ','.join([m.title for m in movies])
    # return HttpResponse("Hello World!")  # map this to a url
    # return HttpResponse(output)

    return render(request, 'movies/index.html', {"movies": movies})


def detail(request, movie_id):
    # try:
    #     movie = Movie.objects.get(pk=movie_id)
    #     return render(request, 'movies/detail.html', {'movie': movie})
    # except Movie.DoesNotExist:
    #     raise Http404
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})
