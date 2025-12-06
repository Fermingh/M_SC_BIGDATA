from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')

driver = webdriver.Chrome(options=options)

driver.get("https://news.ycombinator.com/")

# Esperar hasta que los elementos estén presentes
wait = WebDriverWait(driver, 10)
titulos = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'span.titleline > a')))

print("Títulos encontrados:")
for titulo in titulos:
    print(titulo.text)

driver.quit()
