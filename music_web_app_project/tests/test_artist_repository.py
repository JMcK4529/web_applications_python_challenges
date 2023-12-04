from lib.artist_repository import ArtistRepository
from lib.artist import Artist

def test_repo_all(db_connection):
    db_connection.seed('seeds/artists_table.sql')
    repo = ArtistRepository(db_connection)
    assert repo.all() == [
        Artist(1, "Elbow", "Indie"),
        Artist(2, "Catfish and the Bottlemen", "Alternative"),
        Artist(3, "Nothing But Thieves", "Alt-Rock")
    ]

def test_repo_create(db_connection):
    db_connection.seed('seeds/artists_table.sql')
    repo = ArtistRepository(db_connection)
    new_artist = Artist(None, "YONAKA", "Alt-Rock")
    assert repo.create(new_artist) == None
    assert repo.all() == [
        Artist(1, "Elbow", "Indie"),
        Artist(2, "Catfish and the Bottlemen", "Alternative"),
        Artist(3, "Nothing But Thieves", "Alt-Rock"),
        Artist(4, "YONAKA", "Alt-Rock")
    ]