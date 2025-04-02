from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#CASO AUTOMATIZADO 7
class URL_Footer:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_element(self, xpath):
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath))) #Espera que los elementos sean interactivo antes de dar click.
        element.click() #Clica en los elementos.

    def send_keys(self, xpath, keys):
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath))) #Localiza los elementos.

    def save_screenshot(self, path):
        self.driver.save_screenshot(path) #Realiza la captura de pantalla.
        print(f"Captura guardada en: {path}") #Imprime el mensaje de la captura guardada.

    def footer1(self):
        try:
            #Localiza y clica en la url del footer.
            vuelos_baratos = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='footerNavListId-0']/li[1]/a")))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", vuelos_baratos)
            time.sleep(1)
            vuelos_baratos.click()
            
            #Esperar que la URL cambie.
            self.wait.until(EC.url_to_be("https://nuxqa4.avtest.ink/es/ofertas-destinos/ofertas-de-vuelos/"))
            self.save_screenshot("C:/Users/LuisYánezMalavé/Pictures/Screenshots/ofertas_vuelos.png") 

            #Validar si la URL actual es la esperada
            current_url = self.driver.current_url
            if current_url == "https://nuxqa4.avtest.ink/es/ofertas-destinos/ofertas-de-vuelos/":
                print("✅ Navegación exitosa: La URL es correcta.")
            else:
                print(f"❌ Error: URL incorrecta. Se obtuvo {current_url}")

        except Exception as e:
            print(f"❌ Error en la validación de la URL: {e}")

    def footer2(self):
        try:
            #Localiza y clica en la url del footer.
            somos_av = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='footerNavListId-1']/li[1]/a")))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", somos_av)
            time.sleep(1)
            somos_av.click()
             
            #Esperar que la URL cambie.
            self.wait.until(EC.url_to_be("https://nuxqa4.avtest.ink/es/sobre-nosotros/somos-avianca/"))
            self.save_screenshot("C:/Users/LuisYánezMalavé/Pictures/Screenshots/somos_avianca.png") 

            #Validar si la URL actual es la esperada
            current_url = self.driver.current_url
            if current_url == "https://nuxqa4.avtest.ink/es/sobre-nosotros/somos-avianca/":
                print("✅ Navegación exitosa: La URL es correcta.")
            else:
                print(f"❌ Error: URL incorrecta. Se obtuvo {current_url}")

        except Exception as e:
            print(f"❌ Error en la validación de la URL: {e}")

    def footer3(self):
        try:
            #Localiza y clica en url del footer.
            url_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='footerNavListId-3']/li[1]/a")))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", url_btn)
            time.sleep(1)
            url_btn.click()
             
             #Esperar que la URL cambie.
            self.wait.until(EC.url_to_be("https://nuxqa4.avtest.ink/es/informacion-legal/informacion-legal/"))
            self.save_screenshot("C:/Users/LuisYánezMalavé/Pictures/Screenshots/informacion_legal.png") 

            #Validar si la URL actual es la esperada
            current_url = self.driver.current_url
            if current_url == "https://nuxqa4.avtest.ink/es/informacion-legal/informacion-legal/":
                print("✅ Navegación exitosa: La URL es correcta.")
            else:
                print(f"❌ Error: URL incorrecta. Se obtuvo {current_url}")

        except Exception as e:
            print(f"❌ Error en la validación de la URL: {e}")

    def footer4(self):
        try:
            #Localiza y clica en la url del footer.
            btn_url = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='footerNavListId-3']/li[2]/a")))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn_url)
            time.sleep(1)
            btn_url.click()
             
             #Esperar que la URL cambie.
            self.wait.until(EC.url_to_be("https://nuxqa4.avtest.ink/es/informacion-legal/politica-privacidad/"))
            self.save_screenshot("C:/Users/LuisYánezMalavé/Pictures/Screenshots/politica_privacidad.png") 

            #Validar si la URL actual es la esperada
            current_url = self.driver.current_url
            if current_url == "https://nuxqa4.avtest.ink/es/informacion-legal/politica-privacidad/":
                print("✅ Navegación exitosa: La URL es correcta.")
            else:
                print(f"❌ Error: URL incorrecta. Se obtuvo {current_url}")

        except Exception as e:
            print(f"❌ Error en la validación de la URL: {e}")
