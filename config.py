import os

class Config:

    NEWS_API_BASE_URL ='https://newsapi.org/v2/top-headlines?country=us&apiKey=debc59c4df7748388daae665844a6ca2'
    NEWS_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}