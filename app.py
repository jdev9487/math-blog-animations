from flask import Flask
from flask import send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.get("/animations/<slug>")
def animation(slug):
    filename = f'output/{slug}.mp4'
    return send_file(filename, mimetype='image/mp4')

@app.get("/thumbnails/<slug>")
def thumbnail(slug):
    filename = f'output/{slug}.png'
    return send_file(filename, mimetype='image/png')