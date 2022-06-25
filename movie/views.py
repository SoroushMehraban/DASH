from django.shortcuts import render, redirect
from django.views import View
from .models import Movie


class Home(View):
    def get(self, request):
        return render(request, 'movie/home.html', context={
            'movies': Movie.objects.all()
        })


class Movies(View):
    def get(self, request, movie_id):
        movie = Movie.objects.filter(id=movie_id).first()
        if movie:
            return render(request, 'movie/movie.html', context={'movie': movie})
        else:
            return redirect('NotExist404')


class NotExist404(View):
    def get(self, request):
        return render(request, 'movie/404.html')
