from flask import Flask, render_template, flash, session, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os
from datetime import datetime
from flask_mail import Mail, Message

import generate_key_otp
import create_folder

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bns2001coder'


# SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://bns:bns2001coder@localhost/sdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'vishalpower2001@gmail.com'
app.config['MAIL_PASSWORD'] = "**********************"
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

PERSON_IMAGE_FOLDER = os.path.join(os.getcwd(), "persons")
CRIMINALS = "criminals"
MISSING_PERSON = "missing_person"
WANTED_PERSON = "wanted_person"
ALLOWED_PERSON = "allowed_person"
NOT_ALLOWED_PERSON = "not_allowed_person"
PROOF_FOLDER = os.path.join("static", "government_proof_doc")
PROFILE_UPLOAD_FOLDER = os.path.join("static", "profile_image")
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


db = SQLAlchemy(app)


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
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    catagory = db.Column(db.String(80))

    def __init__(self, firstName, secondName, phone, email, UserID, password, profile_path, addharID, catagory):
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


class Criminals(db.Model):
    _id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    image_path = db.Column(db.Text)
    gender = db.Column(db.String(10))  
    information = db.Column(db.Text)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, name, age, image_path, gender,information):
        super().__init__()
        self.name = name
        self.age = age
        self.image_path = image_path
        self.gender= gender
        self.information = information


class MissingPerson(db.Model):
    _id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    image_path = db.Column(db.Text)
    gender = db.Column(db.String(10))
    information = db.Column(db.Text)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, name, age, image_path,gender, information):
        super().__init__()
        self.name = name
        self.age = age
        self.image_path = image_path
        self.gender= gender
        self.information = information


class WantedPerson(db.Model):
    _id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    image_path = db.Column(db.Text)
    gender = db.Column(db.String(10))  
    information = db.Column(db.Text)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, name, age, image_path, gender,information):
        super().__init__()
        self.name = name
        self.age = age
        self.image_path = image_path
        self.gender=gender
        self.information = information


class Allowed(db.Model):
    _id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    image_path = db.Column(db.Text)
    gender = db.Column(db.String(10))  
    information = db.Column(db.Text)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, name, age, image_path,gender, information):
        super().__init__()
        self.name = name
        self.age = age
        self.image_path = image_path
        self.gender= gender
        self.information = information


class NotAllowed(db.Model):
    _id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    image_path = db.Column(db.Text)
    gender = db.Column(db.String(10))  
    information = db.Column(db.Text)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, name, age, image_path,gender, information):
        super().__init__()
        self.name = name
        self.age = age
        self.image_path = image_path
        self.gender= gender
        self.information = information


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


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        login_id = request.form["userID"]
        login_password = request.form["password"]

        if User.query.filter_by(UserID=login_id, password=login_password):
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

    return render_template("login.html")


@app.route("/logout")
def logout():
    # return "logout code should write"
    if "user_id" in session:
        session.pop("user_id", None)
        session.pop("privilage_key", None)
    return render_template("home.html")


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
                                 password=user_password, UserID=user_ID, addharID=user_addhar, profile_path=profile_path, catagory=catagory)

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
    if session['secure_key'] and session['otp']:
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
                            User_id=user_id, criminals_count=0, missing_count=0, wanted_count=0,allowed_count=0,not_allowed_count=0)

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

                        count = PersonCount(User_id=user_id, criminals_count=0, missing_count=0, wanted_count=0,allowed_count=0,not_allowed_count=0)

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
                        PRTID = PRIVATE_panel(private_ID=private_id, User_id=user_id)

                        count = PersonCount(User_id=user_id, criminals_count=0, missing_count=0, wanted_count=0,allowed_count=0,not_allowed_count=0)

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

                        count = PersonCount(User_id=user_id, criminals_count=0, missing_count=0, wanted_count=0,allowed_count=0,not_allowed_count=0)

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
    # return render_template("dashboard.html")
    if "user_id" in session:

        return render_template("dashboard.html")
    else:
        return redirect("/login")


@app.route("/add_person")
def add_person():
    if "user_id" in session:
        user = User.query.filter_by(UserID=session["user_id"]).first()
        privilage = user.catagory

        return render_template("add_person.html", privilage=privilage)
    else:
        return redirect("/login")


