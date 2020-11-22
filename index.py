#importamos flask al proyecto, render_template para cargar htmls
from flask import Flask, render_template

#instanciamos flask en app
app = Flask(__name__)

#creamos un ruta a la pagina principal con @app.route('/') y se crea una funcion home
#la funcion home retorna el html principal
@app.route('/')
def login():
    return render_template("login.html")

#crea otra ruta a otra pagina del sitio

#validacion para crear un escucha y decile este es el.
#dubug=True le dice al servidor que entre en modo de pruebas se reiniciara cada vez que cambie algo
if __name__ == '__main__':
    app.run(debug=True)