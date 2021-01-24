#importamos flask al proyecto, render_template para cargar htmls
from flask import Flask, render_template, url_for, redirect
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
import project
#instanciamos flask en app
app = Flask(__name__)


#Inicializamos la Base de Datos
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
db=firebase.database()

#creamos un ruta a la pagina principal con @app.route('/') y se crea una funcion home
#la funcion home retorna el html principal

#Login de la App
@app.route('/',methods=['GET','POST'])
def login():
    #Guarda los datos ingresados en el Formulario
    comment_form=forms.CommentForm(request.form)
    if request.method=='POST':
        try:
            #autenticamos el usuario
            user=au.sign_in_with_email_and_password(comment_form.email.data,comment_form.password.data)
            print("Login Exitoso") 
            return redirect(url_for('main'))
        except:
            print("Correo o Contraseña invalido")
    return render_template("login.html",form=comment_form)

@app.route('/gestionProductos',methods=['GET','POST'])
def gestionProductos():
    #Guarda los datos ingresados en el formulario
    gest_form=forms.GestionProducto(request.form)
    productos=db.get()
    if request.method=='POST':
        for item in productos.each():
            if gest_form.nombre.data==item.key():
                
                return render_template("busqueda.html",prod=item.key(),db=db,data=productos)
    return render_template("gestion-productos.html",data=productos,db=db,form=gest_form) 


@app.route('/agregarProducto',methods=['GET','POST'])
def agregarProducto():
    #Guarda los datos ingresados en el formulario
    add_product=forms.AgregarProducto(request.form)
    #Ingresa los datos del formulario en la variable  data
    if request.method=='POST':
       data={'ANombre':add_product.nombre.data,
             'BCodigo':add_product.codigo.data,
             'CPrecio':add_product.precio.data,
             'DCantidad':add_product.cantidad.data,
             'EDia':add_product.dia_vencimiento.data,
             'FMes':add_product.mes_vencimiento.data, 
             'GAño':add_product.ano_vencimiento.data,    
            }
        #Inserta en la Base de Datos
       db.child(add_product.nombre.data).set(data)
       return render_template("agregar-producto.html", form=add_product)
    return render_template("agregar-producto.html",form=add_product)  

       


@app.route('/agregarUsuario',methods=['GET','POST'])
def agregarUsuario():
    add_user=forms.CommentForm(request.form)
    if request.method=='POST':
        try:
            user=au.create_user_with_email_and_password(add_user.email.data,add_user.password.data)
            return redirect(url_for('gestionProductos'))
        except:
            return render_template("agregar-usuario.html",form=add_user)
    return render_template("agregar-usuario.html",form=add_user)

@app.route('/main')
def main():
    return render_template("mainmenu.html")

@app.route('/reset',methods=['GET','POST'])
def reset():
    comment_form=forms.CommentForm(request.form)
    if request.method=='POST':
        try:
            #autenticamos el usuario
            print(comment_form.email.data)
            user=au.send_password_reset_email(comment_form.email.data)
            return redirect(url_for('login'))
        except:
            print("Correo o Contraseña invalido")
    return render_template("recuperar-contraseña.html",form=comment_form)
#crea otra ruta a otra pagina del sitio
@app.route('/eliminar/<id>')
def eliminar(id):
    db.child(id).remove()
    return redirect(url_for('gestionProductos'))

@app.route('/editar/<id>',methods=["GET","POST"])
def editar(id):
    productos=db.get()
    add_product=forms.AgregarProducto(request.form)
    #Ingresa los datos del formulario en la variable  data
    if request.method=='POST':
       data={'ANombre':add_product.nombre.data,
             'BCodigo':add_product.codigo.data,
             'CPrecio':add_product.precio.data,
             'DCantidad':add_product.cantidad.data,
             'EDia':add_product.dia_vencimiento.data,
             'FMes':add_product.mes_vencimiento.data, 
             'GAño':add_product.ano_vencimiento.data,    
            }
        #Inserta en la Base de Datos
       db.child(add_product.nombre.data).set(data)
       return redirect(url_for('gestionProductos'))

    return render_template("editar-producto.html",form=add_product,id=id,db=db,data=productos)

#validacion para crear un escucha y decile este es el.
#dubug=True le dice al servidor que entre en modo de pruebas se reiniciara cada vez que cambie algo
if __name__ == '__main__':
    app.run(debug=True)