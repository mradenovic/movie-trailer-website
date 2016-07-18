"""This module contains class definitions for storing media files"""

import webbrowser

class Movie():
    """Movie class defines movies.

    Attributes:
        movie_title (str): Title of the movie
        movie_storyline (str): Sort description of the movie
        poster_image (str): Url of the poster image
        trailer_youtube (str): URL of the Youtube trailer
    """

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        # type: (object, object, object, object) -> object
        """
        Arguments:
            movie_title (str): Title of the movie
            movie_storyline (str): Sort description of the movie
            poster_image (str): Url of the poster image
            trailer_youtube (str): URL of the Youtube trailer
        """

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
