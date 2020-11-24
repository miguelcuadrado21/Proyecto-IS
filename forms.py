from wtforms import Form, StringField, TextField
from wtforms.fields.html5 import EmailField
from wtforms import validators
class CommentForm(Form):
    email=EmailField('Correo Electronico')
    password=StringField('Contraseña')