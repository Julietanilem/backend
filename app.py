import json
from flask import Flask, jsonify, request
from flask_cors import CORS
import google.generativeai as genai
import os
import random

# Obtener la clave de la variable de entorno
google_api_key = os.getenv('GOOGLE_API_KEY')

# Usar la clave para configurar la API de Gemini
import google.generativeai as genai

genai.configure(api_key=google_api_key)


app = Flask(__name__)
CORS(app)

# Configura tu clave de API de Gemini
GOOGLE_API_KEY = 'AIzaSyBd_4xHAW8v1zkx-t1v571W0Bpq19FojVs'  # Asegúrate de reemplazar esto con tu clave real
genai.configure(api_key=GOOGLE_API_KEY)

# Función para obtener datos del archivo data.json
def get_exoplanet_data():
    try:
        with open("data.json", "r") as json_file:
            data = json.load(json_file)
            indice = random.randint(0, len(data)-1)
            return data[indice]

    except Exception as e:
        print(f"Error al obtener datos del archivo data.json: {str(e)}")
        return None

@app.route('/generate_question')
def generate_question():
    try:
        exoplanet = get_exoplanet_data()
        if not exoplanet:
            return jsonify({"error": "No se encontraron exoplanetas en el archivo."})

        try:
        # Extraer información del exoplaneta
            planet_name = exoplanet['pl_name']
            mass = exoplanet['pl_masse']
            orbital_period = exoplanet['pl_orbper']
            discovery_method = exoplanet['discoverymethod']
            radius = exoplanet['pl_rade']
            year = exoplanet['disc_year']
            location = exoplanet['disc_locale']
            distance = exoplanet['sy_dist']
            status = exoplanet['soltype']  
            stars = exoplanet['sy_snum']
            planets = exoplanet['sy_pnum']
        except Exception as e:
            return jsonify({"error del obtener datos de los planetas": str(e)})

        try:
            # Crear un prompt para el modelo de Gemini
            prompt = f"Genera una pregunta aleatoria sobre cualquier aspecto del exoplaneta {planet_name}, que tiene una masa de {mass} masas de Júpiter, un período orbital de {orbital_period} días, y fue descubierto por el método de {discovery_method}. El exoplaneta tiene un radio de {radius} radios terrestres, "
            prompt +=f"fue descubierto en el año {year} en {location}, y se encuentra a una distancia de {distance} parsecs de la Tierra. El estado del planeta es {status}, y el sistema estelar tiene {stars} estrellas y {planets} planetas." 
            prompt += " Además, que haya tres respuestas, dos incorrectas y una correcta, las respuestas en orden aleatorio también. Debes hacer esto en el formato json siguiente : " 
            prompt += '{ "question": q , "answers": ["answer1", "answer2" , "answer3" ], "correct_answer": a }  en texto plano.Recuerda elegir aspectos variados del planeta, cualquier aspecto suyo. Preguntas diferentes al metodo de descubrimiento'
        except Exception as e:
            return jsonify({"error del leer datos de planetas": str(e)})
        
        try:
            # Generar la pregunta usando Gemini
            model = genai.GenerativeModel('gemini-1.5-flash')  # O gemini-1.5-pro, dependiendo de tu necesidad
            response = model.generate_content(prompt)
            res = response.text  # Extraer el texto de la respuesta
        except Exception as e:
            return jsonify({"error del modelo": str(e)})
        
        try:
            res = res.replace("```json", "").replace("```", "").lstrip()
            res =  json.loads(res)
        except Exception as e:
            return jsonify({"error del parse a json:"+res: str(e)})


        return jsonify(res)

    except Exception as e:
        return jsonify({"error": str(e)})

#procesar respuesta
@app.route('/check-answer', methods=['POST'])
def check_answer():
    data = request.json
    user_answer = data.get('answer', '').strip().lower()
    correct_answer = data.get('correct_answer', '').strip().lower()
    question = data.get('question', '').strip().lower()
    answers = data.get('answers', '')
    

    if user_answer == correct_answer:
        result = "Correcto"
    else:
        result = "Incorrecto"
        
    



    return jsonify({"result":result })

#caso en que solo se entra sin nada
@app.route('/')
def home():
    return jsonify({"message": "¡Bienvenido al generador de preguntas de exoplanetas!"})

if __name__ == '__main__':
    app.run(debug=True)
