from django.shortcuts import render
from django.http import HttpResponse
from movie.models import Movie
#from movie.models import *


def myView(request):
        text="""<h1>welcome to my app !</h1>"""
        return HttpResponse(text)

def homepage(request):
	return render(request, 'movie/home.html')

def results(request):
	m = Movie()
	if request.GET.get('q') is not None:
		searchname = request.GET.get('q')
		movieData = m.getMovieData(searchname)
		return render(request, 'movie/home.html', {'movieData': movieData, 'search': True})
	else:
		return render(request, 'movie/home.html')
