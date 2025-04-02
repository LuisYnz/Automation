from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#CASO AUTOMATIZADO 4

class POS():   
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_element(self, xpath):
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath))) #Espera que los elementos sean interactivo antes de dar click.
        element.click()

    def save_screenshot(self, path):
        self.driver.save_screenshot(path)
        print(f"Captura guardada en: {path}")

    def pos_list(self):  
        self.wait = WebDriverWait(self.driver, 30)

        #Hacer clic en el selector de POS
        self.click_element("//*[@id='pointOfSaleSelectorId']")

        #Lista de POS a seleccionar
        pos_list = [
            "//*[@id='pointOfSaleListId']/li[16]/button",  # Otros países
            "//*[@id='pointOfSaleListId']/li[10]/button",  # España
            "//*[@id='pointOfSaleListId']/li[5]/button",   # Chile
        ]

        for index, pos_xpath in enumerate(pos_list):
            try:
                #Asegurar que la lista de POS está abierta antes de seleccionar
                self.wait.until(EC.visibility_of_element_located((By.XPATH, pos_xpath)))

                #Seleccionar el POS
                self.click_element(pos_xpath)

                #Confirmar la selección
                confirm_button_xpath = "/html/body/points-of-sale-container/div/div/points-of-sale-popup-layout-custom/div/div/div[3]/div/button"
                self.click_element(confirm_button_xpath)

                #Esperar a que el modal desaparezca despues de confirmar el pos.
                self.wait.until(EC.invisibility_of_element_located((By.XPATH, confirm_button_xpath)))

                #Volver a abrir el modal de POS
                pos_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='pointOfSaleSelectorId']")))
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", pos_button)
                time.sleep(1) 
                pos_button.click()

                #Esperar que el modal esté cargado de nuevo.
                self.wait.until(EC.visibility_of_element_located((By.XPATH, pos_list[0])))

                print(f"✅ POS {index + 1} seleccionado correctamente.")
            
            finally:
                #Guardar captura después de cada selección
                screenshot_path = f"C:/Users/LuisYánezMalavé/Pictures/Screenshots/pos_{index + 1}.png"
                self.save_screenshot(screenshot_path)

