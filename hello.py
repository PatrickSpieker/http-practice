from flask import Flask
import flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/memes")
def hello_world_2():
    resp = flask.make_response({"testing": 5})
    resp.headers['Content-Type'] = 'application/json'
    return resp
