from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

movies = [
    {'title': 'Catchfire','year': 1990,},
    {'title': 'Mighty Ducks the Movie: The First Face-Off', 'year': 1997,},
    {'title': 'Le Zombi de Cap-Rouge', 'year': 1997,},
]

movies_data = {1:'The Dark Knight', 2:'12 Angry Men', 3:'Il buono, il brutto, il cattivo'}

def movie_view(request):

    context = {'movies': movies}
    return render(request, 'movies/index.html', context=context)

# def movie_view(request, movie_id):
#
#   movie_title = movies_data.get(movie_id)
#   return HttpResponse(f'Это фильм {movie_title}')