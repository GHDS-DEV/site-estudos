from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def start():
    return render_template("home.html")


@app.route("/contact")
def contact_me():
    return render_template("contact.html")


@app.route("/projects")
def my_projects():
    return render_template("projects.html")


if __name__ == "__main__":
    app.run(debug=True)
