from flask import Flask , render_template, url_for

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

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")





if __name__ == '__main__':
    app.run(debug=True)
