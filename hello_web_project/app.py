import os
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

# Building a route Exercise
@app.route('/submit', methods=['POST'])
def post_name_and_message():
    name = request.form['name']
    message = request.form['message']
    return f"Thanks {name}, you sent this message: \"{message}\""

# Building a route: Challenge
@app.route('/wave', methods=['GET'])
def wave_at_name():
    name = request.args['name']
    return f"I am waving at {name}"

# Test driving a route: Exercise 1
@app.route('/count_vowels', methods=['POST'])
def count_vowels():
    text = request.form['text']
    vowel_count = 0
    for character in text:
        if character in ['a', 'e', 'i', 'o', 'u']:
            vowel_count += 1
    return f"There are {vowel_count} vowels in \"{text}\""

# Test driving a route: Exercise 2
@app.route('/sort-names', methods=['POST'])
def sort_names():
    names = request.form['names']
    if len(names) == 0:
        return "No names were provided."
    names_list = names.split(",")
    alpha_list = []
    for i in range(len(names_list)):
        if names_list[i].isalpha():
            alpha_list.append(names_list[i])

    if len(alpha_list) != len(names_list):
        prepend = "Non-alpha names were removed.\n"
    else:
        prepend = ""
    if len(alpha_list) == 0:
        output = "No names were provided."
    else:
        alpha_list.sort()
        output = ",".join(alpha_list)
    return prepend + output

# Test driving a route: Challenge
@app.route('/names', methods=['GET'])
def names():
    names = ['Alice', 'Julia', 'Karim']
    add = request.args['add']

    if not add.isalpha():
        return "Added name is non-alpha."

    names.append(add)
    names.sort()
    return ", ".join(names)


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

