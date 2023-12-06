# Tests for your routes go here

# # === Example Code Below ===

# """
# GET /emoji
# """
# def test_get_emoji(web_client):
#     response = web_client.get("/emoji")
#     assert response.status_code == 200
#     assert response.data.decode("utf-8") == ":)"

# # === End Example Code ===

# Scenario 1

    # POST /albums
    #  title: 'The Seldom Seen Kid'
    #  release_year: '2008' 
    #  artist_id: '1' 
    #  Expected response (200 OK):
""" # (no content)
"""

    # GET /albums
    #  Expected response (200 OK):
"""
    Album(1, Asleep in the Back, 2001, 1)
    Album(2, The Balcony, 2014, 2)
    Album(3, Nothing But Thieves, 2015, 3)
    Album(4, Cast of Thousands, 2003, 1)
    Album(5, The Ride, 2016, 2)
    Album(6, Moral Panic, 2020, 3)
    Album(7, Leaders of the Free World, 2005, 1)
    Album(8, The Seldom Seen Kid, 2008, 1)
"""

"""
When I call POST /albums with album info
I see that album reflected in the list
"""
def test_post_albums(db_connection, web_client):
    db_connection.seed("seeds/albums_table.sql")
    post_response = web_client.post(
        "/albums", data={
            'title': 'The Seldom Seen Kid',
            'release_year': '2008',
            'artist_id': '1'
        }
    )
    assert post_response.status_code == 200
    assert post_response.data.decode("utf-8") == ""

    get_response = web_client.get("/albums")
    assert get_response.status_code == 200
    assert get_response.data.decode("utf-8") == \
        "Album(1, Asleep in the Back, 2001, 1)\n" + \
        "Album(2, The Balcony, 2014, 2)\n" + \
        "Album(3, Nothing But Thieves, 2015, 3)\n" + \
        "Album(4, Cast of Thousands, 2003, 1)\n" + \
        "Album(5, The Ride, 2016, 2)\n" + \
        "Album(6, Moral Panic, 2020, 3)\n" + \
        "Album(7, Leaders of the Free World, 2005, 1)\n" + \
        "Album(8, The Seldom Seen Kid, 2008, 1)"

# Scenario 2

    # POST /albums
    #  title:
    #  release_year:
    #  artist_id:
    #  Expected response (400 Bad Request):
    """
    Please provide a title, release_year and artist_id
    """

    # GET /albums
    #  Expected response (200 OK):
    """
    Album(1, Asleep in the Back, 2001, 1)
    Album(2, The Balcony, 2014, 2)
    Album(3, Nothing But Thieves, 2015, 3)
    Album(4, Cast of Thousands, 2003, 1)
    Album(5, The Ride, 2016, 2)
    Album(6, Moral Panic, 2020, 3)
    Album(7, Leaders of the Free World, 2005, 1)
    """








# Scenario 1

    # GET /artists
    #  Expected response (200 OK):
    """
    Artist(1, Elbow, Indie)
    Artist(2, Catfish and the Bottlemen, Alternative)
    Artist(3, Nothing But Thieves, Alt-Rock)
    """

"""
GET /artists
  Expected response (200 OK):
  Artist(1, Elbow, Indie)
  Artist(2, Catfish and the Bottlemen, Alternative)
  Artist(3, Nothing But Thieves, Alt-Rock)
"""
def test_get_artists(db_connection, web_client):
    db_connection.seed("seeds/artists_table.sql")
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == \
        "Artist(1, Elbow, Indie)\n" + \
        "Artist(2, Catfish and the Bottlemen, Alternative)\n" + \
        "Artist(3, Nothing But Thieves, Alt-Rock)"

# Scenario 2

    # POST /artists
    #  name: 'YONAKA'
    #  genre: 'Alt-Rock' 
    #  Expected response (200 OK):
    """ # (no content)
    """

    # GET /artists
    #  Expected response (200 OK):
    """
    Artist(1, Elbow, Indie)
    Artist(2, Catfish and the Bottlemen, Alternative)
    Artist(3, Nothing But Thieves, Alt-Rock)
    Artist(4, YONAKA, Alt-Rock)
    """

"""
POST /artists
  Parameters:
    name: YONAKA
    genre: Alt-Rock
  Expected response (200 OK):
  ""
"""
def test_post_artists(db_connection, web_client):
    db_connection.seed("seeds/artists_table.sql")
    post_response = web_client.post('/artists', data={'name': 'YONAKA', 'genre': 'Alt-Rock'})
    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == ''

    get_response = web_client.get('/artists')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == \
        "Artist(1, Elbow, Indie)\n" + \
        "Artist(2, Catfish and the Bottlemen, Alternative)\n" + \
        "Artist(3, Nothing But Thieves, Alt-Rock)\n" + \
        "Artist(4, YONAKA, Alt-Rock)"


# Scenario 3

    # POST /artists
    #  name:
    #  genre:
    #  Expected response (400 Bad Request):
    """
    Please provide a name and genre
    """

    # GET /artists
    #  Expected response (200 OK):
    """
    Artist(1, Elbow, Indie)
    Artist(2, Catfish and the Bottlemen, Alternative)
    Artist(3, Nothing But Thieves, Alt-Rock)
    """

"""
POST /artists
  Parameters:
    None
  Expected response (400 Bad Request):
  ""
"""
def test_post_artists_bad_request(db_connection, web_client):
    db_connection.seed("seeds/artists_table.sql")
    post_response = web_client.post('/artists', data={})
    assert post_response.status_code == 400

    get_response = web_client.get('/artists')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == \
        "Artist(1, Elbow, Indie)\n" + \
        "Artist(2, Catfish and the Bottlemen, Alternative)\n" + \
        "Artist(3, Nothing But Thieves, Alt-Rock)"