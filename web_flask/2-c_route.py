#!/usr/bin/python3
"""
"""


from web_flask import app


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_isfun(text):
    return "C {}".format(text.replace("_", " "))


if __name__ == '__main__':
    app.run()