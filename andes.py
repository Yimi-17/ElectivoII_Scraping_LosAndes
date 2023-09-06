import requests
from bs4 import BeautifulSoup

# URL de la página de noticias
url = 'https://www.losandes.com.pe/'

# Realiza una solicitud GET a la URL
response = requests.get(url)

# Verifica si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Parsea el contenido HTML con BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encuentra los elementos <div> con la clase 'jeg_heroblock_wrapper'
    divs = soup.find_all('div', class_='jeg_heroblock_wrapper')

    # Itera sobre los elementos <div> y encuentra los títulos <h2> dentro de cada uno
    for div in divs:
        # Encuentra los títulos <h2> dentro del <div>
        titulos = div.find_all('h2')
        fechas = div.find_all('i', class_='fa fa-clock-o')

        # Itera sobre los títulos y los imprime
        for titulo, fecha in zip(titulos, fechas):
            titulo_texto = titulo.text.strip()
            fecha_texto = fecha.next_sibling.strip()  # Obtener el texto del hermano siguiente del <i>
            print("Título:", titulo_texto)
            print("Fecha:", fecha_texto)
            print()


else:
    print(f"Error al acceder a la página. Código de estado: {response.status_code}")