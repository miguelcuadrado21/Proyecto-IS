from wtforms import Form, StringField, TextField,PasswordField,validators
from wtforms.fields.html5 import EmailField
from wtforms import validators
class CommentForm(Form):
    email=EmailField('Correo Electronico')
    password=PasswordField('Contraseña')

class AgregarProducto(Form):
    nombre=StringField('Nombre')
    codigo=StringField('Codigo')
    precio=StringField('Precio')
    cantidad=StringField('Cantidad (KG)')
    dia_vencimiento=StringField('Dia de Vencimiento')
    mes_vencimiento=StringField('Mes de Vencimiento')
    ano_vencimiento=StringField('Año de Vencimiento')   
class GestionProducto(Form):
    nombre=StringField('Nombre')
    codigo=StringField('Codigo')