@app.route("/add_form/<int:type>", methods=["GET", "POST"])
def add_form(type):
    if "user_id" in session:
        if request.method == "GET":
            return render_template("add_form.html", type=type)

        if request.method == "POST":
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
                    store_path = os.path.join(PERSON_IMAGE_FOLDER, CRIMINALS)
                    person_count.criminals_count += 1

                    file_name = str(person_count.criminals_count)+file_extension
                    person_path = os.path.join(store_path, file_name)
                    person_image.save(person_path)
                    
                    add_person = Criminals(name=name,age=age,gender=gender,information=info,image_path=person_path)

                if catagory_type == "Missing person":
                    store_path = os.path.join(PERSON_IMAGE_FOLDER, MISSING_PERSON)
                    person_count.missing_count += 1

                    file_name = str(person_count.missing_count)+file_extension
                    person_path = os.path.join(store_path, file_name)
                    person_image.save(person_path)
                    
                    add_person = MissingPerson(name=name,age=age,gender=gender,information=info,image_path=person_path)

                if catagory_type == "Wanted person":
                    store_path = os.path.join(PERSON_IMAGE_FOLDER, WANTED_PERSON)
                    person_count.wanted_count += 1

                    file_name = str(person_count.wanted_count)+file_extension
                    person_path = os.path.join(store_path, file_name)
                    person_image.save(person_path)
                    
                    add_person = WantedPerson(name=name,age=age,gender=gender,information=info,image_path=person_path)

                if catagory_type == "Allowed person":
                    store_path = os.path.join(PERSON_IMAGE_FOLDER, ALLOWED_PERSON)
                    person_count.allowed_count += 1

                    file_name = str(person_count.allowed_count)+file_extension
                    person_path = os.path.join(store_path, file_name)
                    person_image.save(person_path)
                    
                    add_person = Allowed(name=name,age=age,gender=gender,information=info,image_path=person_path)

                if catagory_type == "Not Allowed person":
                    store_path = os.path.join(PERSON_IMAGE_FOLDER, NOT_ALLOWED_PERSON)
                    person_count.not_allowed_count += 1

                    file_name = str(person_count.not_allowed_count)+file_extension
                    person_path = os.path.join(store_path, file_name)
                    person_image.save(person_path)
                    
                    add_person = NotAllowed(name=name,age=age,gender=gender,information=info,image_path=person_path)
                
                
                
                db.session.add(add_person)
                db.session.commit()
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

        return render_template("configuration.html", privilage=privilage, camera_ip=camera_ip)
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
            # fname=request.form["fname"]
            # sname=request.form["sname"]
            # email=request.form["email"]
            # password=request.form["password"]
            # phone=request.form["phone"]
            # addhar=request.form["addhar"]
            # service=request.form["service"]
            # user_profile_image = request.files["profile"]
            # duplicate = {}

            # if User.query.filter_by(email=email).first():
            #     duplicate["email"] = email

            # if User.query.filter_by(phone=phone).first():
            #     duplicate["phone"] = phone

            # if User.query.filter_by(addharID=addhar).first():
            #     duplicate["addhar Number"] = addhar

            # if duplicate:
            #     return render_template("profile.html", duplicate=duplicate ,user=user)
            # else:
            #     if user_profile_image and allowed_file(user_profile_image.filename):
            #         filename = secure_filename(user_profile_image.filename)
            #         # if error occur use rename method to rename the file
            #         _, file_extension = os.path.splitext(filename)
            #         file_name = user.UserID+file_extension
            #         profile_path = os.path.join(PROFILE_UPLOAD_FOLDER, file_name)
            #         user_profile_image.save(profile_path)

            # user.firstName = fname
            # user.secondName = sname
            # user.email = email
            # user.password = password
            # user.addharID = addhar
            # user.phone = phone
            # user.catagory = service
            pass

        else:
            return render_template("profile.html", user=user)

    else:
        return redirect("/login")


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


if __name__ == '__main__':
    # db.create_all()
    app.run(debug=True)


# @app.route("/sendmail/<int:id>")
# def send_mail(id):
#     if id == 1:
#         msg = Message('security key and OTP', sender='vishalpower2001@gmail.com',
#                       recipients=['bnsharath2001@gmail.com'])
#         msg.body = "This is the email body from sarvantharayammi"
#         mail.send(msg)
#     elif id == 2:
#         pass

#     return redirect("/register_part2/1")
#     # return "successfull"
