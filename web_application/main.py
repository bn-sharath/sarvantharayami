from flask import Flask, render_template, flash, session, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os
from datetime import datetime
from multiprocessing import Process
from flask_mail import Mail, Message
from multiprocessing import Process

import cv2
import face_recognition
import generate_key_otp
import create_folder

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bns2001coder'


# SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://bns:bns2001coder@localhost/sbn'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'vishalpower2001@gmail.com'
app.config['MAIL_PASSWORD'] = "qmwzdkheglqyygwj"
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

db = SQLAlchemy(app)
mail = Mail(app)

PERSON_IMAGE_FOLDER = os.path.join('static', "persons")
CRIMINALS = "criminals"
MISSING_PERSON = "missing_person"
WANTED_PERSON = "wanted_person"
ALLOWED_PERSON = "allowed_person"
NOT_ALLOWED_PERSON = "not_allowed_person"
PROOF_FOLDER = os.path.join("static", "government_proof_doc")
PROFILE_UPLOAD_FOLDER = os.path.join("static", "profile_image")
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

FOUNDED_IMAGE_DIR = os.path.join("static", "found")

Criminal_encodings = []
Criminal_image_path = []
Criminal_obj = []

Missing_encodings = []
Missing_image_path = []
Missing_obj = []

Wanted_encodings = []
Wanted_image_path = []
Wanted_obj = []

Allowed_encodings = []
Allowed_image_path = []
Allowed_obj = []

Not_allowed_encodings = []
Not_allowed_image_path = []
Not_allowed_obj = []


videocapture_cctv = []
frames = []


ACTIVE = False


class Admin(db.Model):
    AdminID = db.Column(db.String(50), primary_key=True, autoincrement=False)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, AdminID ,password ):
        super().__init__()
        self.AdminID = AdminID
        self.password = password

class User(db.Model):
    UserID = db.Column(db.String(50), primary_key=True, autoincrement=False)
    firstName = db.Column(db.String(80), nullable=False)
    secondName = db.Column(db.String(80))
    phone = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    # profile = db.Column(db.String(100), nullable=False)
    addharID = db.Column(db.String(100), unique=True, nullable=False)
    profile_path = db.Column(db.Text)
    date = db.Column(db.DateTime, nullable=False, default=datetime.now)
    catagory = db.Column(db.String(80))
    verify = db.Column(db.Integer, default=0)


    def __init__(self, firstName, secondName, phone, email, UserID, password, profile_path, addharID, catagory,verify):
        super().__init__()
        self.UserID = UserID
        self.firstName = firstName
        self.secondName = secondName
        self.email = email
        self.phone = phone
        self.password = password
        self.profile_path = profile_path
        self.addharID = addharID
        self.catagory = catagory
        self.verify = verify


