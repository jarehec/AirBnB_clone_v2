#!/usr/bin/python3
"""
"""


from web_flask import app


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    return "HBNB"


if __name__ == '__main__':
    app.run()
