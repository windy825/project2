from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_safe, require_http_methods, require_POST

from movies.forms import ReviewForm
from .models import Movie, Review



# path('', views.movies),
@require_safe
def movies(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'movies/movies.html', context)


# path('<int:movie_pk>/', views.movie_detail),
@require_safe
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review_set = movie.review_set.all()
    form = ReviewForm()
    context = {
        'movie': movie,
        'review_set': review_set,
        'review_form': form
    }
    return render(request, 'movies/movie_detail.html', context)


# path('<int:movie_pk>/review/', views.review_create),
@require_POST
def review_create(request, movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.user = request.user
            review.save()
        return redirect('movies:movie_detail', movie.pk)
    return redirect('accounts:login')


# path('<int:movie_pk>/review/<int:review_pk>/update/', views.review_update),
# @login_required
# def review_update(request, movie_pk, review_pk):
#     pass


# path('<int:movie_pk>/review/<int:review_pk>/delete/', views.review_delete),
@require_POST
def review_delete(request, movie_pk, review_pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        if request.user == review.user:
            review.delete()
    return redirect('movies:movie_detail', movie_pk)
