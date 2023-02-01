from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    stuff = "This is <strong>Bold</strong> text"
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


















