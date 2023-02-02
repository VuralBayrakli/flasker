from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
#old sqlite db
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:NewPassword@localhost/our_users'

db = SQLAlchemy(app)


# add database  


app.config['SECRET_KEY'] = 'mysecretkey'
#init db


# create model
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self):
        return '<Name %r>' % self.name


#Create a Form class
class UserForm(FlaskForm):
    name = StringField("What is your name?", validators=[DataRequired()])
    email = StringField("What is your email?", validators=[DataRequired()])
    submit = SubmitField("Submit")


#Create a Form class
class NamerForm(FlaskForm):
    name = StringField("What is your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")




@app.route("/user/add", methods=["GET", "POST"])
def add_user():
    name = None
    form = UserForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user is None:
            user = Users(name=form.name.data, email=form.email.data)
            db.session.add(user)
            db.session.commit()
        name = form.name.data
        form.name.data = "" # Clear form
        form.email.data = "" # Clear form
        flash("User added successfully!")
    our_users = Users.query.order_by(Users.date_added)
    return render_template("add_user.html", form = form, name = name,
    our_users = our_users)

@app.route("/")
def index():
    stuff = "This is <strong>Bold</strong> text"
    flash("Welcome to my website")
    favos = ["apple", "banana", "orange"]
    return render_template("index.html", stuff = stuff, favos = favos)

@app.route("/user/<name>")
def user(name):
    return render_template("user.html", name =  name)

#Invalid Error
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Internal server error thing
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500




@app.route("/about")
def about():
    return render_template("about.html")

#Create name page
@app.route("/name", methods=["GET", "POST"])
def name():
    name = None
    form = NamerForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ""
        flash("Form Submitted Successfully!")

    return render_template("name.html", name =  name,
    form = form)


app.app_context().push()












