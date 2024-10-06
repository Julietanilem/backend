from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permitir CORS para todas las rutas

# Lista de preguntas y respuestas (puedes agregar más)
questions = [
    {"question": "¿Cuál es el planeta más cercano al sol?", "answer": "Mercurio"},
    {"question": "¿Qué planeta es conocido como el planeta rojo?", "answer": "Marte"},
    {"question": "¿Cuál es el planeta más grande del sistema solar?", "answer": "Júpiter"}
]

@app.route('/')
def home():
    return 'Servidor de preguntas'

# Endpoint para devolver una pregunta aleatoria
@app.route('/get-question', methods=['GET'])
def get_question():
    import random
    question_data = random.choice(questions)
    return jsonify(question_data)  # Retorna la pregunta en formato JSON

if __name__ == '__main__':
    app.run(debug=True)
