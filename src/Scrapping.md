
# 🕸️ Web Scraping con Python y Selenium  

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)  
![Selenium](https://img.shields.io/badge/Selenium-Automation-brightgreen?logo=selenium&logoColor=white)  
![Web Scraping](https://img.shields.io/badge/WebScraping-Data--Mining-orange?logo=googlechrome&logoColor=white)  

---

## 📌 Introducción  

El **Web Scraping** es una técnica que permite **extraer datos de páginas web** de forma automatizada.  
Mientras que con herramientas como `requests` y `BeautifulSoup` podemos trabajar en sitios estáticos, cuando se trata de **páginas dinámicas con JavaScript**, necesitamos una librería más poderosa: **Selenium**.  

👉 En este ejemplo se trabaja con datos del **catastro en España**, un sitio web que requiere interacción con formularios, pestañas y botones antes de mostrar los resultados.  

📂 El escenario de práctica se encuentra implementado en el repositorio dentro de:  

```

Unidad\_2/src/scrapping/scrapping.py

```

Toda la evidencia de tu trabajo deberá guardarse en el directorio:  

```

work/

```

En particular, la documentación de tu práctica estará en:  

```

work/scenario\_scrapping.md

```

---

## ⚙️ ¿Por qué usar Selenium?  

Selenium fue creado originalmente para **automatizar pruebas en aplicaciones web**, pero su capacidad de **simular la interacción de un usuario real** (clicks, scroll, input de texto, etc.) lo convierte en una herramienta clave para el **web scraping en entornos dinámicos**.  

Ventajas:  
- 🖱️ **Clicks automáticos** en botones, enlaces y menús.  
- ⌨️ Introducción de **texto en formularios**.  
- 🌐 Manejo de **cookies, pop-ups y banners de privacidad**.  
- 🕵️‍♂️ Acceso a **contenido cargado dinámicamente con JavaScript**.  

---

## 🛠️ Requisitos básicos  

Antes de comenzar, necesitas:  

1. **Google Chrome** instalado en tu computadora.  
2. La librería **Selenium** (`pip install selenium`).  
3. El **controlador Chromedriver**, que puede automatizarse con `chromedriver_autoinstaller`.  

---

## 🚀 Flujo de trabajo  

El proceso típico de scraping con Selenium sigue estos pasos:  

1. **Abrir navegador**: iniciar una sesión de Chrome desde Python.  
2. **Cargar página web**: navegar a la URL objetivo.  
3. **Aceptar cookies / pop-ups**: si es necesario, interactuar con el banner inicial.  
4. **Interactuar con la página**: seleccionar pestañas, introducir coordenadas o llenar formularios.  
5. **Extraer información**: localizar elementos mediante `XPATH`, `ID`, `NAME` o `CSS Selectors`.  
6. **Procesar y almacenar datos**: guardar resultados en **CSV, Excel o bases de datos**.  

---

## 📒 Escenario Scrapping

1. **Explorar el código en `scrapping.py`**:  
   - Revisa cómo se abre el navegador y se carga la página del catastro.  
   - Identifica cómo se aceptan las cookies.  
   - Comprueba la interacción con pestañas y formularios.  

2. **Ejecutar el script**:  
   - Corre el archivo y valida que se abre el navegador.  
   - Introduce coordenadas de prueba y extrae datos.  

3. **Documentar el proceso**:  
   - Describe cada etapa en `work/scenario_scrapping.md`.  
   - Incluye capturas de pantalla y resultados obtenidos.  

4. **Guardar evidencia**:  
   - Almacena todos los archivos de salida y notas en el directorio `work`.  

---

## 🔍 Ejemplo práctico de WebScrapping

El ejemplo mostrado abre el portal catastral, selecciona la pestaña **"Coordenadas"**, introduce una latitud y longitud, y finalmente obtiene información como:  

- 📍 **Referencia catastral**  
- 🏢 **Uso principal del inmueble**  
- 📐 **Superficie construida**  
- 🗓️ **Año de construcción**  

Este tipo de scraping es útil para proyectos de **Big Data**, estudios urbanos o análisis de propiedades.  

---

## 📚 Lecturas adicionales  

Para reforzar tu aprendizaje, revisa estas lecturas:  

1. [📖 Documentación oficial de Selenium](https://www.selenium.dev/documentation/)  
2. [🐍 Web Scraping con Python (Real Python)](https://realpython.com/beautiful-soup-web-scraper-python/)  
3. [⚡ Web Scraping con Selenium en Python (GeeksForGeeks)](https://www.geeksforgeeks.org/selenium-python-tutorial/)  

 

> 💡 Recuerda que el **web scraping debe usarse de forma ética y legal**, respetando las políticas de uso de cada sitio web.  

---
