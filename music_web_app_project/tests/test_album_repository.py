from lib.album_repository import AlbumRepository
from lib.album import Album

"""
AlbumRepository.all returns all the albums (and all columns) from
the database
"""
def test_all_records_retrieved_by_all_method(db_connection):
    db_connection.seed("seeds/albums_table.sql")
    repository = AlbumRepository(db_connection)

    albums = repository.all()

    assert albums == [
        Album(1, 'Asleep in the Back', 2001, 1),
        Album(2, 'The Balcony', 2014, 2),
        Album(3, 'Nothing But Thieves', 2015, 3),
        Album(4, 'Cast of Thousands', 2003, 1),
        Album(5, 'The Ride', 2016, 2),
        Album(6, 'Moral Panic', 2020, 3),
        Album(7, 'Leaders of the Free World', 2005, 1)
    ]

"""
AlbumRepository.find(n) returns the Album whose id == n
"""
def test_single_record_with_correct_id_retrieved_by_find(db_connection):
    db_connection.seed("seeds/albums_table.sql")
    repository = AlbumRepository(db_connection)
    album = repository.find(6)
    assert album == Album(6, 'Moral Panic', 2020, 3)

"""
AlbumRepository.create(album) insert the album into the albums table
"""
def test_create_inserts_one_album_into_albums_table(db_connection):
    db_connection.seed("seeds/albums_table.sql")
    repository = AlbumRepository(db_connection)
    album = Album(None, 'Love Story', 2010, 4)
    assert repository.create(album) == None
    assert repository.all() == [
        Album(1, 'Asleep in the Back', 2001, 1),
        Album(2, 'The Balcony', 2014, 2),
        Album(3, 'Nothing But Thieves', 2015, 3),
        Album(4, 'Cast of Thousands', 2003, 1),
        Album(5, 'The Ride', 2016, 2),
        Album(6, 'Moral Panic', 2020, 3),
        Album(7, 'Leaders of the Free World', 2005, 1),
        Album(8, 'Love Story', 2010, 4)
    ]

"""
AlbumRepository.delete(album_id) deletes the album corresponding to
album_id from the albums table
"""
def test_delete_removes_specified_album_from_albums_table(db_connection):
    db_connection.seed("seeds/albums_table.sql")
    repository = AlbumRepository(db_connection)
    assert repository.delete(5) == None
    assert repository.all() == [
        Album(1, 'Asleep in the Back', 2001, 1),
        Album(2, 'The Balcony', 2014, 2),
        Album(3, 'Nothing But Thieves', 2015, 3),
        Album(4, 'Cast of Thousands', 2003, 1),
        Album(6, 'Moral Panic', 2020, 3),
        Album(7, 'Leaders of the Free World', 2005, 1)
    ]