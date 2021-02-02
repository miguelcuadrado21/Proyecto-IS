from wtforms import Form, StringField, TextField,PasswordField,validators
from wtforms.fields.html5 import EmailField, IntegerField, DecimalField
from wtforms import validators
from wtforms.validators import DataRequired,NumberRange,InputRequired
class CommentForm(Form):
    email=EmailField(label='Correo Electronico',validators=[ DataRequired()])
    password=PasswordField(label='Contraseña',validators=[ DataRequired()])

class AgregarProducto(Form):
    nombre=StringField('Nombre',[ InputRequired()])
    codigo=IntegerField('Codigo',[ DataRequired(), NumberRange(min=0,max=None,message='Debe ser mayor a 0')])
    precio=StringField('Precio (Decimales: xx.xx)',validators=[ DataRequired(), NumberRange(min=0,max=None)])
    cantidad=StringField('Cantidad (KG) (Decimales: xx.xx)',validators=[ DataRequired(), NumberRange(min=0,max=None)])
    dia_vencimiento=IntegerField('Dia de Vencimiento',validators=[ InputRequired(), NumberRange(min=1,max=31)])
    mes_vencimiento=IntegerField('Mes de Vencimiento',validators=[ DataRequired(), NumberRange(min=1,max=12)])
    ano_vencimiento=IntegerField('Año de Vencimiento',validators=[ DataRequired(), NumberRange(min=2021,max=None)])   
class GestionProducto(Form):
    nombre=StringField('Nombre')
    codigo=StringField('Codigo')
class AgregarOferta(Form):
    nombre=StringField('Nombre')
    oferta=IntegerField('Oferta (descuento)',[DataRequired(), NumberRange(min=1,max=100,message='Debe estar entre 1 y 100')])
