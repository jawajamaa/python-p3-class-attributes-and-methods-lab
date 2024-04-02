class Song:
    count = 0
    genres = list()
    genre_count = dict()
    artists = list()
    artist_count = dict()

    def __init__(self, name, artist, genre):
        self.add_song_to_count(name, artist, genre)
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_to_genres(genre)
        self.add_to_genre_count(genre)
        self.add_to_artists(artist)
        self.add_to_artist_count(artist)


    @classmethod
    def add_song_to_count(cls, name, artist, genre, increment=1):
        cls.count += increment
        cls.name = name
        cls.artist = artist
        cls.genre = genre


    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
        else:
            return

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)
        else:
            return
        
    @classmethod
    def add_to_genre_count(cls, genre):
        for genny in cls.genre_count:
           cls.genre_count[genny] = cls.genre_count.get(genre,0) + 1 
        breakpoint()
        print(cls.genre_count["Rap"])

    @classmethod
    def add_to_artist_count(cls, artist):
        for artist in cls.artist_count:
           cls.artist_count[artist ] = cls.artist_count.get(artist ,0) + 1
        print(cls.artist_count["Jay Z"]) 

song = Song("99 Problems", "Jay Z", "Rap")
