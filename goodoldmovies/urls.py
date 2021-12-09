from django.urls import path
import movies.views as movies_views, movie_view

urlpatterns = [
    path('', movies_views.movie_view, name='main'),
    path('movies/<int:movie_id>', movie_view),

]
