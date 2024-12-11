from flask import Flask, render_template
from routes.routes import turno_route

# Intancia de la app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')

app.register_blueprint(turno_route)

if __name__ == '__main__':
    app.run(debug=True)
