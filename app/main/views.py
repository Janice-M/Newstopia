from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_movies,get_movie,search_movie
from ..models import Review
from .forms import ReviewForm




#views 
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    #getting popular movies
    popular_movies = get_movies('popular')
    upcoming_movie = get_movies('upcoming')
    now_showing_movie = get_movies('now_playing')
    title = 'Home - Welcome to The Best best Movie Review Website Online'
    
    # message = 'Hello World'
    search_movie = request.args.get('movie_query')

    if search_movie:
        return redirect(url_for('main.search',movie_name = search_movie))
    else:
        return render_template('index.html',title = title, popular = popular_movies,upcoming = upcoming_movie, now_playing = now_showing_movie)

@main.route('/movie/<int:id>')
def movie(id):
    '''
    View root page function theat returns the index pages and its  data 
    '''
    movie = get_movie(id)
    title = f'{movie.title}'
    reviews = Review.get_reviews(movie.id)
    return render_template('movie.html',  title = title, movie = movie, reviews = reviews)

@main.route('/search/<movie_name>')
def search(movie_name):
    '''
    view function to display search results
    '''
    movie_name_list = movie_name.split(" ")
    movie_name_format = "+".join(movie_name_list)
    searched_movies = search_movie(movie_name_format)
    title = f'search result for {movie_name}'
    return render_template('search.html', title = title, movies = searched_movies)


@main.route('/movie/review/new/<int:id>', methods= ['GET','POST'])
def new_review(id):
    form = ReviewForm()
    movie = get_movie(id)

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        new_review = Review(movie.id,title,movie.poster,review)
        new_review.save_review()
        return redirect(url_for('movie',id = movie.id ))
    
    title = f'{movie.title} review'
    return render_template('new_review.html', title = title, review_form = form, movie = movie)