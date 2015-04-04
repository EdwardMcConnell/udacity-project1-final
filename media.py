class Movie():
    """This class provies a way to store and retrieve movie related information"""

    # Identify the family ratings
    FAMILY_RATINGS = ['G','PG','PG-13']

    # Initialize the class
    def __init__(self, 
                 movie_title, 
                 poster_image, 
                 youtube_trailer,
                 rating,
                 synopsis,
                 duration,
                 release_date):

        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_trailer
        self.rating = rating
        self.synopsis = synopsis
        self.duration = duration
        self.release_date = release_date

    # is_family_friendly determines if the movie is 
    # family friendly based on the supplied rating
    # @returns boolean True if Family Friendly, False if Not
    def is_family_friendly(self):

        if self.rating in Movie.FAMILY_RATINGS:
            return True
        else:
            return False

