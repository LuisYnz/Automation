from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#CASO AUTOMATIZADO 4

class Select_Idiomas:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_element(self, xpath):
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath))) #Espera que los elementos sean interactivo antes de dar click.
        element.click()

    def save_screenshot(self, path): #Realiza la captura de pantalla.
        self.driver.save_screenshot(path)
        print(f"Captura guardada en: {path}")

    def select_dropdown(self, dropdown_xpath, idioma_xpath):
        self.click_element(dropdown_xpath)  # Abre el dropdown
        self.click_element(idioma_xpath)    # Selecciona el idioma

    def idiomas(self):
        dropdown_xpath = "//*[contains(@id, 'languageListTriggerId')]" #Seleccionar el dropdown de idiomas.

        idiomas = [ #Organizar la lista de idiomas.
            ("English", "//li[1]/button"),
            ("Português", "//li[2]/button"),
            ("Français", "//li[3]/button"),
            ("Español", "//li[1]/button"),
        ]

        for index, (idioma, idioma_xpath) in enumerate(idiomas): #Oranizar el bucle para recorrer lista de idiomas.
            try:
            #Abrir el dropdown cada vez (para evitar pérdida de referencia tras la recarga)
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath))).click()

            #Seleccionar el idioma
                idioma_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, idioma_xpath)))
                idioma_element.click()

            #Esperar a que la página recargue completamente
                WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//*[@id='pointOfSaleSelectorId']")))

                print(f"✅ Idioma seleccionado correctamente: {idioma}")

            finally:
            # Tomar captura de pantalla después de cada cambio
                screenshot_path = f"C:/Users/LuisYánezMalavé/Pictures/Screenshots/idioma_{index + 1}.png"
                self.wait = WebDriverWait(self.driver, 10)
                self.save_screenshot(screenshot_path)
