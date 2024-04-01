class Song:
    count = 0
    # genres = list()
    genre_count = dict()
    # artists = list()
    artist_count = dict()

    def __init__(self, name, artist, genre):
        self.add_song_to_count()
        # self.add_genres(artist)
        self.add_to_genre_count(artist)
        # self.add_to_artists(genre)
        self.add_to_artist_count(genre)


    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.count += increment


    # @classmethod
    # def add_genres(cls, genre):
    #     if genre not in cls.genres:
    #         cls.genres.append(genre)
    #     else:
    #         return

    # @classmethod
    # def add_to_artists(cls, artist):
    #     if artist not in cls.artists:
    #         cls.artists.append(artist)
    #     else:
    #         return
        
    @classmethod
    def add_to_genre_count(cls):
        for genre in cls.genre_count:
           cls.genre_count[genre] = cls.genre_count.get(genre,0) + 1 

    @classmethod
    def add_to_artist_count(cls):
        for artist in cls.artist_count:
           cls.artist_count[artist ] = cls.artist_count.get(artist ,0) + 1 
