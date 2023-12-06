from lib.artist import Artist

class ArtistRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute(
            'SELECT * FROM artists'
        )
        artists = []
        for row in rows:
            artists.append(Artist(row["id"], row["name"], row["genre"]))
        return artists
    
    def create(self, artist):
        self._connection.execute(
            'INSERT INTO artists (name, genre) VALUES (%s, %s)',
            [artist.name, artist.genre]
        )
        return None
    
    def find(self, artist_id):
        row = self._connection.execute(
            "SELECT * FROM artists WHERE id = %s;",
              [artist_id]
              )[0]
        return Artist(row["id"], row["name"], row["genre"])
