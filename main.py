from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = "________"
Bootstrap(app=app)


@app.route("/")
def home_page():
    return render_template('index.html')

class MyForm(FlaskForm):
    email = EmailField(label='Email', validators=[DataRequired(), Email(granular_message=True)])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8, message="Field must be at least 8 characters long.")])
    submit = SubmitField(label="Log In")

@app.route('/login', methods=['GET', 'POST'])
def get_login_page():
    form = MyForm()
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)