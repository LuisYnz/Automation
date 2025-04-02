from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

#CASO AUTOMATIZADO 1
class Seleccion_Asientos:
	def __init__(self, driver):
		self.driver = driver
		self.wait = WebDriverWait(driver, 60)

	def click_element(self, xpath):
		element = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath))) #Espera que el elemento sea interactivo antes de dar click.
		element.click() #Pulsa click en el elemento.

	def save_screenshot(self, path):
		self.driver.save_screenshot(path) #Realiza la captura de pantalla.
		print(f"Captura guardada en: {path}") #Imprime el mensaje de la captura guardada.

	def asiento_passenger1(self):  #Seleccionar asiento al pasajero 1.
		try:
			asiento_passenger1 = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='seatmapContainer']/div[1]/div/ul/li[11]/ol/li[2]/row/div/seat[2]/button")))
			self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", asiento_passenger1)
			asiento_passenger1.click()
		except TimeoutException:
 			print("No hay asiento disponible, Continuando con el siguiente paso.")

	def asiento_passenger2(self):  #Seleccionar asiento al pasajero 2.
		try:
			self.wait = WebDriverWait(self.driver, 30)
			asiento_passenger2 = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='seatmapContainer']/div[1]/div/ul/li[11]/ol/li[2]/row/div/seat[3]/button"))) 
			self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", asiento_passenger2)
			asiento_passenger2.click()
		except TimeoutException:
 			print("No hay asiento disponible, Continuando con el siguiente paso.")

	def asiento_passenger3(self):  #Seleccionar asiento al pasajero 3.
		try:
			self.wait = WebDriverWait(self.driver, 30)
			asiento_passenger3 = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='seatmapContainer']/div[1]/div/ul/li[11]/ol/li[2]/row/div/seat[1]/button")))
			self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", asiento_passenger3)
			asiento_passenger3.click()
		except TimeoutException:
 			print("No hay asiento disponible, Continuando con el siguiente paso.")
 			self.save_screenshot("C:/Users/LuisYánezMalavé/Pictures/Screenshots/seleccion_seats.png")

	def go_pay(self):
		self.wait = WebDriverWait(self.driver, 30)  
		xpaths = [
		"/html/body/div[1]/main/div/div[4]/div/div/amount-summary-button-container/amount-summary-button/div/div/div[2]/ds-button[2]/button",
		"/html/body/div[1]/main/div/div[4]/div/div/amount-summary-button-container/amount-summary-button/div/div/div[2]/button[2]"
		]

		for xpath in xpaths:
			continuar = self.driver.find_elements(By.XPATH, xpath)
			if continuar:
				continuar[0].click()
				print("✅ Botón de continuar clickeado.")
				return  
