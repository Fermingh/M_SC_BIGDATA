import requests
from bs4 import BeautifulSoup
import time
import random
import csv # <--- NUEVA LIBRERÍA IMPORTADA

# --- CONFIGURACIÓN ÉTICA Y DE URL ---
URL_BASE = 'http://books.toscrape.com/'
HEADERS = {
    'User-Agent': 'MiScraperEticoLibros/1.0 (Para uso educativo, no comercial)',
    'Accept-Language': 'es-ES,es;q=0.9',
}
MIN_DELAY = 3
MAX_DELAY = 6
NOMBRE_ARCHIVO_CSV = 'libros_extraidos.csv' # <--- NOMBRE DEL ARCHIVO DE SALIDA


def realizar_scraping_pagina(url):
    """Realiza la solicitud y extrae datos de una sola página."""
    try:
        print(f"-> Solicitando URL: {url}")
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status() 
        
        soup = BeautifulSoup(response.text, 'html.parser')
        libros_extraidos = []
        
        articulos_libros = soup.find_all('article', class_='product_pod')
        
        for articulo in articulos_libros:
            titulo = articulo.find('h3').find('a').get('title')
            precio = articulo.find('p', class_='price_color').text.strip()
            
            # NOTA: Los precios incluyen símbolos de moneda, es mejor limpiarlos si se van a usar en cálculos
            # Ejemplo: Quitar el símbolo '£'
            precio_limpio = precio.replace('£', '')
            
            libros_extraidos.append({'titulo': titulo, 'precio': precio_limpio})
            
        return libros_extraidos
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Error al conectar o en la respuesta: {e}")
        return []

# ----------------------------------------------------
#               FUNCIÓN PARA GUARDAR CSV
# ----------------------------------------------------
def guardar_a_csv(datos, nombre_archivo):
    """Guarda una lista de diccionarios en un archivo CSV."""
    if not datos:
        print("⚠️ No hay datos para guardar.")
        return

    # Usamos las claves del primer diccionario como encabezados
    encabezados = datos[0].keys()

    try:
        # Abrimos el archivo en modo escritura ('w', de write)
        # newline='' evita que se inserten filas en blanco entre registros
        with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo_csv:
            # Creamos un escritor de diccionarios
            escritor = csv.DictWriter(archivo_csv, fieldnames=encabezados, delimiter=';')
            
            # Escribimos los encabezados (la primera fila)
            escritor.writeheader()
            
            # Escribimos todas las filas de datos
            escritor.writerows(datos)

        print(f"\n✅ Datos guardados con éxito en: **{nombre_archivo}**")

    except IOError:
        print(f"❌ Error de I/O al intentar guardar el archivo {nombre_archivo}")
# ----------------------------------------------------


def scraper_principal():
    """Función principal que maneja la navegación y los retrasos."""
    todos_los_libros = []
    pagina_actual = 1
    
    # Limitamos a 3 páginas para la demostración
    MAX_PAGINAS_A_SCRAPEAR = 3 
    
    while pagina_actual <= MAX_PAGINAS_A_SCRAPEAR:
        # Lógica para construir la URL de cada página
        if pagina_actual == 1:
            url = URL_BASE + 'index.html'
        else:
            # Ejemplo de paginación para las siguientes páginas
            url = URL_BASE + f'catalogue/page-{pagina_actual}.html'
            
        # Implementación del retraso ético
        if pagina_actual > 1:
            sleep_time = random.uniform(MIN_DELAY, MAX_DELAY)
            print(f"\n--- Esperando éticamente: {sleep_time:.2f} segundos ---")
            time.sleep(sleep_time)
        
        datos_pagina = realizar_scraping_pagina(url)
        todos_los_libros.extend(datos_pagina)
        
        pagina_actual += 1

    # Llama a la nueva función para guardar los datos
    guardar_a_csv(todos_los_libros, NOMBRE_ARCHIVO_CSV)


if __name__ == '__main__':
    scraper_principal()