from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

def fill_information():

    driver = webdriver.Chrome()
    driver.get("https://envia.co/")

    wait = WebDriverWait(driver, 10)

    popUp = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="popupDialog"]/div/button')))
    popUp.click()

    #Abrir Fomrulario de cotizacion
    btnCotizar = wait.until(EC.element_to_be_clickable((By.ID, 'titulo-cotiza')))
    btnCotizar.click()
    btnPaquete = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'label[for = "paquete"]')))
    btnPaquete.click()
    btnTerrestre = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'label[for = "terrestre"]')))
    btnTerrestre.click()

    #lista de lugar origen
    inpOrigen = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[placeholder="Lugar de origen"]')))
    inpOrigen.click()

    clickOrigen = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.ss-coti-option[data-value="1"]')))
    clickOrigen.click()

    #lista lugar de destino
    inpDestino = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[placeholder="Lugar de destino"]')))
    inpDestino.click()

    clickDestino = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.ss-coti-option[data-value="1016"]')))
    clickDestino.click()

    #forma pago
    btnPago = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'Label[for^="contado-paq"]')))
    btnPago.click()

    #datos paquete
    btnSpan = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="cont-paquete"]/ul/li[3]/label')))
    btnSpan.click()

    inpValor = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[id^="valor-paq"]')))
    inpValor.send_keys("50000")

    inpPeso = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[id^="peso-paq"]')))
    inpPeso.send_keys("10")

    inpAlto = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[id^="alto-paq"]')))
    inpAlto.send_keys("20")

    inpAncho = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[id^="ancho-paq"]')))
    inpAncho.send_keys("15")

    inpLargo = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[id^="largo-paq"]')))
    inpLargo.send_keys("25")

    btnCotizarFinal = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="hbpCotiza"]')))
    btnCotizarFinal.click()
    time.sleep(2)

    return driver

def save_data(driver):
    wait = WebDriverWait(driver,10)

    empresa = 'Envia'
    ciudadElement = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.selectize-input > div[data-value]')))
    ciudadOrigen = ciudadElement[0].text
    ciudadDestino = ciudadElement[1].text
    valorElement = driver.find_element(By.CSS_SELECTOR, 'input[id^="valor-paq"]')
    valorElementFull = re.sub(r"[^0-9.]","",valorElement.get_attribute("value"))
    valor=int(valorElementFull)
    pesoElement = driver.find_element(By.CSS_SELECTOR, 'input[id^="peso-paq"]')
    peso = int(pesoElement.get_attribute("value"))
    altoElement = driver.find_element(By.CSS_SELECTOR, 'input[id^="alto-paq"]')
    alto = int(altoElement.get_attribute("value"))
    anchoElement = driver.find_element(By.CSS_SELECTOR, 'input[id^="ancho-paq"]')
    ancho =int(anchoElement.get_attribute("value"))
    largoElement = driver.find_element(By.CSS_SELECTOR, 'input[id^="largo-paq"]')
    largo = int(largoElement.get_attribute("value"))

    datosCotizacion ={
        "Empresa":empresa,
        "Ciudad Origen":ciudadOrigen,
        "Ciudad Destino":ciudadDestino,
        "Valor Declarado":valor,
        "Peso":peso,
        "Alto":alto,
        "Ancho":ancho,
        "Largo":largo
    }

    print(datosCotizacion)

    valorFleteElement = driver.find_element(By.ID, 'flete2')
    valorFleteFull = re.sub(r"[^0-9.]","",valorFleteElement.text)
    valorFlete = int(valorFleteFull)

    valorFleteVariableElement = driver.find_element(By.ID,'manejo2')
    valorFleteVariabelFull = re.sub(r"[^0-9.]","",valorFleteVariableElement.text)
    valorFleteVariable = int(valorFleteVariabelFull)

    totalElement = driver.find_element(By.ID , 'total-final-paq-terr')
    totalFull = re.sub(r"[^0-9.]","",totalElement.text)
    total = int(totalFull)

    tiempoEntregaElement = driver.find_element(By.ID, 'dias-paq-terr')
    tiempoEntrega = tiempoEntregaElement.text

    resultadosCotizacion ={
        "Valor Flete":valorFlete,
        "Valor Flete Variable":valorFleteVariable,
        "Total":total,
        "Tiempo entrega":tiempoEntrega
    }

    print(resultadosCotizacion)


data = fill_information()
save_data(data)