from flask import Flask, render_template


# Create a Flask Instance
app = Flask(__name__)


# Create a route decorator
@app.route("/")
def index():
    first_name = "John"
    stuff = "This is Bold text"

    favourite_pizza = ["Pizza1", "Pizza2", "Pizza3"]
    return render_template("index.html",
                           first_name=first_name,
                           stuff=stuff,
                           favourite_pizza=favourite_pizza)


# localhost:5000/user/John
@app.route("/user/<name>")
def user(name):
    return render_template("user.html", user_name=name)


# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


# Internal Server Error
@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 404
