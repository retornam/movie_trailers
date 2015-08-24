class Movie():
	title = "title"
	poster_image_url = "poster"
	trailer_youtube_url = "trailer"
	movie_summary = "summary"
	def __init__(self, title, poster_image_url, trailer_youtube_url, movie_summary):
		self.title = title
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url
		self.movie_summary = movie_summary
