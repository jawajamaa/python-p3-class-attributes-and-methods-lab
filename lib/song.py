class Song:
    count = 0
    genres = list()
    genre_count = dict()
    artists = list()
    artist_count = dict()

    def __init__(self, name, artist, genre):
        type(self).add_song_to_count()
        # self.add_song_to_count(name, artist, genre)
        self.name = name
        self.artist = artist
        self.genre = genre
        type(self).add_to_genres(genre)
        # type(self).add_to_genre_count(genre)
        type(self).add_to_artists(artist)
        # Song.add_to_artist_count(artist)
# line 16 is better, but 17 is hard -coding

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1


    # @classmethod
    # def add_song_to_count(cls, name, artist, genre, increment=1):
    #     cls.count += increment
    #     cls.name = name
    #     cls.artist = artist
    #     cls.genre = genre

    @classmethod
    def add_to_genres(cls, genre):
        cls.genre_count[genre] = cls.genre_count.get(genre,0) + 1
        # line 34 added from own cls method that was redundant on line 49
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        cls.artist_count[artist] = cls.artist_count.get(artist ,0) + 1
        # line 41 added from own cls method that was redundant on line 66
        if artist not in cls.artists:
            cls.artists.append(artist)
        # else:  not needed
        #     return not needed; I don't need to return nothing; unnecessary...
        
    # @classmethod
    # def add_to_genre_count(cls, genre):
    #     cls.genre_count[genre] = cls.genre_count.get(genre,0) + 1

        # my more verbose code (with TC help to get it working, but does pass tests)
        # if cls.genre_count == {}:
        #     cls.genre_count[genre] = 1
        # else:
        #     for genny in cls.genre_count:
        #         # breakpoint()
        #         if genre == genny:
        #             cls.genre_count[genny] = cls.genre_count.get(genre,0) + 1 
        #             return
        #     cls.genre_count[genre] = 1
        # print(cls.genre_count["Rap"])

    # @classmethod
    # def add_to_artist_count(cls, artist):
    #     cls.artist_count[artist] = cls.artist_count.get(artist ,0) + 1

# my more verbose code; logic copied from above class method.  1 line above = Pythonic
        # if cls.artist_count == {}:
        #     cls.artist_count[artist] = 1
        # else:
        #     for arty in cls.artist_count:
        #         if artist == arty:
        #             cls.artist_count[arty] = cls.artist_count.get(artist ,0) + 1
        #             return
        #     cls.artist_count[artist] = 1
        # print(cls.artist_count["Jay Z"]) 

# song = Song("99 Problems", "Jay Z", "Rap")
