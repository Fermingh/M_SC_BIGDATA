***

## Práctica de Scraping con Selenium, Python y Chrome

### Requisitos previos

- Instala Python 3.x
- Instala Google Chrome.
- Descarga el ChromeDriver correspondiente a tu versión de Chrome: [Descargar ChromeDriver](https://chromedriver.chromium.org/downloads).
- Instala la librería Selenium:

```bash
pip install selenium
```


***

### Paso a paso

#### 1. Crear el entorno y archivo .py

1. Abre tu editor y crea un archivo llamado `scraping_selenium_hn.py`.
2. Coloca el archivo ChromeDriver en el directorio de trabajo o asegúrate de que esté en el PATH.

***

#### 2. Código con comentarios línea a línea

```python
# Importamos las librerías necesarias para Selenium y manejo de esperas
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuramos opciones de Chrome, aquí se abre maximizado
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')

# Inicializamos el driver de Chrome con las opciones configuradas
driver = webdriver.Chrome(options=options)

# Abrimos la página de Hacker News
driver.get("https://news.ycombinator.com/")

# Esperamos hasta que los títulos de las noticias estén presentes en la página (máximo 10 segundos)
wait = WebDriverWait(driver, 10)
titulos = wait.until(
    EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, 'span.titleline > a')
    )
)

# Imprimimos los textos (titulos) de cada elemento encontrado
print("Títulos encontrados:")
for titulo in titulos:
    print(titulo.text)

# Cerramos el navegador y liberamos recursos
driver.quit()
```


***

### Explicación de cada paso

- **Importar librerías:** Permite utilizar WebDriver, elegir selectores CSS y utilizar funciones para esperar elementos en la página.
- **Configurar Chrome:** El navegador se abre en modo visual, útil para depuración.
- **Inicializar WebDriver:** Es el motor de Selenium que controla Chrome.
- **Abrir página objetivo:** El navegador navega a la URL indicada.
- **Esperar elementos:** El script espera hasta que los titulares sean visibles antes de proceder, evitando obtener listas vacías.
- **Imprimir resultados:** Se muestran los titulares recopilados en la consola.
- **Cerrar navegador:** Finaliza la sesión para no dejar procesos abiertos.

***

>Otro ejemplo controlado se muestra a continuación

5 ideas de scraping propuestas para el entorno público de Moodle en [enlinea.tecmm.mx], estructuradas como ejemplos orientativos. Los selectores deben ajustarse según la inspección directa en el frontend real del sitio.

***

## 1. Listado de cursos públicos

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://enlinea.tecmm.mx/moodle/course/index.php")

# Selector ejemplo, puedes inspeccionar el sitio y ajustar
cursos = driver.find_elements(By.CSS_SELECTOR, ".coursename a")
for curso in cursos:
    print(curso.text)

driver.quit()
```


***

## 2. Extracción de categorías académicas

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://enlinea.tecmm.mx/moodle/course/index.php")

categorias = driver.find_elements(By.CSS_SELECTOR, ".categoryname")
for categoria in categorias:
    print(categoria.text)

driver.quit()
```


***

## 3. Recolección de títulos de foros públicos

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://enlinea.tecmm.mx/moodle/mod/forum/index.php") # puede requerir ajustar ruta

# Selector ejemplo
foros = driver.find_elements(By.CSS_SELECTOR, ".forumname a")
for foro in foros:
    print(foro.text)

driver.quit()
```


***

## 4. Listar documentos de los cursos abiertos

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://enlinea.tecmm.mx/moodle/course/index.php")

# Selector ejemplo para archivos públicos
documentos = driver.find_elements(By.CSS_SELECTOR, ".activity.resource .instancename a")
for doc in documentos:
    print(doc.text)

driver.quit()
```


***

## 5. Catalogar actividades abiertas

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://enlinea.tecmm.mx/moodle/course/index.php")

actividades = driver.find_elements(By.CSS_SELECTOR, ".activity .instancename")
for actividad in actividades:
    print(actividad.text)

driver.quit()
```


***

> **Ajusta los selectores CSS según los elementos que observes con la herramienta de inspección del navegador, ya que los nombres de clase pueden variar según la plantilla actual de Moodle utilizada en TecMM. Todos los scripts se ejecutan en entradas públicas, sin login ni acceso a datos personales.**