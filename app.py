from flask import Flask
from flask import render_template
import random 
import threading
import webbrowser


app = Flask(__name__)


@app.route('/')
def index():
  movieOne = {
   'mtitle': 'Furious 7',
   'trailer_youtube_id': 'dKi5XoeTN0k',
   'summary': '''After defeating international terrorist Owen Shaw,
                 Dominic Toretto (Vin Diesel), Brian O'Conner (Paul Walker) and the rest
                of the crew have separated to return to more normal lives. However,
                Deckard Shaw (Jason Statham), Owen's older brother, is thirsty for
                revenge. A slick government agent offers to help Dom and company take
                care of Shaw in exchange for their help in rescuing a kidnapped
                computer hacker who has developed a powerful surveillance program.''',
   'poster_image_url': 'http://ia.media-imdb.com/images/M/MV5BMTM3NTg2NDQzOF5BMl5BanBnXkFtZTcwNjc2NzQzOQ@@._V1_SX214_AL_.jpg'
  }
  movieTwo = {
  'mtitle': 'Focus',
  'trailer_youtube_id': 'MxCRgtdAuBo',
  'summary': '''
             Nicky (Will Smith), a veteran con artist, takes a novice named Jess
            (Margot Robbie) under his wing. While Nicky teaches Jess the tricks of
            the trade, the pair become romantically involved; but,
            when Jess gets uncomfortably close, Nicky ends their relationship.
            Three years later, Nicky is in Buenos Aires working a very dangerous
            scheme when Jess -- now an accomplished femme fatale -- unexpectedly
            shows up. Her appearance throws Nicky for a loop at a time when he
            cannot afford to be off his game.
             ''',
  'poster_image_url': 'http://ia.media-imdb.com/images/M/MV5BMTUwODg2OTA4OF5BMl5BanBnXkFtZTgwOTE5MTE4MzE@._V1_SX214_AL_.jpg'
  }
  movieThree = {
  'mtitle': 'Insurgent',
  'trailer_youtube_id': 'UtgPdoxU-SY',
  'summary': '''
                Now on the run from Jeanine (Kate Winslet) and the rest of the
                power-hungry Erudites, Tris (Shailene Woodley) and Four (Theo James)
                search for allies and answers in the ruins of Chicago.
                They must find out what Tris' family sacrificed their lives to protect
                and why the Erudites will do anything to stop them. Side by side,
                Tris and Four face one seemingly insurmountable challenge
                after another, as they unravel the secrets of the past and
                -- ultimately -- the future of their world.
             ''',
  'poster_image_url': 'http://ia.media-imdb.com/images/M/MV5BMTgxOTYxMTg3OF5BMl5BanBnXkFtZTgwMDgyMzA2NDE@._V1_SX214_AL_.jpg'
  }
  movie_titles = [movieOne, movieTwo, movieThree]


  return render_template("tomatoes.html",movie_title=movie_titles)







if __name__ == '__main__':
  port = 5000 + random.randint(0, 999)
  url = "http://127.0.0.1:{0}".format(port)
  threading.Timer(1.25, lambda: webbrowser.open(url) ).start()
  app.run(port=port, debug=True)


for x in movie:
  print x['mtitle']
  print x['trailer_youtube_id']
  print x['summary']
  print x['poster_image_url']
