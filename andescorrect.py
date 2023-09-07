import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

url = 'https://www.losandes.com.pe'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encuentra todos los elementos con la clase "jeg_post_title" (títulos)
    titles = soup.find_all(class_='jeg_post_title')

    # Encuentra todos los elementos con la clase "jeg_meta_date" (fechas)
    dates = soup.find_all(class_='jeg_meta_date')

    # Verifica que haya títulos y fechas disponibles
    if titles and dates:
        # Abre un archivo CSV para escribir
        with open('losandesoficial.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
            archivo = csv.writer(csvfile, delimiter=';')

            # Escribe el encabezado del CSV
            archivo.writerow(['TITULO', 'FECHA'])

            # Itera a través de los títulos y fechas y escribe en el CSV
            for title, date in zip(titles, dates):
                titulo_texto = title.get_text(strip=True)
                fecha_texto = date.get_text(strip=True)

                if titulo_texto:  # Verifica que el título no esté vacío
                    # Ajusta el formato de la fecha
                    fecha_texto = fecha_texto.replace('Enero', 'January').replace('Febrero', 'February').replace('Marzo', 'March').replace('Abril', 'April').replace('Mayo', 'May').replace('Junio', 'June').replace('Julio', 'July').replace('Agosto', 'August').replace('Septiembre', 'September').replace('Octubre', 'October').replace('Noviembre', 'November').replace('Diciembre', 'December')
                    fecha_objeto = datetime.strptime(fecha_texto, '%d %B, %Y')
                    fecha_formateada = fecha_objeto.strftime('%Y-%m-%d')

                    archivo.writerow([titulo_texto, fecha_formateada])

        print("Archivo CSV creado correctamente.")
    else:
        print("No se encontraron títulos o fechas en la página.")
else:
    print("No se pudo acceder a la página:", response.status_code)