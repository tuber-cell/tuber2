from flask import Flask, render_template, request
from pytube import YouTube

app = Flask(_name_)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/download', methods=["POST"])
def download_video():
    url = request.form["url"]
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    stream.download("downloads/")
    return f"Downloaded: {yt.title}"

if _name_ == '_main_':
    app.run(debug=True)