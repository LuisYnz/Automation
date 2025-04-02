from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#CASO AUTOMATIZADO 2
class Services:
	def __init__(self, driver):
		self.driver = driver
		self.wait = WebDriverWait(driver, 30)

	def click_element(self, xpath):
		element = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath))) #Espera que el elemento sea interactivo antes de dar click.
		element.click() #Pulsa click en el elemento.


	def save_screenshot(self, path):
		self.driver.save_screenshot(path) #Realiza la captura de pantalla.
		print(f"Captura guardada en: {path}") #Imprime el mensaje de la captura guardada.

	def servicio(self): #Abrir la categoria de servicios.
		self.click_element("//*[@id='serviceButtonTypeOversize']")

	def passenger1_services(self): #Seleccionar servicio pasajero 1.
		self.wait = WebDriverWait(self.driver, 10)
		self.wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/ngb-modal-window/div/div/div/div/div[2]/ns-service-selector-custom/div/div[2]/div/div[2]/ns-service-details-custom/div/div[1]/div/div/div[2]/div[1]/div[2]/div/div[1]/service-item-custom/div/div/div[4]/div/ns-minus-plus/div/button[2]"))).click()
		self.save_screenshot("C:/Users/LuisYánezMalavé/Pictures/Screenshots/passenger1_services.png") 

	def passenger2_services(self): #Seleccionar servicio pasajero 2.
		passenger2_services = self.driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/div/div/div[2]/ns-service-selector-custom/div/div[2]/div/div[2]/ns-service-details-custom/div/div[1]/div/div/div[2]/div[2]/div[2]/div/div[1]/service-item-custom/div/div/div[4]/div/ns-minus-plus/div/button[2]")
		self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", passenger2_services)
		passenger2_services.click()
		self.save_screenshot("C:/Users/LuisYánezMalavé/Pictures/Screenshots/passenger2_services.png") 

	def passenger3_services(self): #Seleccionar servicio pasajero 3.
		passenger3_services = self.driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/div/div/div[2]/ns-service-selector-custom/div/div[2]/div/div[2]/ns-service-details-custom/div/div[1]/div/div/div[2]/div[3]/div[2]/div/div[1]/service-item-custom/div/div/div[4]/div/ns-minus-plus/div/button[2]")
		self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", passenger3_services)
		passenger3_services.click()
		self.save_screenshot("C:/Users/LuisYánezMalavé/Pictures/Screenshots/passenger1_services.png") 

	def confirm_boton(self):  
		xpaths = [
		"/html/body/ngb-modal-window/div/div/div/div/div[2]/ns-service-selector-custom/div/div[3]/amount-summary-button/div/div/div[2]/ds-button[2]/button",
		"/html/body/ngb-modal-window/div/div/div/div/div[2]/ns-service-selector-custom/div/div[3]/amount-summary-button/div/div/div[2]/button[2]"
		]

		for xpath in xpaths:
			botones = self.driver.find_elements(By.XPATH, xpath)
			if botones:
				self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", botones[0])
				botones[0].click()
				print("✅ Botón de confirmación clickeado.")
				return  

	def continue_btn(self):
		self.wait = WebDriverWait(self.driver, 30)
		self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='maincontent']/div/div[6]/div/div/button-container/div/div/button"))).click()

		
		
