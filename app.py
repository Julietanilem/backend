from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

# Habilitar CORS para todas las rutas
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return "¡Bienvenido a mi aplicación Flask con CORS habilitado!"

if __name__ == '__main__':
    app.run()
