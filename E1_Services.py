from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#CASO AUTOMATIZADO 1
class Servicios:
	def __init__(self, driver):
		self.driver = driver
		self.wait = WebDriverWait(driver, 15)

	def click_element(self, xpath):
		element = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath))) #Espera que el elemento sea interactivo antes de dar click.
		element.click() #Pulsa click en el elemento.

	def send_keys(self, xpath, keys):
		element = self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath))) #Localiza el input y espera que sea visible.
		element.send_keys(keys) #Ingresa la informacion en el input.

	def save_screenshot(self, path):
		self.driver.save_screenshot(path) #Realiza la captura de pantalla.
		print(f"Captura guardada en: {path}") #Imprime el mensaje de la captura guardada.

	def continuar_btn(self):
		self.wait = WebDriverWait(self.driver, 30)
		self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='maincontent']/div/div[6]/div/div/button-container/div/div/button"))).click()
		self.save_screenshot("C:/Users/LuisYánezMalavé/Pictures/Screenshots/services.png") 