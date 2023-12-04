import os
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

@app.route('/albums', methods=['POST'])
def post_albums():
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
    albums_string_list = []
    for album in albums:
        albums_string_list.append(str(album))
    return "\n".join(albums_string_list)


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

