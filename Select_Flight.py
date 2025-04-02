from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#CASO AUTOMATIZADO 2

class Select_Flight:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_element(self, xpath):
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath))) #Espera que los elementos sean interactivo antes de dar click.
        element.click() #Clica en los elementos.

    def send_keys(self, xpath, keys):
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath))) #Localiza los elementos.
        element.send_keys(keys) #Ingresa informacion en los input.

    def save_screenshot(self, path):
        self.driver.save_screenshot(path) #Realiza la captura de pantalla.
        print(f"Captura guardada en: {path}") #Imprime el mensaje de la captura guardada.

    def vuelo_ida(self):
        #Abrir la seleccion de tarifas de vuelo ida.
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/main/div/div[2]/div/div/journey-availability-select-container/div/price-journey-select-custom/div[2]/div[2]/div[1]/journey-control-custom/div/div/div[1]/div[2]/button"))).click()
        #Seleccionar la tarifa basic.
        vuelo_ida = self.wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/main/div/div[2]/div/div/journey-availability-select-container/div/price-journey-select-custom/div[2]/div[2]/div[1]/journey-control-custom/div/div/div[2]/div/div/div/div[1]/fare-control/div/div[3]/button")))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", vuelo_ida)
        time.sleep(1)
        vuelo_ida.click()

    def vuelo_vuelta(self):
        self.wait = WebDriverWait(self.driver, 20)
        # Abrir la selección de tarifas vuelo vuelta.
        fare = self.wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/main/div/div[2]/div/div/journey-availability-select-container/div[2]/price-journey-select-custom/div[2]/div[2]/div[1]/journey-control-custom/div/div/div[1]/div[2]/button")))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", fare)
        time.sleep(1)
        fare.click()  # Se debe invocar la función click

        # Seleccionar la tarifa flex.
        vuelo_vuelta = self.wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/main/div/div[2]/div/div/journey-availability-select-container/div[2]/price-journey-select-custom/div[2]/div[2]/div[1]/journey-control-custom/div/div/div[2]/div/div/div/div[3]/fare-control/div/div[3]/button")))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", vuelo_vuelta)
        time.sleep(1)
        vuelo_vuelta.click()

    def continuar(self):
        self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "page-loader")))
        self.click_element("//*[@id='maincontent']/div/div[2]/div/div/button-container/div/div/button")

