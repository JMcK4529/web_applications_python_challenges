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
    #  title: 'The Seldom Seen Kid'
    #  release_year: '2008' 
    #  artist_id: '1' 
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