import csv
import json
import time
import random
from datetime import datetime
 
# Definir las rutas de los archivos de entrada y salida
input_csv = 'critic_reviews.csv'
output_json = 'critic\\critic.json'
 
# Abrir el archivo CSV
with open(input_csv, mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
   
    # Abrir el archivo JSON en modo escritura
    with open(output_json, mode='w', encoding='utf-8') as json_file:
        for row in csv_reader:
            # Añadir timestamp a cada registro
            row['@timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
           
            json.dump(row, json_file, ensure_ascii=False)
            json_file.write('\n')  # Escribir cada JSON en una nueva línea
            json_file.flush()  # Asegurarse de que se escriba en el archivo inmediatamente
           