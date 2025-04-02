from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#CASO AUTOMATIZADO 6
class URL_Validation:
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

    def header1(self):
        try:
            #Clicar en el menu del header.
            self.click_element("//*[@id='mainHeaderDiv']/main-header-container/main-header-layout-custom/header/div[2]/div[2]/primary-nav-custom/nav/ul/li[2]/button")
            #Clicar en la opción del submenu.
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='primary-nav-sub-menu-1']/div/div/div[2]/div/nav/ul/li[1]/a"))).click()
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
            print(f"❌ Error en la navegación del menú: {e}")

    def header2(self):
        try:
            #Clicar en el menu del header.
            self.click_element("//*[@id='mainHeaderDiv']/main-header-container/main-header-layout-custom/header/div[2]/div[2]/primary-nav-custom/nav/ul/li[2]/button")
            #Clicar en la opción del submenu.
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='primary-nav-sub-menu-1']/div/div/div[2]/div/nav/ul/li[2]/a"))).click()
             #Esperar que la URL cambie.
            self.wait.until(EC.url_to_be("https://nuxqa4.avtest.ink/es/ofertas-destinos/destinos/"))
            self.save_screenshot("C:/Users/LuisYánezMalavé/Pictures/Screenshots/destinos.png") 

            #Validar si la URL actual es la esperada
            current_url = self.driver.current_url
            if current_url == "https://nuxqa4.avtest.ink/es/ofertas-destinos/destinos/":
                print("✅ Navegación exitosa: La URL es correcta.")
            else:
                print(f"❌ Error: URL incorrecta. Se obtuvo {current_url}")

        except Exception as e:
            print(f"❌ Error en la navegación del menú: {e}")

    def header3(self):
        try:
            #Clicar en el menu del header.
            self.click_element("//*//*[@id='mainHeaderDiv']/main-header-container/main-header-layout-custom/header/div[2]/div[2]/primary-nav-custom/nav/ul/li[2]/button")
            #Clicar en la opción del submenu.
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='primary-nav-sub-menu-1']/div/div/div[2]/div/nav/ul/li[3]/a"))).click()
            #Esperar que la URL cambie.
            self.wait.until(EC.url_to_be("https://nuxqa4.avtest.ink/es/ofertas-destinos/nuevas-rutas/"))
            self.save_screenshot("C:/Users/LuisYánezMalavé/Pictures/Screenshots/nuevas_rutas.png") 

             #Validar si la URL actual es la esperada
            current_url = self.driver.current_url
            if current_url == "https://nuxqa4.avtest.ink/es/ofertas-destinos/nuevas-rutas/":
                print("✅ Navegación exitosa: La URL es correcta.")
            else:
                print(f"❌ Error: URL incorrecta. Se obtuvo {current_url}")

        except Exception as e:
            print(f"❌ Error en la navegación del menú: {e}")