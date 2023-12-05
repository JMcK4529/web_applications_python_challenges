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