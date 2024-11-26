from pymongo.mongo_client import MongoClient

# Configura url del server mongo
uri = "mongodb+srv://tuturno:admin@cluster0.ltinoxz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# crear el cliente para conectar a la base de datos
client = MongoClient(uri)

# Obtiene la base de datos desde el cliente y lo almacena en la variable mydb
mydb = client["tuTurno"]

# instancia de la coleccion de productos
miColeccionProductos = mydb["productos"]

# Instancia de coleccion de juegos
miColeccionJuegos = mydb["juegos"]