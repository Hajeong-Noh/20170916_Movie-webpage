import webbrowser


class Movie():
    """ This class includes information and methods of movie """

    """ This constructor takes title, story line, poster image and trailer url
        of movies """
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    """ This function opens the trailer of movies on Youtube """
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
