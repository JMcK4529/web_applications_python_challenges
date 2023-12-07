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

def test_is_valid():
    for empty in [None, ""]:
        artist1 = Artist(1, "YONAKA", "Alt-Rock")
        artist2 = Artist(1, empty, "Alt-Rock")
        artist3 = Artist(1, "YONAKA", empty)
        artist4 = Artist(1, empty, empty)

        assert artist1.is_valid()
        for artist in [artist2, artist3, artist4]:
            assert artist.is_valid() == False

def test_generate_errors():
    for empty in [None, ""]:
        artist1 = Artist(1, "YONAKA", "Alt-Rock")
        artist2 = Artist(1, empty, "Alt-Rock")
        artist3 = Artist(1, "YONAKA", empty)
        artist4 = Artist(1, empty, empty)

    assert artist1.generate_errors() == None
    assert artist2.generate_errors() == "Name can't be empty."
    assert artist3.generate_errors() == "Genre can't be empty."
    assert artist4.generate_errors() == "Name can't be empty. Genre can't be empty."
    