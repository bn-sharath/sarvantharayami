from flask import Flask, render_template, flash, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bns2001coder'


# SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://bns:bns2001coder@localhost/sdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

UPLOAD_FOLDER = os.path.join(os.getcwd(), "profile_image")
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(80), nullable=False)
    secondName = db.Column(db.String(80))
    phone = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    UserID = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    # profile = db.Column(db.String(100), nullable=False)
    addharID = db.Column(db.String(100), unique=True, nullable=False)
    profile_path = db.Column(db.Text)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, firstName, secondName, phone, email, UserID, password, profile_path, addharID):
        super().__init__()
        self.firstName=firstName
        self.secondName=secondName
        self.email=email
        self.phone=phone
        self.password=password
        self.profile_path=profile_path
        self.UserID=UserID
        self.addharID=addharID

# class Admin(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     firstName = db.Column(db.String(80), nullable=False)
#     secondName = db.Column(db.String(80))
#     phone = db.Column(db.String(15), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     adminID = db.Column(db.String(50), unique=True, nullable=False)
#     Password = db.Column(db.String(100), nullable=False)


# class Profile:


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/service")
def service():
    return render_template("service.html")


@app.route("/admin/<int:id>")
def admin(id):
    if(id == 54321):
        return render_template("admin_panel.html")
    else:
        return "for security please ender proper id"


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
    if request.method == "POST":
        user_firstname = request.form["firstname"]
        user_secondname = request.form["secondname"]
        user_email = request.form["email"]
        user_phone = request.form["phone_no"]
        user_password = request.form["password"]
        user_ID = request.form["userID"]
        user_addhar = request.form["addhar"]
        user_profile_image = request.files["profile"]
        duplicate={}

        if User.query.filter_by(email=user_email).first():
            duplicate["email"] = user_email
        
        if User.query.filter_by(phone=user_phone).first():
            duplicate["phone"] = user_phone
        
        if User.query.filter_by(UserID=user_ID).first():
            duplicate["userID"] = user_ID
        
        if User.query.filter_by(addharID=user_addhar).first():
            duplicate["addhar Number"] = user_addhar
        
        if duplicate:
            return render_template("register.html", duplicate=duplicate)
        else:    
            if user_profile_image and allowed_file(user_profile_image.filename):
                filename = secure_filename(user_profile_image.filename)
                profile_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                user_profile_image.save(profile_path)

            user_register = User(firstName=user_firstname, secondName=user_secondname, email=user_email, phone=user_phone,password=user_password, UserID=user_ID, addharID=user_addhar, profile_path=profile_path)
            
            db.session.add(user_register)
            db.session.commit()
            return redirect(url_for("login"))
    else:
        return render_template("register.html")


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


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
    # db.create_all()
    app.run(debug=True)
