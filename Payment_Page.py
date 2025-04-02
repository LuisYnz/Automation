from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#CASO AUTOMATIZADO 2
class Payment:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def click_element(self, xpath):
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath))) #Espera que el elemento sea interactivo antes de dar click.
        element.click() #Pulsa click en el elemento.

    def send_keys(self, xpath, keys):
        element = self.wait.until(EC.presence_of_element_located((By.XPATH, xpath))) #Localiza el input y espera que sea visible.
        element.send_keys(keys) #Ingresa la informacion en el input.

    def select_dropdown(self, xpath, value_xpath):
        self.click_element(xpath) #Abre el dropdown
        self.click_element(value_xpath) #Selecciona la opcion del dropdown

    def save_screenshot(self, path):
        self.driver.save_screenshot(path) #Realiza la captura de pantalla.
        print(f"Captura guardada en: {path}") #Imprime el mensaje de la captura guardada.

    def credit_card(self):  
    #Acceptar los cookies.
        cookies_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='onetrust-accept-btn-handler']")))
        cookies_button.click()
        time.sleep(2)

        #Localizar el iframe de credit card y entrar en el.
        payment_iframe = self.wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[contains(@class, 'payment-forms-layout_iframe')]")))
        self.driver.switch_to.frame(payment_iframe)

        #Ingresar titular de la tarjeta  
        holder_input = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='Holder']")))
        holder_input.send_keys("Luis Test")

        #Número de tarjeta  
        data_input = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='Data']")))
        data_input.send_keys("4111111111111111")

        #Seleccionar fecha de expiración  
        self.select_dropdown("//*[@id='expirationMonth_ExpirationDate']", "//*[@id='expirationMonth_ExpirationDate-4']")
        self.select_dropdown("//*[@id='expirationYear_ExpirationDate']", "//*[@id='expirationYear_ExpirationDate-26']")

        #CVV  
        cvv_input = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='Cvv']")))
        cvv_input.send_keys("123")
        self.save_screenshot("C:/Users/LuisYánezMalavé/Pictures/Screenshots/credit_card.png")


        self.driver.switch_to.default_content() #Salir del iframe de credit card.

        #Email 
        email_input = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='email']")))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", email_input)
        email_input.send_keys("luis@flyr.com")

        #Dirección  
        address_input = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='address']")))
        address_input.send_keys("KR 20 18 10")  

        #Ciudad  
        city_input = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='city']")))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", city_input)
        city_input.send_keys("Manizales")

        #País  
        self.select_dropdown("//*[@id='country']", "//*[@id='country-0']")
        self.save_screenshot("C:/Users/LuisYánezMalavé/Pictures/Screenshots/credit_info.png")


        #Aceptar términos  
        self.click_element("//*[@id='terms']")
    
       

