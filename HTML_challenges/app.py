import os
from flask import Flask, request, render_template, redirect
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
@app.route('/artists_list', methods=['GET'])
def get_artists_list():
    connection = get_flask_database_connection(app)
    artist_repo = ArtistRepository(connection)
    artists = artist_repo.all()
    return "\n".join([str(artist) for artist in artists])

@app.route('/artists_list', methods=['POST'])
def post_artists_list():
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

@app.route('/album/<int:album_id>', methods=['GET'])
def get_album(album_id):
    connection = get_flask_database_connection(app)
    album_repo = AlbumRepository(connection)
    album = album_repo.find(album_id)
    artist_repo = ArtistRepository(connection)
    artist = artist_repo.find(album.artist_id)
    return render_template('single_album.html', album=album, artist=artist)

@app.route('/artists/<int:artist_id>', methods=['GET'])
def get_artist(artist_id):
    connection = get_flask_database_connection(app)
    artist_repo = ArtistRepository(connection)
    artist = artist_repo.find(artist_id)
    return render_template('single_artist.html', artist=artist)

@app.route('/artists', methods=['GET'])
def get_artists():
    connection = get_flask_database_connection(app)
    artist_repo = ArtistRepository(connection)
    artists = artist_repo.all()
    return render_template('artists.html', artists=artists)

@app.route('/albums/new', methods=['GET'])
def get_albums_new():
    return render_template('albums_form.html')

@app.route('/albums/new', methods=['POST'])
def create_new_album():
    connection = get_flask_database_connection(app)
    album_repo = AlbumRepository(connection)
    new_album = Album(None, request.form['title'], 
                      request.form['release_year'],
                      request.form['artist_id'])
    if not new_album.is_valid():
        return render_template('albums_form.html', 
                               errors=new_album.generate_errors()), 400
    else:
        album_repo.create(new_album)

        album_id = album_repo.all()[-1].id
        return redirect(f"/album/{album_id}")

@app.route('/artists/new', methods=['GET'])
def get_artists_new():
    return render_template('artists_form.html')

@app.route('/artists/new', methods=['POST'])
def create_new_artist():
    connection = get_flask_database_connection(app)
    artist_repo = ArtistRepository(connection)
    new_artist = Artist(None, request.form['name'], request.form['genre'])
    if not new_artist.is_valid():
        return render_template('artists_form.html', 
                               errors=new_artist.generate_errors()), 400
    
    artist_repo.create(new_artist)
    id = artist_repo.all()[-1].id
    return redirect(f'/artists/{id}')

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
