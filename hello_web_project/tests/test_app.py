# Tests for your routes go here

# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"

# === End Example Code ===

# Test driving a route: Exercise 1 
"""
When: I make a POST request to /count_vowels
And: I send "eee" as the body parameter text
Then: I should get a 200 response with 3 in the message
"""
def test_post_count_vowels_eee(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eee'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 3 vowels in "eee"'

"""
When: I make a POST request to /count_vowels
And: I send "eunoia" as the body parameter text
Then: I should get a 200 response with 5 in the message
"""
def test_post_count_vowels_eunoia(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eunoia'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 5 vowels in "eunoia"'

"""
When: I make a POST request to /count_vowels
And: I send "mercurial" as the body parameter text
Then: I should get a 200 response with 4 in the message
"""
def test_post_count_vowels_mercurial(web_client):
    response = web_client.post('/count_vowels', data={'text': 'mercurial'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 4 vowels in "mercurial"'

# Test driving a route: Exercise 2
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

# Test driving a route: Challenge
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
GET /names?add=Aaron
  Expected response (200 OK):
  "Aaron, Alice, Julia, Karim"
"""
def test_get_names_with_Aaron(web_client):
    response = web_client.get('/names?add=Aaron')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Aaron, Alice, Julia, Karim'

"""
GET /names?add=123
  Expected response (200 OK):
  "Added name is non-alpha."
"""
def test_get_names_with_Aaron(web_client):
    response = web_client.get('/names?add=123')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Added name is non-alpha.'

"""
GET /names
  Expected response (400 Bad Response):
"""
def test_get_names_empty(web_client):
    response = web_client.get('/names')
    assert response.status_code == 400