from flask import Flask, render_template
import feedparser
import os

app = Flask(__name__)

def parse_feed(path_or_url):
    return feedparser.parse(path_or_url)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/lavanguardia/<section>")
def lavanguardia(section):
    local_path = f"rss/lavanguardia/{section}.xml"
    remote_url = f"https://www.lavanguardia.com/rss/{section}.xml"

    if os.path.exists(local_path):
        feed = parse_feed(local_path)
    else:
        feed = parse_feed(remote_url)

    return render_template("lavanguardia.html", feed=feed, section=section)
