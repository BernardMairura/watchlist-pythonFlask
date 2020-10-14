class Config:
    '''
    General configuration parent class
    '''
    pass



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{https://api.themoviedb.org/3/movie/550?api_key=02f7be3ce0eed59b9c343a691c817cf0}?api_key={02f7be3ce0eed59b9c343a691c817cf0}'


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True