# Sort Names - Route Design Recipe

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
# Sort Names route
POST /sort-names
  names: Joe,Alice,Zoe,Julia,Kieran

# Expected response (sorted list of names):
Alice,Joe,Julia,Kieran,Zoe
```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python
# POST /sort-names
#  Parameters:
#    names: 
#  Expected response (200 OK):
"""
No names were provided.
"""

# POST /sort-names
#  Parameters:
#    names: Bob,Alice
#  Expected response (200 OK):
"""
Alice,Bob
"""

# POST /sort-names
#  Parameters:
#    names: Joe,Alice,Zoe,Julia,Kieran
#  Expected response (200 OK):
"""
Alice,Joe,Julia,Kieran,Zoe
"""

# POST /sort-names
#  Parameters:
#    names: JoeAliceZoeJuliaKieran
#  Expected response (200 OK):
"""
JoeAliceZoeJuliaKieran
"""

# POST /sort-names
#  Parameters:
#    names: Joe,1,Alice,4,Zoe,Bob
#  Expected response (200 OK):
"""
Non-alpha names were removed.
Alice,Bob,Joe,Zoe
"""

# POST /sort-names
#  Parameters:
#    names: 5,3,2,1,4
#  Expected response (200 OK):
"""
Non-alpha names were removed.
No names were provided.
"""
```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
"""
POST /sort-names
  Parameters:
    names: ''
  Expected response (200 OK):
  "No names were provided."
"""
def test_post_empty_to_sort_names(web_client):
    response = web_client.post('/sort-names', data={'names': ''})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'No names were provided.'

"""
POST /sort-names
  Parameters:
    names: 'Alice'
  Expected response (200 OK):
  "Alice"
"""
def test_post_one_name_to_sort_names(web_client):
    response = web_client.post('/sort-names', data={'names': 'Alice'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice'

"""
POST /sort-names
  Parameters:
    names: 'Bob,Alice'
  Expected response (200 OK):
  "Alice,Bob"
"""
def test_post_two_names_to_sort_names(web_client):
    response = web_client.post('/sort-names', data={'names': 'Bob,Alice'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice,Bob'

"""
POST /sort-names
  Parameters:
    names: 'Joe,Alice,Zoe,Julia,Kieran'
  Expected response (200 OK):
  "Alice,Joe,Julia,Kieran,Zoe"
"""
def test_post_many_names_to_sort_names(web_client):
    response = web_client.post('/sort-names', data={'names': 'Joe,Alice,Zoe,Julia,Kieran'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice,Joe,Julia,Kieran,Zoe'

"""
POST /sort-names
  Parameters:
    names: '5,3,1,4,2'
  Expected response (200 OK):
  "Non-alpha names were removed.\nNo names were provided."
"""
def test_post_non_alpha_to_sort_names(web_client):
    response = web_client.post('/sort-names', data={'names': '5,3,1,4,2'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Non-alpha names were removed.\nNo names were provided.'

"""
POST /sort-names
  Parameters:
    names: 'Zoe,Alice,1,Joe,Michelle'
  Expected response (200 OK):
  "Non-alpha names were removed.\nAlice,Joe,Michelle,Zoe"
"""
def test_post_mixed_alpha_non_alpha_to_sort_names(web_client):
    response = web_client.post('/sort-names', data={'names': 'Zoe,Alice,1,Joe,Michelle'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Non-alpha names were removed.\nAlice,Joe,Michelle,Zoe'
```
