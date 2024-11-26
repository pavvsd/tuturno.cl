from flask import Flask, render_template
from model import connection

# Intancia de la app
app = Flask(__name__)

def creaListaProductos(productosCol, myquery):
    productos = []
    for doc in productosCol.find(myquery):
            productos.append({
                'nombre_producto': doc['nombre_producto'],
                'valor_producto': doc['valor_producto'],
                'descripcion_producto': doc['descripcion_producto'],
                'foto_producto': doc['foto_producto']
            })
    return productos



@app.route('/')
def home():
    return render_template('index.html')



@app.route('/menu/<elemento>', methods = ['POST', 'GET'])
def menu(elemento):
    productosCol = connection.miColeccionProductos

    if str(elemento) == 'bebestible':
        myquery = { "tipo_producto" : "Bebestible" }

        productos = creaListaProductos(productosCol, myquery)

        return render_template('menu.html', cafeteria = productos)
    
    elif str(elemento) == 'pasteleria':
        myquery = { "tipo_producto" : "Pasteleria" }

        productos = creaListaProductos(productosCol, myquery)

        return render_template('menu.html', cafeteria = productos)
    else:
        myquery = { "tipo_producto" : "Cafeteria" }

        productos = creaListaProductos(productosCol, myquery)
    
    return render_template('menu.html', cafeteria = productos)
    


@app.route('/menu')
def menu2():
    return render_template('index.html')




@app.route('/ludoteca')
def ludoteca():
    juegosCol = connection.miColeccionJuegos
    juegos = []
    for doc in juegosCol.find().sort("nombre_juego"):
        juegos.append({
            'nombre_juego': doc['nombre_juego'],
            'jugadores_juego': doc['jugadores_juego'],
            'edad_juego': doc['edad_juego']
        })
    return render_template('ludoteca.html', juegos = juegos)



@app.route('/ubicacion')
def ubicacion():
    return render_template('ubicacion.html')





if __name__ == '__main__':
    app.run(debug=True)