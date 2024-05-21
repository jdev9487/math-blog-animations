from flask import Flask
from flask import send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.get("/animations/<slug>")
def animation(slug):
    filename = f'animations/{slug}/media/videos/source/2160p60/Source.mp4'
    return send_file(filename, mimetype='image/mp4')