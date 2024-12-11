from database import connection

colProductos = connection.miColeccionProductos

def creaListaProductos(query):
    productos = []
    for doc in colProductos.find(query):
            productos.append({
                'nombre_producto': doc['nombre_producto'],
                'valor_producto': doc['valor_producto'],
                'descripcion_producto': doc['descripcion_producto'],
                'foto_producto': doc['foto_producto']
            })
    return productos







