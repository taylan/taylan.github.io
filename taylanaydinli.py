from flask import (Flask, render_template)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/.well-known/acme-challenge/<id>")
def acme_challenge(id):
    return "vBlS7Sc9Nc5nb2lfVrVKhbhjEZd_OF7x__3aXQgrlHA.CyBrusGjiby7J5p0SvG0zGCwwXucb0wcMyT4mLHFfzc"

if __name__ == "__main__":
    app.run()