class Criminals(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    image_path = db.Column(db.Text)
    gender = db.Column(db.String(10))
    information = db.Column(db.Text)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    User_id = db.Column(db.String(50), nullable=False)

    def __init__(self, name, age, image_path, gender, information, User_id):
        super().__init__()
        self.name = name
        self.age = age
        self.image_path = image_path
        self.gender = gender
        self.information = information
        self.User_id = User_id


class MissingPerson(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    image_path = db.Column(db.Text)
    gender = db.Column(db.String(10))
    information = db.Column(db.Text)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    User_id = db.Column(db.String(50), nullable=False)

    def __init__(self, name, age, image_path, gender, information, User_id):
        super().__init__()
        self.name = name
        self.age = age
        self.image_path = image_path
        self.gender = gender
        self.information = information
        self.User_id = User_id


class WantedPerson(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    image_path = db.Column(db.Text)
    gender = db.Column(db.String(10))
    information = db.Column(db.Text)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    User_id = db.Column(db.String(50), nullable=False)

    def __init__(self, name, age, image_path, gender, information, User_id):
        super().__init__()
        self.name = name
        self.age = age
        self.image_path = image_path
        self.gender = gender
        self.information = information
        self.User_id = User_id


class Allowed(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    image_path = db.Column(db.Text)
    gender = db.Column(db.String(10))
    information = db.Column(db.Text)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    User_id = db.Column(db.String(50), nullable=False)

    def __init__(self, name, age, image_path, gender, information, User_id):
        super().__init__()
        self.name = name
        self.age = age
        self.image_path = image_path
        self.gender = gender
        self.information = information
        self.User_id = User_id


class NotAllowed(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    image_path = db.Column(db.Text)
    gender = db.Column(db.String(10))
    information = db.Column(db.Text)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    User_id = db.Column(db.String(50), nullable=False)

    def __init__(self, name, age, image_path, gender, information, User_id):
        super().__init__()
        self.name = name
        self.age = age
        self.image_path = image_path
        self.gender = gender
        self.information = information
        self.User_id = User_id


class Founded_person(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    db_image_path = db.Column(db.Text)
    # cctv_image_path = db.Column(db.Text)
    gender = db.Column(db.String(10))
    typeOfPerson = db.Column(db.String(50))
    information = db.Column(db.Text)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    User_id = db.Column(db.String(50), nullable=False)

    def __init__(self, name, age, typeOfPerson, db_image_path,  gender, information, User_id):
        super().__init__()
        self.name = name
        self.age = age
        self.db_image_path = db_image_path
        # self.cctv_image_path = cctv_image_path
        self.gender = gender
        self.typeOfPerson = typeOfPerson
        self.information = information
        self.User_id = User_id


class PersonCount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    User_id = db.Column(db.String(50), nullable=False)
    criminals_count = db.Column(db.Integer, default=0)
    missing_count = db.Column(db.Integer, default=0)
    wanted_count = db.Column(db.Integer, default=0)
    allowed_count = db.Column(db.Integer, default=0)
    not_allowed_count = db.Column(db.Integer, default=0)

    def __init__(self, User_id, criminals_count, missing_count, wanted_count, allowed_count, not_allowed_count):
        super().__init__()
        self.User_id = User_id
        self.criminals_count = criminals_count
        self.missing_count = missing_count
        self.wanted_count = wanted_count
        self.allowed_count = allowed_count
        self.not_allowed_count = not_allowed_count


class GOV_panel(db.Model):
    gov_ID = db.Column(db.String(150), primary_key=True, autoincrement=False)
    User_id = db.Column(db.String(50), unique=True, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    proof_path = db.Column(db.Text)

    def __init__(self, gov_ID, User_id, proof_path):
        super().__init__()
        self.gov_ID = gov_ID
        self.User_id = User_id
        self.proof_path = proof_path


class PUBLIC_panel(db.Model):
    public_ID = db.Column(
        db.String(150), primary_key=True, autoincrement=False)
    User_id = db.Column(db.String(50), unique=True, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    # proof_path = db.Column(db.Text)

    def __init__(self, public_ID, User_id):
        super().__init__()
        self.public_ID = public_ID
        self.User_id = User_id


class PRIVATE_panel(db.Model):
    private_ID = db.Column(
        db.String(150), primary_key=True, autoincrement=False)
    User_id = db.Column(db.String(50), unique=True, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    # proof_path = db.Column(db.Text)

    def __init__(self, private_ID, User_id):
        super().__init__()
        self.private_ID = private_ID
        self.User_id = User_id


class GENERAL_panel(db.Model):
    general_ID = db.Column(
        db.String(150), primary_key=True, autoincrement=False)
    User_id = db.Column(db.String(50), unique=True, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    # proof_path = db.Column(db.Text)

    def __init__(self, general_ID, User_id):
        super().__init__()
        self.general_ID = general_ID
        self.User_id = User_id


class Configure_camera(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    privilage_id = db.Column(db.String(150), nullable=False)
    User_id = db.Column(db.String(50), nullable=False)
    ip = db.Column(db.Text, nullable=False)

    def __init__(self, privilage_id, User_id, ip):
        super().__init__()
        self.privilage_id = privilage_id
        self.User_id = User_id
        self.ip = ip


@app.route("/adm_logout")
def adm_logout():
    
    if "admin_id" in session:
        session.pop("admin_id", None)
        
    return redirect("/")

@app.route("/adm_missing")
def adm_missing():
    
    if "admin_id" in session:
                
        criminal_list = Criminals.query.all()
        missing_list = MissingPerson.query.all()
        wanted_list = WantedPerson.query.all()
        allowed_list = Allowed.query.all()
        not_allowed_list = NotAllowed.query.all()  
    
        return render_template("adm_view_people.html", criminal_list=criminal_list, missing_list=missing_list, wanted_list=wanted_list, allowed_list=allowed_list, not_allowed_list=not_allowed_list)
    else:    
        return redirect("/admin")

@app.route("/adm_delete_person/<int:i>", methods=["POST"])
def adm_delete_person(i):
    if "admin_id" in session:

        if request.method == "POST":
            id = request.form["delete"]

            if i == 1:
                criminal_obj = Criminals.query.filter_by(_id=id).first()
                os.remove(criminal_obj.image_path)
                db.session.delete(criminal_obj)
                db.session.commit()
            if i == 2:
                missing_obj = MissingPerson.query.filter_by(_id=id).first()
                os.remove(missing_obj.image_path)
                db.session.delete(missing_obj)
                db.session.commit()

            if i == 3:
                wanted_obj = WantedPerson.query.filter_by(_id=id).first()
                os.remove(wanted_obj.image_path)
                db.session.delete(wanted_obj)
                db.session.commit()

          
            return redirect("/adm_missing")
    else:
        return redirect("/admin")

@app.route("/verify/<string:user_id>")
def verify(user_id):

    if "admin_id" in session:
        user = User.query.filter_by(UserID=user_id).first()
        user.verify = 1
        db.session.commit()
        return redirect("/dash")
    else:    
        return redirect("/admin")

@app.route("/reject/<string:user_id>")
def reject(user_id):
    
    if "admin_id" in session:
        user = User.query.filter_by(UserID=user_id).first()
        user.verify = 0
        db.session.commit()
        return redirect("/dash")
    else:
        return redirect("/admin")
    
     
    

@app.route("/admin", methods=['GET', 'POST'])
def admin():
    if request.method == "POST":
        A_login_id = request.form["userID"]
        A_login_password = request.form["password"]

        if Admin.query.filter_by(AdminID=A_login_id, password=A_login_password).first():
            session["admin_id"] = A_login_id
            return redirect("/dash")
        else:
            return render_template("admin.html", error="User id or password is incorrect, please re enter the user id and password")

    return render_template("admin.html")


@app.route("/dash", methods=['GET', 'POST'])
def dash():
    if "admin_id" in session:
        users = User.query.all()
        return render_template("dash.html", users = users)
    else:
        return redirect("/admin")


@app.route("/approved", methods=['GET', 'POST'])
def approved():
    if "admin_id" in session:
        users = User.query.all()    
        return render_template("adm_approved.html", users = users)
    else:
        return redirect("/admin")


@app.route("/rejected", methods=['GET', 'POST'])
def rejected():
    if "admin_id" in session:
        users = User.query.all()
        return render_template("adm_rejected.html", users = users)
    else:
        return redirect("/admin")


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        login_id = request.form["userID"]
        login_password = request.form["password"]

        if User.query.filter_by(UserID=login_id, password=login_password).first():
            session["user_id"] = login_id
            user = User.query.filter_by(UserID=session["user_id"]).first()

            if user.catagory == "government":
                user_pivilage = GOV_panel.query.filter_by(
                    User_id=user.UserID).first()
                session["privilage_key"] = user_pivilage.gov_ID

            elif user.catagory == "public":
                user_pivilage = PUBLIC_panel.query.filter_by(
                    User_id=user.UserID).first()
                session["privilage_key"] = user_pivilage.public_ID

            elif user.catagory == "private":
                user_pivilage = PRIVATE_panel.query.filter_by(
                    User_id=user.UserID).first()
                session["privilage_key"] = user_pivilage.private_ID

            elif user.catagory == "general":
                user_pivilage = GENERAL_panel.query.filter_by(
                    User_id=user.UserID).first()
                session["privilage_key"] = user_pivilage.general_ID

            return redirect("/dashboard")
        else:
            return render_template("login.html", error="User id or password is incorrect, please re enter the user id and password")

    return render_template("login.html")


@app.route("/logout")
def logout():
    # return "logout code should write"
    if "user_id" in session:
        session.pop("user_id", None)
        session.pop("privilage_key", None)
    return redirect("/")


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == "POST" and "otp" not in session:
        user_firstname = request.form["firstname"]
        user_secondname = request.form["secondname"]
        user_email = request.form["email"]
        user_phone = request.form["phone_no"]
        user_password = request.form["password"]
        user_ID = request.form["userID"]
        user_addhar = request.form["addhar"]
        catagory = request.form["service"]
        user_profile_image = request.files["profile"]
        duplicate = {}

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
                # if error occur use rename method to rename the file
                _, file_extension = os.path.splitext(filename)
                file_name = user_ID+file_extension
                profile_path = os.path.join(PROFILE_UPLOAD_FOLDER, file_name)
                user_profile_image.save(profile_path)

            user_register = User(firstName=user_firstname, secondName=user_secondname, email=user_email, phone=user_phone,
                                 password=user_password, UserID=user_ID, addharID=user_addhar, profile_path=profile_path, catagory=catagory,verify=None)

# sending mail code
            msg = Message('security key and OTP of user-id : '+user_ID, sender='vishalpower2001@gmail.com',
                          recipients=[user_email])
            key = generate_key_otp.createKEY(
                catagory, user_firstname, user_addhar)
            otp = generate_key_otp.createOTP()
            msg.body = "secure key for registration = "+key+"<br>\n the OTP = " + otp
            mail.send(msg)
# adding key and otp to session
            session["secure_key"] = key
            session["otp"] = otp

# inserting user to database
            db.session.add(user_register)
            db.session.commit()
            return render_template("register_part2.html", form_id=catagory)
            # return redirect(url_for("register_part2/"+catagory))
    else:
        return render_template("register.html")


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/register_part2/<form_id>", methods=['GET', 'POST'])
def register_part2(form_id):
    if "secure_key" in session and "otp" in session:
        if request.method == "POST":
            if form_id == "government":
                gov_id = request.form["ID"]
                otp = request.form["otp"]
                ID_proof = request.files["ID_proof"]
                user_id = request.form["userid"]

                if User.query.filter_by(UserID=user_id).first():

                    if session["secure_key"] == gov_id and session["otp"] == otp:
                        if ID_proof:
                            filename = secure_filename(ID_proof.filename)
                            _, file_extension = os.path.splitext(filename)
                            file_name = gov_id+file_extension
                            proof_path = os.path.join(PROOF_FOLDER, file_name)
                            ID_proof.save(proof_path)

                        GOVID = GOV_panel(
                            gov_ID=gov_id, User_id=user_id, proof_path=proof_path)
                        count = PersonCount(
                            User_id=user_id, criminals_count=0, missing_count=0, wanted_count=0, allowed_count=0, not_allowed_count=0)

                        # creation of folders
                        create_folder.folder_create(
                            folder_path=PERSON_IMAGE_FOLDER, name=user_id)
                        create_folder.folder_create(folder_path=os.path.join(
                            PERSON_IMAGE_FOLDER, user_id), name=CRIMINALS)
                        create_folder.folder_create(folder_path=os.path.join(
                            PERSON_IMAGE_FOLDER, user_id), name="missing_person")
                        create_folder.folder_create(folder_path=os.path.join(
                            PERSON_IMAGE_FOLDER, user_id), name="wanted_person")

                        db.session.add(count)
                        db.session.add(GOVID)
                        db.session.commit()
                        session.pop("secure_key", None)
                        session.pop("otp", None)
                        return redirect("/login")

                    else:
                        err = "OTP and KEY is incorrect please check and re-enter again"
                        return render_template("register_part2.html", form_id=form_id, error=err)
                else:
                    err = "User ID not found please check your user-id and re-enter "
                    return render_template("register_part2.html", form_id=form_id, error=err)

            if form_id == "public":
                public_id = request.form["ID"]
                otp = request.form["otp"]
                user_id = request.form["userid"]

                if User.query.filter_by(UserID=user_id).first():

                    if session["secure_key"] == public_id and session["otp"] == otp:
                        session.pop("secure_key", None)
                        session.pop("otp", None)
                        PUBID = PUBLIC_panel(
                            public_ID=public_id, User_id=user_id)

                        count = PersonCount(User_id=user_id, criminals_count=0, missing_count=0,
                                            wanted_count=0, allowed_count=0, not_allowed_count=0)

                        # creation of folders
                        create_folder.folder_create(
                            folder_path=PERSON_IMAGE_FOLDER, name=user_id)
                        create_folder.folder_create(folder_path=os.path.join(
                            PERSON_IMAGE_FOLDER, user_id), name=MISSING_PERSON)

                        db.session.add(count)
                        db.session.add(PUBID)
                        db.session.commit()
                        return redirect("/login")
                    else:
                        err = "OTP and KEY is incorrect please check and re-enter again"
                        return render_template("register_part2.html", form_id=form_id, error=err)
                else:
                    err = "User ID not found please check your user-id and re-enter "
                    return render_template("register_part2.html", form_id=form_id, error=err)

            if form_id == "private":
                private_id = request.form["ID"]
                otp = request.form["otp"]
                user_id = request.form["userid"]

                if User.query.filter_by(UserID=user_id).first():

                    if session["secure_key"] == private_id and session["otp"] == otp:
                        session.pop("secure_key", None)
                        session.pop("otp", None)
                        PRTID = PRIVATE_panel(
                            private_ID=private_id, User_id=user_id)

                        count = PersonCount(User_id=user_id, criminals_count=0, missing_count=0,
                                            wanted_count=0, allowed_count=0, not_allowed_count=0)

                        # creation of folders
                        create_folder.folder_create(
                            folder_path=PERSON_IMAGE_FOLDER, name=user_id)
                        create_folder.folder_create(folder_path=os.path.join(
                            PERSON_IMAGE_FOLDER, user_id), name=MISSING_PERSON)
                        create_folder.folder_create(folder_path=os.path.join(
                            PERSON_IMAGE_FOLDER, user_id), name=ALLOWED_PERSON)
                        create_folder.folder_create(folder_path=os.path.join(
                            PERSON_IMAGE_FOLDER, user_id), name=NOT_ALLOWED_PERSON)

                        db.session.add(count)
                        db.session.add(PRTID)
                        db.session.commit()
                        return redirect("/login")
                    else:
                        err = "OTP and KEY is incorrect please check and re-enter again"
                        return render_template("register_part2.html", form_id=form_id, error=err)
                else:
                    err = "User ID not found please check your user-id and re-enter "
                    return render_template("register_part2.html", form_id=form_id, error=err)

            if form_id == "general":
                general_id = request.form["ID"]
                otp = request.form["otp"]
                user_id = request.form["userid"]

                if User.query.filter_by(UserID=user_id).first():

                    if session["secure_key"] == general_id and session["otp"] == otp:
                        session.pop("secure_key", None)
                        session.pop("otp", None)
                        GENID = GENERAL_panel(
                            general_ID=general_id, User_id=user_id)

                        count = PersonCount(User_id=user_id, criminals_count=0, missing_count=0,
                                            wanted_count=0, allowed_count=0, not_allowed_count=0)

                        # creation of folders
                        create_folder.folder_create(
                            folder_path=PERSON_IMAGE_FOLDER, name=user_id)
                        create_folder.folder_create(folder_path=os.path.join(
                            PERSON_IMAGE_FOLDER, user_id), name=MISSING_PERSON)

                        db.session.add(count)
                        db.session.add(GENID)
                        db.session.commit()
                        return redirect("/login")
                    else:
                        err = "OTP and KEY is incorrect please check and re-enter again"
                        return render_template("register_part2.html", form_id=form_id, error=err)
                else:
                    err = "User ID not found please check your user-id and re-enter "
                    return render_template("register_part2.html", form_id=form_id, error=err)
        else:
            return render_template("register_part2.html", form_id=form_id)

    return redirect("/register")


@app.route("/otp", methods=['GET', 'POST'])
def otp_verify():

    return render_template("otp.html")


@app.route("/forgot_pw", methods=['GET', 'POST'])
def forgot_pw():
    if request.method == "POST":
        email = request.form["email"]
        if User.query.filter_by(email=email):
            otp = generate_key_otp.createOTP()
            body = " the OTP = " + otp

            msg = Message('forgot password OTP', body=body, sender='vishalpower2001@gmail.com',
                          recipients=[email])
            # key = generate_key_otp.createKEY(catagory, user_firstname, user_addhar)
            mail.send(msg)
            session["f_otp"] = otp
            return redirect("/otp")
        else:
            error = "This email is not register"
            return render_template("forgot_pw.html", error=error)

    return render_template("forgot_pw.html")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/service")
def service():
    return render_template("service.html")


@app.route("/dashboard")
def dashboard():
    if "user_id" in session:
        user = User.query.filter_by(UserID=session["user_id"]).first()
        if user.verify == 1:

            privilage = user.catagory
            criminalfound = Founded_person.query.filter_by(typeOfPerson="criminal")
            misssingfound = Founded_person.query.filter_by(typeOfPerson="missing person")
            wantedfound = Founded_person.query.filter_by(typeOfPerson="wanted person")
            Allowedfound = Founded_person.query.filter_by(typeOfPerson="allowed person")
            notAllowedfound = Founded_person.query.filter_by(typeOfPerson="not allowed person")

            return render_template("dashboard.html", cf = criminalfound,mf= misssingfound, wf=wantedfound,af=Allowedfound,nf=notAllowedfound,privilage=privilage )
        else:
            return render_template("verification.html", user=user )
    else:
        return redirect("/login")


@app.route("/delete_found",methods=["POST"])
def delete_found():
    if "user_id" in session:
        if request.method == "POST":
            id = request.form["delete"]
            obj = Founded_person.query.filter_by(_id=id).first()
            db.session.delete(obj)
            db.session.commit()
            return redirect("/dashboard")
    else:
        return redirect("/login")


@app.route("/activate")
def activate_cctv():
    global ACTIVE
    if not ACTIVE:
        ACTIVE = True
        fetch_person()
        fetch_cctv()
        # p = Process(target=db_encoding_run)
        db_encoding_run()
        # p.start()
        print("activate")

    return redirect("dashboard")


@app.route("/deactivate")
def deactivate_cctv():

    global ACTIVE
    if ACTIVE:
        ACTIVE = False
        clear_encodings()
        clear_cctv()
        # p.kill()
        print("de activate")

    return redirect("dashboard")


@app.route("/add_person")
def add_person():
    if "user_id" in session:
        user = User.query.filter_by(UserID=session["user_id"]).first()
        privilage = user.catagory

        return render_template("add_person.html", privilage=privilage, active=ACTIVE)

    else:
        return redirect("/login")


@app.route("/view_person")
def view_person():
    if "user_id" in session:
        criminal_list = Criminals.query.filter_by(
            User_id=session['user_id']).all()
        missing_list = MissingPerson.query.filter_by(
            User_id=session['user_id']).all()
        wanted_list = WantedPerson.query.filter_by(
            User_id=session['user_id']).all()
        allowed_list = Allowed.query.filter_by(
            User_id=session['user_id']).all()
        not_allowed_list = NotAllowed.query.filter_by(
            User_id=session['user_id']).all()
        return render_template("view_person.html", criminal_list=criminal_list, missing_list=missing_list, wanted_list=wanted_list, allowed_list=allowed_list, not_allowed_list=not_allowed_list)
    else:
        return redirect("/login")


@app.route("/edit_person/<int:i>", methods=["GET", "POST"])
def edit_person(i):
    if "user_id" in session:
        id = request.form["edit"]

        if request.method == "POST":
            if i == 1:
                criminal_obj = Criminals.query.filter_by(_id=id).first()
                return render_template("edit_form.html", i=i, person=criminal_obj)
            if i == 2:
                missing_obj = MissingPerson.query.filter_by(_id=id).first()
                return render_template("edit_form.html", i=i, person=missing_obj)

            if i == 3:
                wanted_obj = WantedPerson.query.filter_by(_id=id).first()
                return render_template("edit_form.html", i=i, person=wanted_obj)

            if i == 4:
                allowed_obj = Allowed.query.filter_by(_id=id).first()
                return render_template("edit_form.html", i=i, person=allowed_obj)

            if i == 5:
                not_allowed_obj = NotAllowed.query.filter_by(_id=id).first()
                return render_template("edit_form.html", i=i, person=not_allowed_obj)

            return redirect("/view_person")
    else:
        return redirect("/login")


@app.route("/delete_person/<int:i>", methods=["POST"])
def delete_person(i):
    if "user_id" in session:

        if request.method == "POST":
            id = request.form["delete"]

            if i == 1:
                criminal_obj = Criminals.query.filter_by(_id=id).first()
                os.remove(criminal_obj.image_path)
                db.session.delete(criminal_obj)
                db.session.commit()
            if i == 2:
                missing_obj = MissingPerson.query.filter_by(_id=id).first()
                os.remove(missing_obj.image_path)
                db.session.delete(missing_obj)
                db.session.commit()

            if i == 3:
                wanted_obj = WantedPerson.query.filter_by(_id=id).first()
                os.remove(wanted_obj.image_path)
                db.session.delete(wanted_obj)
                db.session.commit()

            if i == 4:
                allowed_obj = Allowed.query.filter_by(_id=id).first()
                os.remove(allowed_obj.image_path)
                db.session.delete(allowed_obj)
                db.session.commit()

            if i == 5:
                not_allowed_obj = NotAllowed.query.filter_by(_id=id).first()
                os.remove(not_allowed_obj.image_path)
                db.session.delete(not_allowed_obj)
                db.session.commit()

            return redirect("/view_person")
    else:
        return redirect("/login")


@app.route("/edit_form/<int:i>", methods=["POST"])
def edit_form(i):
    if "user_id" in session:

        if request.method == "POST":
            person_count = PersonCount.query.filter_by(
                User_id=session["user_id"]).first()

            id = request.form["person_id"]
            if i == 1:
                criminal_obj = Criminals.query.filter_by(_id=id).first()
                if request.form["name"]:
                    criminal_obj.name = request.form["name"]

                if request.form["age"]:
                    criminal_obj.age = request.form["age"]

                if request.form["gender"]:
                    criminal_obj.gender = request.form["gender"]

                if request.form["info"]:
                    criminal_obj.information = request.form["info"]

                if request.files["person"]:
                    person_image = request.files["person"]
                    filename = secure_filename(person_image.filename)

                    path_image = criminal_obj.image_path
                    person_path = os.path.join(path_image)
                    os.remove(path_image)

                    person_image.save(person_path)

                db.session.commit()
            if i == 2:
                missing_obj = MissingPerson.query.filter_by(_id=id).first()
                if request.form["name"]:
                    missing_obj.name = request.form["name"]

                if request.form["age"]:
                    missing_obj.age = request.form["age"]

                if request.form["gender"]:
                    print(request.form["gender"])
                    missing_obj.gender = request.form["gender"]

                if request.form["info"]:
                    missing_obj.information = request.form["info"]

                if request.files["person"]:
                    person_image = request.files["person"]
                    filename = secure_filename(person_image.filename)
                    path_image = missing_obj.image_path
                    person_path = os.path.join(path_image)
                    os.remove(path_image)

                    person_image.save(person_path)

                db.session.commit()

            if i == 3:
                wanted_obj = WantedPerson.query.filter_by(_id=id).first()
                if request.form["name"]:
                    wanted_obj.name = request.form["name"]

                if request.form["age"]:
                    wanted_obj.age = request.form["age"]

                if request.form["gender"]:
                    wanted_obj.gender = request.form["gender"]

                if request.form["info"]:
                    wanted_obj.information = request.form["info"]

                if request.files["person"]:
                    person_image = request.files["person"]
                    filename = secure_filename(person_image.filename)
                    path_image = wanted_obj.image_path

                    person_path = os.path.join(path_image)
                    os.remove(path_image)

                    person_image.save(person_path)

                db.session.commit()

            if i == 4:
                allowed_obj = Allowed.query.filter_by(_id=id).first()
                if request.form["name"]:
                    allowed_obj.name = request.form["name"]

                if request.form["age"]:
                    allowed_obj.age = request.form["age"]

                if request.form["gender"]:
                    allowed_obj.gender = request.form["gender"]

                if request.form["info"]:
                    allowed_obj.information = request.form["info"]

                if request.files["person"]:
                    person_image = request.files["person"]
                    filename = secure_filename(person_image.filename)
                    path_image = allowed_obj.image_path

                    person_path = os.path.join(path_image)
                    os.remove(path_image)

                    person_image.save(person_path)

                db.session.commit()

            if i == 5:
                not_allowed_obj = NotAllowed.query.filter_by(_id=id).first()
                if request.form["name"]:
                    not_allowed_obj.name = request.form["name"]

                if request.form["age"]:
                    not_allowed_obj.age = request.form["age"]

                if request.form["gender"]:
                    not_allowed_obj.gender = request.form["gender"]

                if request.form["info"]:
                    not_allowed_obj.information = request.form["info"]

                if request.files["person"]:
                    person_image = request.files["person"]
                    filename = secure_filename(person_image.filename)
                    path_image = not_allowed_obj.image_path

                    person_path = os.path.join(path_image)
                    os.remove(path_image)

                    person_image.save(person_path)

                db.session.commit()

            return redirect("/view_person")

    else:
        return redirect("/login")


@app.route("/add_form/<int:type>", methods=["GET", "POST"])
def add_form(type):
    if "user_id" in session:
        if request.method == "GET":
            return render_template("add_form.html", type=type)

        elif request.method == "POST":
            name = request.form["name"]
            age = request.form["age"]
            gender = request.form["gender"]
            catagory_type = request.form["type"]
            info = request.form["info"]
            person_image = request.files["person"]

            person_count = PersonCount.query.filter_by(
                User_id=session["user_id"]).first()

            if person_image and allowed_file(person_image.filename):
                filename = secure_filename(person_image.filename)
                _, file_extension = os.path.splitext(filename)

                if catagory_type == "Criminal":
                    store_path = os.path.join(
                        PERSON_IMAGE_FOLDER, person_count.User_id, CRIMINALS)
                    person_count.criminals_count += 1

                    file_name = str(
                        person_count.criminals_count)+file_extension
                    person_path = os.path.join(store_path, file_name)
                    person_image.save(person_path)

                    add_person = Criminals(
                        name=name, age=age, gender=gender, information=info, image_path=person_path, User_id=person_count.User_id)

                if catagory_type == "Missing person":
                    store_path = os.path.join(
                        PERSON_IMAGE_FOLDER, person_count.User_id, MISSING_PERSON)
                    person_count.missing_count += 1

                    file_name = str(person_count.missing_count)+file_extension
                    person_path = os.path.join(store_path, file_name)
                    person_image.save(person_path)

                    add_person = MissingPerson(
                        name=name, age=age, gender=gender, information=info, image_path=person_path, User_id=person_count.User_id)

                if catagory_type == "Wanted person":
                    store_path = os.path.join(
                        PERSON_IMAGE_FOLDER, person_count.User_id, WANTED_PERSON)
                    person_count.wanted_count += 1

                    file_name = str(person_count.wanted_count)+file_extension
                    person_path = os.path.join(store_path, file_name)
                    person_image.save(person_path)

                    add_person = WantedPerson(
                        name=name, age=age, gender=gender, information=info, image_path=person_path, User_id=person_count.User_id)

                if catagory_type == "Allowed person":
                    store_path = os.path.join(
                        PERSON_IMAGE_FOLDER, person_count.User_id, ALLOWED_PERSON)
                    person_count.allowed_count += 1

                    file_name = str(person_count.allowed_count)+file_extension
                    person_path = os.path.join(store_path, file_name)
                    person_image.save(person_path)

                    add_person = Allowed(
                        name=name, age=age, gender=gender, information=info, image_path=person_path, User_id=person_count.User_id)

                if catagory_type == "Not Allowed person":
                    store_path = os.path.join(
                        PERSON_IMAGE_FOLDER, person_count.User_id, NOT_ALLOWED_PERSON)
                    person_count.not_allowed_count += 1

                    file_name = str(
                        person_count.not_allowed_count)+file_extension
                    person_path = os.path.join(store_path, file_name)
                    person_image.save(person_path)

                    add_person = NotAllowed(
                        name=name, age=age, gender=gender, information=info, image_path=person_path, User_id=person_count.User_id)

                db.session.add(add_person)
                db.session.commit()

            return redirect("/add_person")
    else:
        return redirect("/login")


@app.route("/liveVideo")
def live_video():
    # return render_template("live_video.html")
    if "user_id" in session:
        user = User.query.filter_by(UserID=session["user_id"]).first()
        ip_src = Configure_camera.query.filter_by(User_id=user.UserID).all()

        return render_template("live_video.html", ip_src=ip_src)

    else:
        return redirect("/login")


@app.route("/configure")
def configure():
    # return render_template("configuration.html")
    if "user_id" in session:
        user = User.query.filter_by(UserID=session["user_id"]).first()
        privilage = user.catagory
        camera_ip = Configure_camera.query.filter_by(User_id=user.UserID).all()

        return render_template("configuration.html", privilage=privilage, camera_ip=camera_ip, active=ACTIVE)
    else:
        return redirect("/login")


@app.route("/config_add", methods=["POST"])
def config_add():
    if request.method == "POST":
        ip = request.form["ip_add"]
        camera = Configure_camera(
            privilage_id=session["privilage_key"], User_id=session["user_id"], ip=ip)

        db.session.add(camera)
        db.session.commit()
        return redirect("/configure")
    else:
        return redirect("/")


@app.route("/delete_ip/<int:id>")
def delete_ip(id):
    if "user_id" in session:
        camera_obj = Configure_camera.query.filter_by(id=id).first()
        db.session.delete(camera_obj)
        db.session.commit()
        return redirect("/configure")
    else:
        return redirect("/login")


@app.route("/config_edit", methods=["POST"])
def config_edit():
    # print("hello")
    if request.method == "POST":
        ip_id = request.form["edit"]
        camera_obj = Configure_camera.query.filter_by(id=ip_id).first()
        camera_obj.ip = request.form["ip_edit"]
        db.session.add(camera_obj)
        db.session.commit()
        return redirect("/configure")
    else:
        return redirect("/")


@app.route("/profile", methods=['GET', 'POST'])
def profile():
    if "user_id" in session:
        user = User.query.filter_by(UserID=session["user_id"]).first()
        if request.method == "POST":
            duplicate = {}

            if request.form["fname"]:
                user.firstName = request.form["fname"]

            if request.form["sname"]:
                user.secondName = request.form["sname"]

            if request.form["email"]:
                if User.query.filter_by(email=request.form["email"]).first():
                    duplicate["email"] = request.form["email"]
                else:
                    user.email = request.form["email"]

            if request.form["password"]:
                user.password = request.form["password"]

            if request.form["phone"]:
                if User.query.filter_by(phone=request.form["phone"]).first():
                    duplicate["phone"] = request.form["phone"]
                else:
                    user.phone = request.form["phone"]

            if request.form["addhar"]:
                if User.query.filter_by(addharID=request.form["addhar"]).first():
                    duplicate["addhar Number"] = request.form["addhar"]
                else:
                    user.addharID = request.form["addhar"]

            if request.form["service"]:
                user.catagory = request.form["service"]

            if "profile" in request.files:
                user_profile_image = request.files["profile"]

            if user_profile_image and allowed_file(user_profile_image.filename):
                filename = secure_filename(user_profile_image.filename)
                # if error occur use rename method to rename the file
                _, file_extension = os.path.splitext(filename)
                file_name = user.UserID+file_extension
                profile_path = os.path.join(
                    PROFILE_UPLOAD_FOLDER, file_name)
                os.remove(user.profile_path)
                user_profile_image.save(profile_path)
                user.profile_path = profile_path

                db.session.commit()
            return render_template("profile.html", duplicate=duplicate, user=user)

        else:
            return render_template("profile.html", user=user)

    else:
        return redirect("/login")


def found_result(person_obj, image_path, type_of_person):
    print("person fonded-1")
    name = person_obj.name
    age = person_obj.age
    db_image_path = image_path
    # cctv_image_path = image
    gender = person_obj.gender
    information = person_obj.information
    User_id = person_obj.User_id
    typeOfPerson = type_of_person
    found_person = Founded_person(name=name, age=age, gender=gender, db_image_path=db_image_path, information=information, User_id=User_id, typeOfPerson=typeOfPerson)

    print("person fonded-2")
    db.session.add(found_person)
    db.session.commit()


def fetch_person():
    c_db_image = Criminals.query.all()
    m_db_image = MissingPerson.query.all()
    w_db_image = WantedPerson.query.all()
    a_db_image = Allowed.query.all()
    n_db_image = NotAllowed.query.all()

    collect_person(c_db=c_db_image, m_db=m_db_image,
                   w_db=w_db_image, a_db=a_db_image, n_db=n_db_image)


def fetch_cctv():
    print("fetching")
    ip = Configure_camera.query.all()
    print(ip[0].ip)
    collect_cctv(cctv_ip=ip)


def collect_person(c_db, m_db, w_db, a_db, n_db):
    for c in c_db:
        Criminal_image_path.append(c.image_path)
        Criminal_obj.append(c)
        # img = cv2.imread(c.image_path)
        img = face_recognition.load_image_file(c.image_path)
        img = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        encode_img = face_recognition.face_encodings(img)[0]
        Criminal_encodings.append(encode_img)
        # cv2.imshow("hello",img)
        print(encode_img)

    for c in m_db:
        Missing_image_path.append(c.image_path)
        Missing_obj.append(c)
        img = face_recognition.load_image_file(c.image_path)
        # img = cv2.imread(c.image_path)
        img = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        encode_img = face_recognition.face_encodings(img)[0]
        Missing_encodings.append(encode_img)
        print(c.image_path)

    for c in a_db:
        Wanted_image_path.append(c.image_path)
        Wanted_obj.append(c)
        img = face_recognition.load_image_file(c.image_path)
        # img = cv2.imread(c.image_path)
        img = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        encode_img = face_recognition.face_encodings(img)[0]
        Wanted_encodings.append(encode_img)
        print(c.image_path)

    for c in w_db:
        Allowed_image_path.append(c.image_path)
        Allowed_obj.append(c)
        img = face_recognition.load_image_file(c.image_path)
        # img = cv2.imread(c.image_path)
        img = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        encode_img = face_recognition.face_encodings(img)[0]
        Allowed_encodings.append(encode_img)
        print(c.image_path)

    for c in n_db:
        Not_allowed_image_path.append(c.image_path)
        img = face_recognition.load_image_file(c.image_path)
        Not_allowed_obj.append(c)
        # img = cv2.imread(c.image_path)
        img = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        encode_img = face_recognition.face_encodings(img)[0]
        Not_allowed_encodings.append(encode_img)
        print(c.image_path)


def frame_encoding(f):
    print("function endered")
    face_loc = face_recognition.face_locations(f)
    encoding_test_image = face_recognition.face_encodings(f, face_loc)
    for face_encode, location in zip(encoding_test_image, face_loc):
        criminal_result = face_recognition.compare_faces(
            Criminal_encodings, face_encode)
        missing_result = face_recognition.compare_faces(
            Missing_encodings, face_encode)
        wanted_result = face_recognition.compare_faces(
            Wanted_encodings, face_encode)
        allowed_result = face_recognition.compare_faces(
            Allowed_encodings, face_encode)
        not_allowed_result = face_recognition.compare_faces(
            Not_allowed_encodings, face_encode)
        print("runnin -2 hi")
        if True in criminal_result:
            obj = Criminal_obj[criminal_result.index(True)]
            ipath = Criminal_image_path[criminal_result.index(True)]
            # cv2.imwrite(filename=FOUNDED_IMAGE_DIR+str(obj.name), img=f)
            print("runnin -3 hello")
            found_result(person_obj=obj, image_path=ipath,type_of_person="criminal")
            

        if True in missing_result:
            obj = Missing_obj[missing_result.index(True)]
            ipath = Missing_image_path[missing_result.index(True)]
            # cv2.imwrite(filename=FOUNDED_IMAGE_DIR+str(obj._id), img=f)
            found_result(person_obj=obj, image_path=ipath,  type_of_person="missing person")

        if True in wanted_result:
            obj = Wanted_obj[wanted_result.index(True)]
            ipath = Wanted_image_path[wanted_result.index(True)]
            # cv2.imwrite(filename=FOUNDED_IMAGE_DIR+str(obj._id), img=f)
            found_result(person_obj=obj, image_path=ipath, type_of_person="wanted person")

        if True in allowed_result:
            obj = Allowed_obj[allowed_result.index(True)]
            ipath = Allowed_image_path[allowed_result.index(True)]
            # cv2.imwrite(filename=FOUNDED_IMAGE_DIR+str(obj._id), img=f)
            found_result(person_obj=obj, image_path=ipath, type_of_person="allowed person")

        if True in not_allowed_result:
            obj = Not_allowed_obj[not_allowed_result.index(True)]
            ipath = Not_allowed_image_path[not_allowed_result.index(True)]
            # cv2.imwrite(filename=FOUNDED_IMAGE_DIR+str(obj._id), img=f)
            found_result(person_obj=obj, image_path=ipath,  type_of_person="not allowed person")


def collect_cctv(cctv_ip):
    print("cctv updating")
    for ip in cctv_ip:
        cap = "http://" + str(ip.ip)
        try:
            videocapture_cctv.append(cv2.VideoCapture(cap))
            print("videocapture over" + cap)
        except:
            print(ip.ip)
    print(len(videocapture_cctv))
    

def db_encoding_run():
    print("process started")
    
    no_of_camera = len(videocapture_cctv)
    print(no_of_camera)
   
    f = [None]*no_of_camera

    while no_of_camera > 0:
        print("running -1")
        for i in range(no_of_camera):
            _, f[i] = videocapture_cctv[i].read()
            # cv2.imshow(str(i), frames[i])
            print("camera -" + str(i))
            print("ender in for")
            frame_encoding(f[i])
            
    for tv in videocapture_cctv:
        tv.release()
   

def clear_cctv():
    videocapture_cctv.clear()


def clear_encodings():
    Criminal_encodings.clear()
    Criminal_image_path.clear()
    Criminal_obj.clear()
    Missing_encodings.clear()
    Missing_image_path.clear()
    Missing_obj.clear()
    Wanted_encodings.clear()
    Wanted_image_path.clear()
    Wanted_obj.clear()

    Allowed_encodings.clear()
    Allowed_image_path.clear()
    Allowed_obj.clear()

    Not_allowed_encodings.clear()
    Not_allowed_image_path.clear()
    Not_allowed_obj.clear()


if __name__ == '__main__':
    print("started")
    with app.app_context():
        db.create_all()
    
    print("success")
    app.run(debug=True)
    # app.run()
