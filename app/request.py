
import urllib.request,json
from .models import Article


# Getting api key
api_key = None

# Getting the movie base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']


def get_movies(category):
    '''
    Function that gets the json responce to our url requestarticles
    '''
    get_movies_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_movies_url) as url:
        get_movies_data = url.read()
        get_movies_response = json.loads(get_movies_data)

        movie_results = None

        if get_movies_response['articles']:
            movie_results_list = get_movies_response['articles']
            movie_results = process_results(movie_results_list)


    return movie_results


def process_results(movie_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects
    Args:
        movie_list: A list of dictionaries that contain movie details
    Returns :
        movie_results: A list of movie objects
    '''
    movie_results = []
    for movie_item in movie_list:
        author = movie_item.get('author')
        title = movie_item.get('title')
        description = movie_item.get('description')
        url = movie_item.get('url')
        urlToImage = movie_item.get('urlToImage')
        publishedAt = movie_item.get('publishedAt')
        content = movie_item.get('content')

        movie_object = Article( author ,title, description, url, urlToImage , publishedAt, content)
        movie_results.append(movie_object)

    return movie_results

def get_movie():
    get_movie_details_url = base_url.format(api_key)

    with urllib.request.urlopen(get_movie_details_url) as url:
        movie_details_data = url.read()
        movie_details_response = json.loads(movie_details_data)

        movie_object = None
        if movie_details_response:
            author = movie_details_response.get('author')
            title = movie_details_response.get('title')
            description = movie_details_response.get('description')
            url = movie_details_response.get('url')
            urlToImage = movie_details_response.get('urlToImage')
            publishedAt = movie_details_response.get('publishedAt')
            content = movie_details_response.get('content')

            movie_object = Article( author ,title, description, url, urlToImage , publishedAt, content)

    return movie_object
def search_movie(movie_name):
    search_movie_url = 'https://api.themoviedb.org/3/search/movie?api_key={}&query={}'.format(api_key,movie_name)
    with urllib.request.urlopen(search_movie_url) as url:
        search_movie_data = url.read()
        search_movie_response = json.loads(search_movie_data)

        search_movie_results = None

        if search_movie_response['articles']:
            search_movie_list = search_movie_response['articles']
            search_movie_results = process_results(search_movie_list)


    return search_movie_results