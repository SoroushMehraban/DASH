from django.urls import path
from movie.views import Home, Movies, NotExist404

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('movie/<int:movie_id>', Movies.as_view(), name="movies"),
    path('404/', NotExist404.as_view(), name='NotExist404')
]
