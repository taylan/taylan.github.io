from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Taylan Aydinli"

if __name__ == "__main__":
    app.run()
