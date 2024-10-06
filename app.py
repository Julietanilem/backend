from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app)  # Permitir solicitudes CORS

@app.route('/', methods=['POST'])
def obtener_info_exoplaneta():
    data = request.get_json()
    nombre_exoplaneta = data.get('nombre')
    
    # Hacer el scraping (puedes cambiar la URL y los selectores según tus necesidades)
    url = f'https://ejemplo.com/exoplanetas/{nombre_exoplaneta}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extraer la información deseada
    info = soup.find('div', class_='info-exoplaneta').text
    
    # Devolver la información al frontend
    return jsonify({'nombre': nombre_exoplaneta, 'informacion': info})

if __name__ == '__main__':
    app.run(debug=True)
