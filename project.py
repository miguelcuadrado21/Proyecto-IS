from wtforms import Form, StringField, TextField
from wtforms.fields.html5 import EmailField
from wtforms import validators
class AgregarProducto(Form):
    nombre=StringField('Nombre')
    codigo=StringField('Codigo')
    precio=StringField('Precio')
    cantidad=StringField('Cantidad (KG)')
    dia_vencimiento=StringField('Dia de Vencimiento')
    mes_vencimiento=StringField('Mes de Vencimiento')
    ano_vencimiento=StringField('Año de Vencimiento')   