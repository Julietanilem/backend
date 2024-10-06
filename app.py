from flask import Flask, jsonify, request
from flask_cors import CORS
import random

app = Flask(__name__)

# Permitir CORS para todas las rutas y todos los orígenes
CORS(app)  # Esto permite CORS para todos los orígenes

# Lista de preguntas y respuestas
questions = [
    {"question": "¿Cuál es el planeta más cercano al sol?", "answer": "Mercurio"},
    {"question": "¿Qué planeta es conocido como el planeta rojo?", "answer": "Marte"},
    {"question": "¿Cuál es el planeta más grande del sistema solar?", "answer": "Júpiter"}
]

@app.route('/')
def home():
    return 'Servidor de preguntas'

@app.route('/get-question', methods=['GET'])
def get_question():
    question_data = random.choice(questions)
    return jsonify(question_data)

@app.route('/check-answer', methods=['POST'])
def check_answer():
    data = request.get_json()
    user_answer = data.get('answer', '').strip()
    correct_answer = data.get('correct_answer', '').strip()

    if user_answer.lower() == correct_answer.lower():
        return jsonify({'result': 'correcto'})
    else:
        return jsonify({'result': 'incorrecto'})

if __name__ == '__main__':
    app.run(debug=True)
