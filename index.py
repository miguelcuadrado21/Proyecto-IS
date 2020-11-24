#importamos flask al proyecto, render_template para cargar htmls
from flask import Flask, render_template
from wtforms import Form, StringField, TextField
from wtforms.fields.html5 import EmailField
from flask import request
import forms
import pyrebase
import firebase_admin
from firebase_admin import credentials, auth
from firebase_admin import db
import json
import requests
from requests import Session
from requests.exceptions import HTTPError
#instanciamos flask en app
app = Flask(__name__)


#DB Init
firebaseConfig={
    "apiKey": "AIzaSyDhw83XTyUu58dOB7M1pCbT5olzakeNUqE",
    "authDomain": "proyectois-47739.firebaseapp.com",
    "databaseURL": "https://proyectois-47739.firebaseio.com",
    "projectId": "proyectois-47739",
    "storageBucket": "proyectois-47739.appspot.com",
    "messagingSenderId": "677768606392",
    "appId": "1:677768606392:web:a1225eb634ab25f416ba4d",
    "measurementId": "G-BEMJ6TR440"
}
cred = credentials.Certificate("firebase-sdk.json")
firebase=pyrebase.initialize_app(firebaseConfig)
au=firebase.auth()
#creamos un ruta a la pagina principal con @app.route('/') y se crea una funcion home
#la funcion home retorna el html principal

@app.route('/',methods=['GET','POST'])
def login():
    comment_form=forms.CommentForm(request.form)
    if request.method=='POST':
        try:
            au.sign_in_with_email_and_password(comment_form.email.data,comment_form.password.data)
            print("Login Exitoso") 
            return render_template("gestion-productos.html") 
        except:
            print("Correo o Contraseña invalido")
    return render_template("login.html",form=comment_form)

@app.route('/gestionProductos')
def gestionProductos():
    return render_template("gestion-productos.html") 

@app.route('/agregarProducto')
def agregarProducto():
    return render_template("agregar-producto.html")  

@app.route('/moficarProducto')
def modificarProducto():
    return render_template("modificar-producto.html")           

#crea otra ruta a otra pagina del sitio

#validacion para crear un escucha y decile este es el.
#dubug=True le dice al servidor que entre en modo de pruebas se reiniciara cada vez que cambie algo
if __name__ == '__main__':
    app.run(debug=True)