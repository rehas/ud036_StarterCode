import webbrowser


class Movie():
    """This class represents the structure of a movie """
    """It initializes a movie object with
    Title,
    Storyline,
    Poster Image URL,
    Youtube Trailer, URL as arguments
    """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    def __init__(self,
                 movie_title,
                 movie_storyline,
                 poster_image,
                 trailer_youtube):

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """This method shows the trailer of the movie from youtube """
        webbrowser.open(self.trailer_youtube_url)
