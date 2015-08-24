from media import Movie
from fresh_tomatoes import open_movies_page

movies = []

movie1 = Movie("Furious 7", "http://ia.media-imdb.com/images/M/MV5BMTM3NTg2NDQzOF5BMl5BanBnXkFtZTcwNjc2NzQzOQ@@._V1_SX214_AL_.jpg", "https://www.youtube.com/watch?v=dKi5XoeTN0k", "After defeating international terrorist Owen Shaw, Dominic Toretto (Vin Diesel), Brian O'Conner (Paul Walker) and the rest of the crew have separated to return to more normal lives. However, Deckard Shaw (Jason Statham), Owen's older brother, is thirsty for revenge. A slick government agent offers to help Dom and company take care of Shaw in exchange for their help in rescuing a kidnapped computer hacker who has developed a powerful surveillance program.")
movie2 = Movie("Focus", "http://ia.media-imdb.com/images/M/MV5BMTUwODg2OTA4OF5BMl5BanBnXkFtZTgwOTE5MTE4MzE@._V1_SX214_AL_.jpg", "https://www.youtube.com/watch?v=MxCRgtdAuBo", "Nicky (Will Smith), a veteran con artist, takes a novice named Jess (Margot Robbie) under his wing. While Nicky teaches Jess the tricks of the trade, the pair become romantically involved; but, when Jess gets uncomfortably close, Nicky ends their relationship. Three years later, Nicky is in Buenos Aires working a very dangerous scheme when Jess -- now an accomplished femme fatale -- unexpectedly shows up. Her appearance throws Nicky for a loop at a time when he cannot afford to be off his game.")
movie3 = Movie("Insurgent", "http://ia.media-imdb.com/images/M/MV5BMTgxOTYxMTg3OF5BMl5BanBnXkFtZTgwMDgyMzA2NDE@._V1_SX214_AL_.jpg", "https://www.youtube.com/watch?v=UtgPdoxU-SY", "Now on the run from Jeanine (Kate Winslet) and the rest of the power-hungry Erudites, Tris (Shailene Woodley) and Four (Theo James) search for allies and answers in the ruins of Chicago. They must find out what Tris' family sacrificed their lives to protect and why the Erudites will do anything to stop them. Side by side, Tris and Four face one seemingly insurmountable challenge after another, as they unravel the secrets of the past and -- ultimately -- the future of their world.")

movies.append(movie1)
movies.append(movie2)
movies.append(movie3)

open_movies_page(movies)
