from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


# Create a Flask Instance
app = Flask(__name__)
app.config['SECRET_KEY'] = "my secret key"


# Create a Form Class
class NameForm(FlaskForm):
    name = StringField("What`s Your Name", validators=[DataRequired()])
    submit = SubmitField("Submit")


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


# Create name page
@app.route("/name", methods=['GET', 'POST'])
def name():
    name = None
    form = NameForm()
    # Validate Form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template("name.html", name=name, form=form)


# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


# Internal Server Error
@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 404
