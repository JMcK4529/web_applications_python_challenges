import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist_repository import ArtistRepository
from lib.artist import Artist

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==


# == Example Code Below ==

# GET /emoji
# Returns a smiley face in HTML
# Try it:
#   ; open http://localhost:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    # We use `render_template` to send the user the file `emoji.html`
    # But first, it gets processed to look for placeholders like {{ emoji }}
    # These placeholders are replaced with the values we pass in as arguments
    return render_template('emoji.html', emoji=':)')

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# Page Structure: Exercise 2
@app.route('/goodbye', methods=['GET'])
def get_goodbye():
    try:
        name = request.args['name']
    except:
        name = "user"
    return render_template('farewell.html', name=name)

# Dynamic Templates
@app.route('/artists', methods=['GET'])
def get_artists():
    connection = get_flask_database_connection(app)
    artist_repo = ArtistRepository(connection)
    artists = artist_repo.all()
    return "\n".join([str(artist) for artist in artists])

@app.route('/artists', methods=['POST'])
def post_artists():
    connection = get_flask_database_connection(app)
    artist_repo = ArtistRepository(connection)
    new_artist_info = request.form['name'], request.form['genre']
    artist_repo.create(Artist(None, new_artist_info[0], new_artist_info[1]))
    return ''

@app.route('/albums_list', methods=['GET'])
def get_albums_list():
    connection = get_flask_database_connection(app)
    album_repo = AlbumRepository(connection)
    albums = album_repo.all()
    albums_string_list = []
    for album in albums:
        albums_string_list.append(str(album))
    return "\n".join(albums_string_list)

@app.route('/albums_list', methods=['POST'])
def post_albums_list():
    connection = get_flask_database_connection(app)
    album_repo = AlbumRepository(connection)
    album_info = request.form['title'], request.form['release_year'], request.form['artist_id']
    new_album = Album(None, album_info[0], album_info[1], album_info[2])
    album_repo.create(new_album)
    return ''

@app.route('/albums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    album_repo = AlbumRepository(connection)
    albums = album_repo.all()

    return render_template('albums.html', albums=albums)

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
