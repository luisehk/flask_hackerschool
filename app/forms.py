from flask_wtf import Form
from wtforms import StringField, TextAreaField, validators


class MessageForm(Form):
    author = StringField('Nombre', validators=[validators.DataRequired()])
    body = TextAreaField('Mensaje', validators=[validators.DataRequired()])
