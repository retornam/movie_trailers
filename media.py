# Movie class to be used for creating instances of movies. Contains title
# poster image link, trailer link and summary
class Movie():
    """Movie structure with a title, a poster image link,
    a trailer link and a summary"""

    # movie title, by default will be set to 'title'
    title = "title"

    # movie poster image url, by default will be set to 'http://fake.jpg'
    poster_image_url = "http://fake.jpg"

    # movie trailer url, by default will be set to 'http://fake.mov'
    trailer_youtube_url = "http://fake.mov"

    # movie summary
    movie_summary = "summary"

    # constructor to instantiate new movies and pass arguments directly
    def __init__(self, title, poster_image_url, trailer_youtube_url,
                 movie_summary):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.movie_summary = movie_summary
