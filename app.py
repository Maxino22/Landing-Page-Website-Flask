from flask import Flask, redirect, render_template, url_for, flash, request
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = 'mysecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\Maxino\\Desktop\\Loooplab_Flask\\db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


class SignUpForm(FlaskForm):
    name = StringField()
    email = StringField()
    password = PasswordField()
    pass_confirm = PasswordField()
    submit = SubmitField()

# database


class Contact(db.Model):
    __tablename__ = "Contact Form"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    message = db.Column(db.String(500))


class SignUp(db.Model):
    __tablename__ = "Sign Up"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SignUpForm()
    if form.validate_on_submit():
        user = SignUp(name=form.name.data, email=form.email.data,
                      password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Thank you for signing up")

    return render_template('index.html', form=form)


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        message = Contact(name=name, email=email, message=message)
        db.session.add(message)
        db.session.commit()
        return render_template('submit.html')


if __name__ == "__main__":
    app.run(debug=True)
