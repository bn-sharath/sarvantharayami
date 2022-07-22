from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bns2001coder'


# SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://bns:bns2001coder@localhost/sdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(80), nullable=False)
    secondName = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/service")
def service():
    return render_template("service.html")


@app.route("/blog")
def blog():
    return render_template("blog.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    return render_template("login.html")


@app.route("/register", methods=['GET', 'POST'])
def register():
    return render_template("register.html")


@app.route("/otp", methods=['GET', 'POST'])
def otp_verify():
    return render_template("otp.html")


@app.route("/forgot_pw", methods=['GET', 'POST'])
def forgot_pw():
    return render_template("forgot_pw.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

if __name__ == '__main__':
    app.run(debug=True)
