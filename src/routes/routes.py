from flask import Blueprint, render_template
from model.model_juego import get_juegos
from model.model_producto import creaListaProductos

turno_route = Blueprint('tuturno', __name__, url_prefix='/tuturno')

@turno_route.route('/menu/<elemento>', methods = ['POST', 'GET'])
def menu(elemento):

    if str(elemento) == 'bebestible':
        myquery = { "tipo_producto" : "Bebestible" }
        productos = creaListaProductos(myquery)
        return render_template('menu.html', cafeteria = productos)
    
    elif str(elemento) == 'pasteleria':
        myquery = { "tipo_producto" : "Pasteleria" }
        productos = creaListaProductos(myquery)
        return render_template('menu.html', cafeteria = productos)
    
    else:
        myquery = { "tipo_producto" : "Cafeteria" }
        productos = creaListaProductos(myquery)

    pagina = 'menu'
    return render_template('menu.html', cafeteria = productos, pagina = pagina)

@turno_route.route('/menu')
def menu2():
    return menu('cafeteria')

@turno_route.route('/ludoteca')
def ludoteca():
    juegos = get_juegos()
    pagina = 'ludoteca'
    return render_template('ludoteca.html', juegos = juegos, pagina = pagina)

@turno_route.route('/ubicacion')
def ubicacion():
    pagina = 'ubicacion'
    return render_template('ubicacion.html', pagina = pagina)

