from flask import Flask, render_template, request, redirect

import json
import random
import string

app = Flask(__name__)

DATA_FILE = "urls.json"


def generate_code(length=6):
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for _ in range(length))


def load_urls():
    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_urls(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/shorten", methods=["POST"])
def shorten():

    url = request.form.get("url", "").strip()

    urls = load_urls()

    code = generate_code()

    # Prevent duplicate short codes
    while code in urls:
        code = generate_code()

    urls[code] = {
        "url": url,
        "clicks": 0
    }

    save_urls(urls)

    short_link = request.host_url + "s/" + code

    return render_template(
        "index.html",
        short_link=short_link
    )
    
@app.route("/s/<code>")
def redirect_to_url(code):

    urls = load_urls()

    if code not in urls:
        return render_template("404.html"), 404

    urls[code]["clicks"] += 1

    save_urls(urls)

    return redirect(urls[code]["url"])

@app.route("/dashboard")
def dashboard():

    urls = load_urls()

    return render_template(
        "dashboard.html",
        urls=urls
    )


if __name__ == "__main__":
    app.run(debug=True)