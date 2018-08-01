import os

class Config:
    '''
    General configuration parent class
    '''
    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'
    # https://api.themoviedb.org/3/movie/550?api_key=e75ebc3f9b1295e781106c8a49fe1edb
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')

class ProdConfig(Config):
    '''
    Production configuration child class

     Args:
     Config: The parent configuration class with General configuration settings
     '''
    pass

class DevConfig(Config):
    """
    Development configuration child class
    Args:
    Config: The parent configuration class with General configuration settings
    """
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
