from lib.artist import Artist

def test_artist_constructs():
    artist = Artist(1, "YONAKA", "Alt-Rock")
    assert artist.id == 1
    assert artist.name == "YONAKA"
    assert artist.genre == "Alt-Rock"

def test_artist_repr():
    artist = Artist(1, "YONAKA", "Alt-Rock")
    assert str(artist) == "Artist(1, YONAKA, Alt-Rock)"

def test_artist_eq():
    artist1 = Artist(1, "YONAKA", "Alt-Rock")
    artist2 = Artist(1, "YONAKA", "Alt-Rock")
    assert artist1 == artist2