from wtforms import Form, TextField, PasswordField, validators

class LoginForm(Form):
    username = TextField('username', [validators.Length(min=4, max=25)])
    password = PasswordField('password', [validators.Required(), validators.Length(min=4)])
