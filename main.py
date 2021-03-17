from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/')
def home():
    response = requests.get("https://api.npoint.io/5abcca6f4e39b4955965").json()
    return render_template("index.html", blogs=response)


@app.route("/post/<blog_id>")
def post(blog_id):
    response = requests.get("https://api.npoint.io/5abcca6f4e39b4955965").json()[int(blog_id)-1]
    return render_template("post.html", blog=response)


if __name__ == "__main__":
    app.run(debug=True)
