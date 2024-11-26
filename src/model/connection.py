from pymongo.mongo_client import MongoClient
from env import *

# crear el cliente para conectar a la base de datos
client = MongoClient(uri_bd)

# Obtiene la base de datos desde el cliente y lo almacena en la variable mydb
mydb = client["tuTurno"]

# instancia de la coleccion de productos
miColeccionProductos = mydb["productos"]

# Instancia de coleccion de juegos
miColeccionJuegos = mydb["juegos"]