from pymongo.mongo_client import MongoClient
from configparser import ConfigParser

# Obtengo el archivo .ini
archivo = 'src/settings.ini'

# instancia del .ini
config = ConfigParser()

# leo archivo .ini para traerme las configuraciones de la BBDD
config.read(archivo)

# crear el cliente para conectar a la base de datos
client = MongoClient(config.get('main-bbdd', 'uri'))

# Obtiene la base de datos desde el cliente y lo almacena en la variable mydb
mydb = client[config.get('main-bbdd', 'nombreBD')]

# instancia de la coleccion de productos
miColeccionProductos = mydb[config.get('main-bbdd', 'coleccionProd')]

# Instancia de coleccion de juegos
miColeccionJuegos = mydb[config.get('main-bbdd', 'coleccionJuego')]