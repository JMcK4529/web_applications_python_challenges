# Albums: Route Design Recipe

_Copy this design recipe template to test-drive a plain-text Flask route._

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
GET /artists

POST /artists
  name: string
  genre: string
```

## 2. Create Examples as Tests

```python
# Scenario 1

    # GET /artists
    #  Expected response (200 OK):
    """
    Artist(1, Elbow, Indie)
    Artist(2, Catfish and the Bottlemen, Alternative)
    Artist(3, Nothing But Thieves, Alt-Rock)
    """

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
```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
"""
GET /artists
  Expected response (200 OK):
  Artist(1, Elbow, Indie)
  Artist(2, Catfish and the Bottlemen, Alternative)
  Artist(3, Nothing But Thieves, Alt-Rock)
"""
def test_get_artists(web_client):
    response = web_client.get('/artists')
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
def test_post_artists(web_client):
    post_response = web_client.post('/artists', data={'name': 'YONAKA', 'genre': 'Alt-Rock'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == ''

    get_response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == \
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
def test_post_artists_bad_request(web_client):
    post_response = web_client.post('/artists', data={})
    assert response.status_code == 400
    assert response.data.decode('utf-8') == ''

    get_response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == \
        "Artist(1, Elbow, Indie)\n" + \
        "Artist(2, Catfish and the Bottlemen, Alternative)\n" + \
        "Artist(3, Nothing But Thieves, Alt-Rock)"

```
