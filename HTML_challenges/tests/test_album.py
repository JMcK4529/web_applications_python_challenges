from lib.album import Album

"""
Album construsts with an id, title, release_year and artist_id
"""
def test_album_constructs():
    album = Album(1, "Test Title", 1000, 5)
    assert album.id == 1
    assert album.title == "Test Title"
    assert album.release_year == 1000
    assert album.artist_id == 5

"""
Albums are formatted to strings in a readable way
"""
def test_album_to_string():
    album = Album(1, "Test Title", 1000, 5)
    assert str(album) == "Album(1, Test Title, 1000, 5)"

"""
Comparing two instances of Album with the same data should
result in them being equal
"""
def test_album_equality():
    album1 = Album(1, "Test Title", 1000, 5)
    album2 = Album(1, "Test Title", 1000, 5)
    assert album1 == album2

"""
Album#is_valid() returns True if title, release_year and artist_id are valid
Else it returns False
"""
def test_album_is_valid():
    album1 = Album(None, None, "2008", "1")
    album2 = Album(None, "The Seldom Seen Kid", None, "1")
    album3 = Album(None, "The Seldom Seen Kid", "2008", None)
    album4 = Album(None, "The Seldom Seen Kid", "2008", "1")

    for album in [album1, album2, album3]:
        assert album.is_valid() == False
    assert album4.is_valid()

"""
Album#generate_errors() returns an error string
If #is_valid() returns False
"""
def test_album_generate_errors(db_connection):
    db_connection.seed("seeds/artists_table.sql")
    album1 = Album(None, None, "2008", "1")
    album2 = Album(None, "The Seldom Seen Kid", None, "1")
    album3 = Album(None, "The Seldom Seen Kid", "2008", None)

    album1.generate_errors() == "Title can't be blank."
    album2.generate_errors() == "Release year can't be blank."
    album3.generate_errors() == "Artist ID can't be blank."