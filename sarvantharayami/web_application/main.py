from flask import Flask , render_template, url_for, request

app = Flask(__name__)

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

@app.route("/register", methods=['GET','POST'])
def register():
    return render_template("register.html")

@app.route("/otp" , methods=['GET', 'POST'])
def otp_verify():
    return render_template("otp.html")

@app.route("/forgot_pw" , methods=['GET', 'POST'])
def forgot_pw():
    return render_template("forgot_pw.html")





if __name__ == '__main__':
    app.run(debug=True)
