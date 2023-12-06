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
def test_get_artists_list(db_connection, web_client, test_web_address):
    db_connection.seed("seeds/artists_table.sql")
    response = web_client.get(f'http://{test_web_address}/artists_list')
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
def test_post_artists_list(db_connection, web_client, test_web_address):
    db_connection.seed("seeds/artists_table.sql")
    post_response = web_client.post(f'http://{test_web_address}/artists_list', data={'name': 'YONAKA', 'genre': 'Alt-Rock'})
    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == ''

    get_response = web_client.get(f'http://{test_web_address}/artists_list')
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
def test_post_artists_list_bad_request(db_connection, web_client, test_web_address):
    db_connection.seed("seeds/artists_table.sql")
    post_response = web_client.post(f'http://{test_web_address}/artists_list', data={})
    assert post_response.status_code == 400

    get_response = web_client.get(f'http://{test_web_address}/artists_list')
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
def test_get_albums(db_connection, page, test_web_address):
    db_connection.seed("seeds/albums_table.sql")
    page.goto(f"http://{test_web_address}/albums")
    div_tags_locator = page.locator("div")
    div_tags_list = page.locator("div").all()
    expected_text_list = [
        "Title: Asleep in the Back\nReleased: 2001",
        "Title: The Balcony\nReleased: 2014",
        "Title: Nothing But Thieves\nReleased: 2015",
        "Title: Cast of Thousands\nReleased: 2003",
        "Title: The Ride\nReleased: 2016",
        "Title: Moral Panic\nReleased: 2020",
        "Title: Leaders of the Free World\nReleased: 2005"
    ]
    assert len(div_tags_list) > 0
    for div, text in zip(div_tags_list, expected_text_list):
        expect(div).to_have_text(text)

# Dynamic Templates: Challenge
"""
When I call GET /albums/<album_id>
I get a HTML response which shows the release year and the artist
for the album with id "album_id"
"""
def test_get_album(db_connection, page, test_web_address):
    db_connection.seed("seeds/albums_table.sql")
    expected_h1_list = [
        "Asleep in the Back",
        "The Balcony",
        "Nothing But Thieves"
    ]
    expected_p_list = [
        "Release Year: 2001\nArtist: Elbow",
        "Release Year: 2014\nArtist: Catfish and the Bottlemen",
        "Release Year: 2015\nArtist: Nothing But Thieves"
    ]
    for num in range(1,4):
        page.goto(f"http://{test_web_address}/album/{num}")
        h1_loc = page.locator("h1")
        expect(h1_loc).to_have_text(
            expected_h1_list[num-1]
        )
        p_loc = page.locator("p")
        expect(p_loc).to_have_text(
            expected_p_list[num-1]
        )
    
# Using Links: Exercise
def test_get_albums_has_links(db_connection, page, test_web_address):
    db_connection.seed("seeds/albums_table.sql")
    page.goto(f"http://{test_web_address}/albums")
    a_list = page.locator("a")
    a_list = a_list.all()
    for a, num in zip(a_list, range(1,len(a_list)+1)):
        a.dblclick()
        expect(page).to_have_url(f"http://{test_web_address}/album/{num}")
        page.goto(f"http://{test_web_address}/albums")

# Using Links: Challenge
def test_get_artist_by_id(db_connection, page, test_web_address):
    db_connection.seed("seeds/artists_table.sql")
    expected_title_list = [
        "Artist Info: Elbow",
        "Artist Info: Catfish and the Bottlemen",
        "Artist Info: Nothing But Thieves"
    ]
    expected_h1_list = [
        "Elbow",
        "Catfish and the Bottlemen",
        "Nothing But Thieves"
    ]
    expected_p_list = [
        "Genre: Indie",
        "Genre: Alternative",
        "Genre: Alt-Rock"
    ]

    for num in range(1,4):
        page.goto(f"http://{test_web_address}/artists/{num}")
        title = page.locator("title")
        assert title.inner_text().strip() == expected_title_list[num - 1]
        # expect(title).to_have_text(expected_title_list[num - 1]) # Why doesn't this work??
        h1 = page.locator("h1")
        expect(h1).to_have_text(expected_h1_list[num - 1])
        p = page.locator("p")
        expect(p).to_have_text(expected_p_list[num - 1])

def test_get_artists(db_connection, page, test_web_address):
    db_connection.seed("seeds/artists_table.sql")
    page.goto(f"http://{test_web_address}/artists")
    title = page.locator("title")
    assert title.inner_text().strip() == "Artists with links"
    h1 = page.locator("h1")
    expect(h1).to_have_text("Artists")

    expected_divs = [
        "Name: Elbow\nGenre: Indie",
        "Name: Catfish and the Bottlemen\nGenre: Alternative",
        "Name: Nothing But Thieves\nGenre: Alt-Rock"
    ]
    divs = page.locator("div")
    divs_list = divs.all()
    for div, text in zip(divs_list, expected_divs):
        expect(div).to_have_text(text)

    a_tags = page.locator("a")
    a_tags_list = a_tags.all()
    for a, num in zip(a_tags_list, range(1, 4)):
        a.dblclick()
        expect(page).to_have_url(f"http://{test_web_address}/artists/{num}")
        page.goto(f"http://{test_web_address}/artists")
