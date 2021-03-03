from flask import Flask, url_for, render_template, request

from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'spacexxx47@gmail.com'  # введите свой адрес электронной почты здесь
app.config['MAIL_DEFAULT_SENDER'] = 'spacexxx47@gmail.com'  # и здесь
app.config['MAIL_PASSWORD'] = 'EADSbMFFD6GwBdM'  # введите пароль

mail = Mail(app)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/post", methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        print(name)
        email = request.form['email']
        msg = request.form['message']
        mail_message = Message("Order", recipients=[email])
        mail_message.body = f'Дороу,{name}, спасибо за заказ'
        mail.send(mail_message)
        return render_template('thanks.html', name=name)


if __name__ == '__main__':
    app.run()
