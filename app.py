from flask import Flask
from flask import send_file

app = Flask(__name__)

@app.get("/animations/<slug>")
def animation(slug):
    filename = f'output/{slug}.mp4'
    return send_file(filename, mimetype='image/mp4')

@app.get("/thumbnails/<slug>")
def thumbnail(slug):
    filename = f'output/{slug}.png'
    return send_file(filename, mimetype='image/png')

if __name__ == "__main__":
    app.run()