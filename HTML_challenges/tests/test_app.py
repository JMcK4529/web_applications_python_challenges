from playwright.sync_api import Page, expect

# Tests for your routes go here

# === Example Code Below ===

"""
We can get an emoji from the /emoji page
"""
def test_get_emoji(page, test_web_address): # Note new parameters
    # We load a virtual browser and navigate to the /emoji page
    page.goto(f"http://{test_web_address}/emoji")

    # We look at the <strong> tag
    strong_tag = page.locator("strong")

    # We assert that it has the text ":)"
    expect(strong_tag).to_have_text(":)")

# === End Example Code ===

# Page Structure: Exercise 2
def test_get_goodbye(page, test_web_address):
    page.goto(f"http://{test_web_address}/goodbye")
    strong_tag = page.locator("strong")
    expect(strong_tag).to_have_text("Bye, user!")

# Dynamic Templates: Exercise

"""
GET /artists
  Expected response (200 OK):
  Artist(1, Elbow, Indie)
  Artist(2, Catfish and the Bottlemen, Alternative)
  Artist(3, Nothing But Thieves, Alt-Rock)
"""
def test_get_artists(db_connection, web_client, test_web_address):
    db_connection.seed("seeds/artists_table.sql")
    response = web_client.get(f'http://{test_web_address}/artists')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == \
        "Artist(1, Elbow, Indie)\n" + \
        "Artist(2, Catfish and the Bottlemen, Alternative)\n" + \
        "Artist(3, Nothing But Thieves, Alt-Rock)"

"""
POST /artists
  Parameters:
    name: YONAKA
    genre: Alt-Rock
  Expected response (200 OK):
  ""
"""
def test_post_artists(db_connection, web_client, test_web_address):
    db_connection.seed("seeds/artists_table.sql")
    post_response = web_client.post(f'http://{test_web_address}/artists', data={'name': 'YONAKA', 'genre': 'Alt-Rock'})
    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == ''

    get_response = web_client.get(f'http://{test_web_address}/artists')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == \
        "Artist(1, Elbow, Indie)\n" + \
        "Artist(2, Catfish and the Bottlemen, Alternative)\n" + \
        "Artist(3, Nothing But Thieves, Alt-Rock)\n" + \
        "Artist(4, YONAKA, Alt-Rock)"
    
"""
POST /artists
  Parameters:
    None
  Expected response (400 Bad Request):
  ""
"""
def test_post_artists_bad_request(db_connection, web_client, test_web_address):
    db_connection.seed("seeds/artists_table.sql")
    post_response = web_client.post(f'http://{test_web_address}/artists', data={})
    assert post_response.status_code == 400

    get_response = web_client.get(f'http://{test_web_address}/artists')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == \
        "Artist(1, Elbow, Indie)\n" + \
        "Artist(2, Catfish and the Bottlemen, Alternative)\n" + \
        "Artist(3, Nothing But Thieves, Alt-Rock)"
    
"""
When I call POST /albums_list with album info
I see that album reflected in the list
"""
def test_post_albums_list(db_connection, web_client, test_web_address):
    db_connection.seed("seeds/albums_table.sql")
    post_response = web_client.post(
        f"http://{test_web_address}/albums_list", data={
            'title': 'The Seldom Seen Kid',
            'release_year': '2008',
            'artist_id': '1'
        }
    )
    assert post_response.status_code == 200
    assert post_response.data.decode("utf-8") == ""

    get_response = web_client.get(f"http://{test_web_address}/albums_list")
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

"""
When I call GET /albums
I get a HTML response which shows some Titles and Release Years
"""
def test_get_albums(db_connection, web_client, page, test_web_address):
    page.goto(f"http://{test_web_address}/goodbye")
    div_tags_locator = page.locator("div")
    div_tags_list = div_tags_locator.all()
    expected_text_list = [
        "Title: Asleep in the Back\nReleased: 2001",
        "Title: The Balcony\nReleased: 2014",
        "Title: Nothing But Thieves\nReleased: 2015",
        "Title: Cast of Thousands\nReleased: 2003",
        "Title: The Ride\nReleased: 2016",
        "Title: Moral Panic\nReleased: 2020",
        "Title: Leaders of the Free World\nReleased: 2005"
    ]
    for div, text in zip(div_tags_list, expected_text_list):
        expect(div).to_have_text(text)