import firebase_admin
from firebase_admin import credentials
from firebase_admin import db 

cred=credentials.Certificate('firebase-sdk.json')

firebase_admin.initialize_app(cred,{
    'databaseURL':'https://proyectois-47739.firebaseio.com/'
})
'''
ref=db.reference('/')
ref.set({
    'Producto':
    {
        'Queso':{
            'nombre':'Paisa',
            'precio':2,
            'peso':23,

        }
    }
})
'''
#update data
'''
ref= db.reference('Producto')
queso_ref=ref.child('Queso')
queso_ref.update({
    'precio':5
})
'''

#Multiple Update
'''
ref=db.reference('Producto')
ref.update({
    'Queso/peso':25
})
'''
#adding value using push
'''
ref=db.reference('Empleado')
emp_ref=ref.push({
    'nombre':'Miguel',
    'apellido':'Cuadrado',
    'mail':'@gmail',
    'edad':19
})
print(emp_ref.key)
'''

#
ref=db.reference('Producto')
print(ref.get())