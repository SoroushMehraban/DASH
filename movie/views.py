from django.shortcuts import render
from django.views import View
from .models import Movie

class Home(View):
    def get(self, request):
        return render(request, 'movie/home.html', context={
            'movies': Movie.objects.all()
        })
