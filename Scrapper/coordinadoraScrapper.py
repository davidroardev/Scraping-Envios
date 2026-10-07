from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# --- CONFIGURACIÓN DEL NAVEGADOR ---
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # ventana grande
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
# si quieres verlo visualmente, no pongas headless
# chrome_options.add_argument("--headless")

# Ruta del driver (ajústala si lo tienes en otro lugar)
service = Service("chromedriver.exe")

driver = webdriver.Chrome(options=chrome_options)

try:
    # --- ABRIR LA PÁGINA ---
    url = "https://coordinadora.com/envios/cotizar-un-envio/"
    driver.get(url)

    # --- ESPERAR Y ABRIR EL COTIZADOR ---
    wait = WebDriverWait(driver, 20)
    
    div_cotizador = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class = 'rgc_widget_envios']")))
    driver.execute_script("window.scrollBy(0, 250);")
                
    #Mover raton hacia div de cotizacion:
    actions = ActionChains(driver)
    actions.move_to_element(div_cotizador).perform()
    driver.execute_script("arguments[0].click();",div_cotizador)
    time.sleep(2)

    #Click en Nacional
    elemento_nacional = wait.until(EC.element_to_be_clickable((By.ID, "nacional")))
    driver.execute_script("arguments[0].click();", elemento_nacional)

    #Click en Ciudad origen
    campo_destino = wait.until(EC.element_to_be_clickable((By.NAME, "ciudadDestino")))
    driver.execute_script("arguments[0].click();", campo_destino)

    # --- LIMPIAR Y ESCRIBIR LA CIUDAD ---
    campo_destino.clear()
    campo_destino.send_keys("Cucuta")  # sin el (Ant)
    ciudad_click = 'Cucuta (N/stder)'
    time.sleep(2)  # espera que aparezcan las sugerencias

    opcion_ciudad = wait.until(EC.element_to_be_clickable((By.XPATH,f"//button[normalize-space(text())='{ciudad_click}']")))
    driver.execute_script("arguments[0].click();", opcion_ciudad)

    # --- OBTENER HTML COMPLETO PARA ANALIZAR ---
    html_completo = driver.page_source

    # --- GUARDARLO EN UN ARCHIVO ---
    with open("pagina_coordinadora.html", "w", encoding="utf-8") as f:
        f.write(html_completo)

    print("✅ HTML guardado como 'pagina_coordinadora.html'")

    # --- OPCIONAL: mantener el navegador abierto para inspección ---
    time.sleep(5)

finally:
    driver.quit()