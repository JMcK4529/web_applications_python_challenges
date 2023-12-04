# Albums: Route Design Recipe

_Copy this design recipe template to test-drive a plain-text Flask route._

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
POST /albums
  title: string
  release_year: number (string)
  artist_id: number (string)

GET /albums

```

## 2. Create Examples as Tests

```python
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
```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
"""
GET /home
  Expected response (200 OK):
  "This is my home page!"
"""
def test_get_home(web_client):
    response = web_client.get('/home')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'This is my home page!'

"""
POST /submit
  Parameters:
    name: Leo
    message: Hello world
  Expected response (200 OK):
  "Thanks Leo, you sent this message: "Hello world""
"""
def test_post_submit(web_client):
    response = web_client.post('/submit', data={'name': 'Leo', 'message': 'Hello world'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Thanks Leo, you sent this message: "Hello world"'
```
