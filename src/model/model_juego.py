from database import connection

colJuegos = connection.miColeccionJuegos

def get_juegos():
    juegos = []
    for doc in colJuegos.find().sort("nombre_juego"):
        juegos.append({
            'nombre_juego': doc['nombre_juego'],
            'jugadores_juego': doc['jugadores_juego'],
            'edad_juego': doc['edad_juego']
        })
    return juegos

