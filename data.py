import requests
import json


url = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+pl_name,pl_masse,pl_rade,discoverymethod,disc_year,disc_locale,sy_dist,soltype,pl_orbper,sy_snum,sy_pnum+from+ps&format=json"


response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    with open("data.json", "w") as json_file:
        json.dump(data, json_file, indent=4)

    print("Datos guardados en data.json exitosamente.")
else:
    print(f"Error al realizar la solicitud. Código de estado: {response.status_code}")

'''
Obtenemos 
pl_name: Nombre del exoplaneta.

pl_masse: Masa del exoplaneta en relación a la masa de la Tierra.

pl_rade: Radio del exoplaneta en relación al radio de la Tierra.

discoverymethod: Método de descubrimiento utilizado para detectar el exoplaneta.

disc_year: Año en que el exoplaneta fue descubierto.

disc_locale: Lugar u observatorio desde donde fue descubierto el exoplaneta.

sy_dist: Distancia del sistema estelar al sistema solar en parsecs.

soltype: Estado o la categoría en la que el planeta se encuentra, basándose en la calidad y cantidad de los datos obtenidos para ese planeta.

pl_orbper: Período orbital del exoplaneta (el tiempo que tarda en completar una órbita alrededor de su estrella) en días.

sy_snum: Número de estrellas en el sistema.

sy_pnum: Número de planetas en el sistema.

'''