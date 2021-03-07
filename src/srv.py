from flask import Flask, url_for, render_template, request
from dynaconf import settings as _ds
from flask_mail import Mail, Message

from feedback_form import FeedBackForm

app = Flask(__name__)

app.config["MAIL_SERVER"] = "smtp.googlemail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = "spacexxx47@gmail.com"
app.config["MAIL_DEFAULT_SENDER"] = "spacexxx47@gmail.com"
app.config["MAIL_PASSWORD"] = _ds.MAIL_PASSWORD
app.config["CSRF_ENABLED"] = True
app.config["SECRET_KEY"] = _ds.SECRET_KEY

mail = Mail(app)


@app.route("/", methods=["POST", "GET"])
def index():
    feedback = FeedBackForm()
    if request.method == "POST":
        form()
    return render_template("index.html", form=feedback)


# @app.route("/post", methods=["POST", "GET"])
def form():
    if request.method == "POST":
        name = request.form["name"]
        print(name)
        email = request.form["email"]
        msg = request.form["message"]
        mail_message = Message("Order", recipients=[email])
        mail_message.body = f"Дороу,{name}, спасибо за заказ"
        mail.send(mail_message)


if __name__ == "__main__":
    app.run()
