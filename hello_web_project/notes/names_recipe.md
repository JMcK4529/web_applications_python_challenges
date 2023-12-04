# {{ NAME }} Route Design Recipe

_Copy this design recipe template to test-drive a plain-text Flask route._

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
# This route should return a list of pre-defined names, plus the name given.

# Expected response (2OO OK):
Julia, Alice, Karim, Eddie


# names route
GET /names?add=<string>
```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python
# GET /names?add=Eddie
#  Expected response (200 OK):
"""
Alice, Eddie, Julia, Karim
"""

# GET /names
#  Expected response (400 Bad Request):
"""
"""
```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
"""
GET /names?add=Eddie
  Expected response (200 OK):
  "Alice, Eddie, Julia, Karim"
"""
def test_get_names_with_Eddie(web_client):
    response = web_client.get('/names?add=Eddie')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice, Eddie, Julia, Karim'

"""
GET /names
  Expected response (400 Bad Response):
"""
def test_get_names_empty(web_client):
    response = web_client.get('/names')
    assert response.status_code == 400
```
