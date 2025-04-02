from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#CASO AUTOMATIZADO 1

class SelectFlight:
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

    def seleccion_vuelo(self):
        #Abrir la seleccion de tarifas de vuelo.
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='journeyFare_3432344634373745343334433446374533393336333933343745343135363745333233303332333532443330333532443330333137453335333333343335333433373332343433343331333533363333333933333336333333393333333433323434333433323334343633343337333433333334343333343436333234343333333233333330333333323333333533323434333333303333333533323434333333303333333133323434333333303333333633333335333333357E33313339']/journey-control-custom/div/div/div[1]/div[2]/button"))).click()            
        #Seleccionar la tarifa basic.
        select_fare = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='journeyFare_3432344634373745343334433446374533393336333933343745343135363745333233303332333532443330333532443330333137453335333333343335333433373332343433343331333533363333333933333336333333393333333433323434333433323334343633343337333433333334343333343436333234343333333233333330333333323333333533323434333333303333333533323434333333303333333133323434333333303333333633333335333333357E33313339']/journey-control-custom/div/div/div[2]/div/div/div/div[1]/fare-control/div/div[3]/button")))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", select_fare)
        time.sleep(2)
        
        select_fare.click()
        self.save_screenshot("C:/Users/LuisYánezMalavé/Pictures/Screenshots/vuelo_seleccionado.png") 

    def continuar_btn(self):
        self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "page-loader")))
        self.click_element("//*[@id='maincontent']/div/div[2]/div/div/button-container/div/div/button")
