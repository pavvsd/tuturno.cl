from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'tuTurno'

mysql = MySQL(app)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/menu/<elemento>', methods = ['POST', 'GET'])
def menu(elemento):
    if str(elemento) == 'cafeteria':
        cur = mysql.connection.cursor()
        cur.execute('SELECT nombre_producto, precio_producto, descripcion_producto, imagen_producto FROM productos WHERE tipo_producto = "cafeteria"')
        lista = cur.fetchall()
        print(lista)
        return render_template('menu.html', cafeteria = lista)
    elif str(elemento) == 'bebestible':
        cur = mysql.connection.cursor()
        cur.execute('SELECT nombre_producto, precio_producto, descripcion_producto, imagen_producto FROM productos WHERE tipo_producto = "bebestible"')
        lista = cur.fetchall()
        print(lista)
        return render_template('menu.html', cafeteria = lista)
    elif str(elemento) == 'pasteleria':
        cur = mysql.connection.cursor()
        cur.execute('SELECT nombre_producto, precio_producto, descripcion_producto, imagen_producto FROM productos WHERE tipo_producto = "pasteleria"')
        lista = cur.fetchall()
        print(lista)
        return render_template('menu.html', cafeteria = lista)
    return render_template('menu.html')
    
@app.route('/ludoteca')
def ludoteca():
    cur = mysql.connection.cursor()
    cur.execute('SELECT nombre_juego, jugadores_juego, edad_juego FROM juegos')
    lista = cur.fetchall()

    return render_template('ludoteca.html', juegos = lista)

@app.route('/ubicacion')
def ubicacion():
    return render_template('ubicacion.html')





if __name__ == '__main__':
    app.run(debug=True)