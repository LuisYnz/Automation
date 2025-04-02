from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import time
#CASO AUTOMATIZADO 1

class Passengers_Form:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_element(self, xpath):
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath))) #Espera que el elemento sea interactivo antes de dar click.
        element.click() #Pulsa click en el elemento.

    def send_keys(self, xpath, keys):
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath))) #Localiza el input y espera que sea visible.
        element.send_keys(keys) #Ingresa la informacion en el input.

    def select_dropdown(self, xpath, value_xpath):
        self.click_element(xpath) #Abre el dropdown
        self.click_element(value_xpath) #Selecciona la opcion del dropdown

    def save_screenshot(self, path):
        self.driver.save_screenshot(path) #Realiza la captura de pantalla.
        print(f"Captura guardada en: {path}") #Imprime el mensaje de la captura guardada.    

    def adt(self): #Diligenciar form del pasajero ADT.
        #Seleccionar titulo del ADT.
        self.select_dropdown("//*[@id='IdPaxGender_7E7E303030312D30312D30317E353334423438324433323244343535383534']", "//*[@id='IdPaxGender_7E7E303030312D30312D30317E353334423438324433323244343535383534-0']")
        # Ingresar nombre del pasajero ADT.
        self.send_keys("/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[1]/personal-data-form-custom/div/form/div/div[1]/div/div[2]/ibe-input/div/div/input", "Charizard")
        # Ingresar surname del pasajero ADT.
        self.send_keys("/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[1]/personal-data-form-custom/div/form/div/div[2]/ibe-input/div/div/input", "Tetsa")
        # Seleccionar fecha de nacimiento del ADT.
        self.select_dropdown("/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[1]/personal-data-form-custom/div/form/div/div[3]/input-date-picker-custom/ibe-select-date-picker-custom/div/div/fieldset/div/div[1]/ibe-select-custom/div/div[2]/button", "//*[@id='dateDayId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433323244343535383534_-0']")
        self.select_dropdown("/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[1]/personal-data-form-custom/div/form/div/div[3]/input-date-picker-custom/ibe-select-date-picker-custom/div/div/fieldset/div/div[2]/ibe-select-custom/div/div[2]/button", "//*[@id='dateMonthId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433323244343535383534_-2']")
        self.select_dropdown("/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[1]/personal-data-form-custom/div/form/div/div[3]/input-date-picker-custom/ibe-select-date-picker-custom/div/div/fieldset/div/div[3]/ibe-select-custom/div/div[2]/button", "//*[@id='dateYearId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433323244343535383534_-2']")
        self.select_dropdown("/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[1]/personal-data-form-custom/div/form/div/div[4]/ibe-select-custom/div/div[2]/button", "//*[@id='IdDocNationality_7E7E303030312D30312D30317E353334423438324433323244343535383534-1']")
        self.save_screenshot("C:/Users/LuisYánezMalavé/Pictures/Screenshots/passenger_adt.png") 
        
    def inf(self): #Diligenciar form del pasajero INF.
        # Localiza el formulario INF y realiza scroll
        form_inf = self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[2]/personal-data-form-custom/div/form")
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", form_inf)

        #Seleccionar titulo del INF.
        self.select_dropdown("/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[2]/personal-data-form-custom/div/form/div/div[1]/div/div[1]/ibe-select-custom/div/div[2]/button", "//*[@id='IdPaxGender_7E7E303030312D30312D30317E353334423438324433313244343535383534-1']")
        # Ingresar nombre del pasajero INF.
        self.send_keys("/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[2]/personal-data-form-custom/div/form/div/div[1]/div/div[2]/ibe-input/div/div/input", "Tester")
        # Ingresar surname del pasajero INF.
        self.send_keys("/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[2]/personal-data-form-custom/div/form/div/div[2]/ibe-input/div/div/input", "Goku")
        # Seleccionar fecha de nacimiento del INF.
        self.select_dropdown("/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[2]/personal-data-form-custom/div/form/div/div[3]/input-date-picker-custom/ibe-select-date-picker-custom/div/div/fieldset/div/div[1]/ibe-select-custom/div/div[2]/button", "//*[@id='dateDayId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433313244343535383534_-0']")
        self.select_dropdown("/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[2]/personal-data-form-custom/div/form/div/div[3]/input-date-picker-custom/ibe-select-date-picker-custom/div/div/fieldset/div/div[2]/ibe-select-custom/div/div[2]/button", "//*[@id='dateMonthId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433313244343535383534_-0']")
        self.select_dropdown("/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[2]/personal-data-form-custom/div/form/div/div[3]/input-date-picker-custom/ibe-select-date-picker-custom/div/div/fieldset/div/div[3]/ibe-select-custom/div/div[2]/button", "//*[@id='dateYearId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433313244343535383534_-0']")
        self.select_dropdown("/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[2]/personal-data-form-custom/div/form/div/div[4]/ibe-select-custom/div/div[2]/button", "//*[@id='IdDocNationality_7E7E303030312D30312D30317E353334423438324433313244343535383534-1']")
        self.save_screenshot("C:/Users/LuisYánezMalavé/Pictures/Screenshots/passenger_inf.png") 

    def youth(self): #Diligenciar form del pasajero joven.
        # Localiza el formulario joven y realiza scroll
        form_youth = self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[3]/personal-data-form-custom/div/form")                                                 
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", form_youth)

        #Seleccionar titulo del joven.
        self.select_dropdown("/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[3]/personal-data-form-custom/div/form/div/div[1]/div/div[1]/ibe-select-custom/div/div[2]/button", "//*[@id='IdPaxGender_7E7E303030312D30312D30317E353334423438324433333244343535383534-0']")
        # Ingresar nombre del pasajero joven.
        self.send_keys("/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[3]/personal-data-form-custom/div/form/div/div[1]/div/div[2]/ibe-input/div/div/input", "Vegueta")
        # Ingresar surname del pasajero joven.
        self.send_keys("/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[3]/personal-data-form-custom/div/form/div/div[2]/ibe-input/div/div/input", "Turs")
        # Seleccionar fecha de nacimiento del joven.
        self.select_dropdown("/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[3]/personal-data-form-custom/div/form/div/div[3]/input-date-picker-custom/ibe-select-date-picker-custom/div/div/fieldset/div/div[1]/ibe-select-custom/div/div[2]/button", "//*[@id='dateDayId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433333244343535383534_-1']")
        self.select_dropdown("/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[3]/personal-data-form-custom/div/form/div/div[3]/input-date-picker-custom/ibe-select-date-picker-custom/div/div/fieldset/div/div[2]/ibe-select-custom/div/div[2]/button", "//*[@id='dateMonthId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433333244343535383534_-2']")
        self.select_dropdown("/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[3]/personal-data-form-custom/div/form/div/div[3]/input-date-picker-custom/ibe-select-date-picker-custom/div/div/fieldset/div/div[3]/ibe-select-custom/div/div[2]/button", "//*[@id='dateYearId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433333244343535383534_-1']")
        self.select_dropdown("/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[3]/personal-data-form-custom/div/form/div/div[4]/ibe-select-custom/div/div[2]/button", "//*[@id='IdDocNationality_7E7E303030312D30312D30317E353334423438324433333244343535383534-1']")   
        self.save_screenshot("C:/Users/LuisYánezMalavé/Pictures/Screenshots/passenger_joven.png") 

    def chd(self): #Diligenciar form del pasajero joven.
        # Localiza el formulario joven y realiza scroll
        form_chd = self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[4]/personal-data-form-custom/div/form")                                                 
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", form_chd)

        #Seleccionar titulo del CHD.
        self.select_dropdown("/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[4]/personal-data-form-custom/div/form/div/div[1]/div/div[1]/ibe-select-custom/div/div[2]/button", "//*[@id='IdPaxGender_7E7E303030312D30312D30317E353334423438324433343244343535383534-0']")
        # Ingresar nombre del pasajero CHD.
        self.send_keys("/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[4]/personal-data-form-custom/div/form/div/div[1]/div/div[2]/ibe-input/div/div/input", "Pedro")
        # Ingresar surname del pasajero CHD.
        self.send_keys("/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[4]/personal-data-form-custom/div/form/div/div[2]/ibe-input/div/div/input", "Peresa")
        # Seleccionar fecha de nacimiento del CHD.
        self.select_dropdown("/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[4]/personal-data-form-custom/div/form/div/div[3]/input-date-picker-custom/ibe-select-date-picker-custom/div/div/fieldset/div/div[1]/ibe-select-custom/div/div[2]/button", "//*[@id='dateDayId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433343244343535383534_-1']")
        self.select_dropdown("/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[4]/personal-data-form-custom/div/form/div/div[3]/input-date-picker-custom/ibe-select-date-picker-custom/div/div/fieldset/div/div[2]/ibe-select-custom/div/div[2]/button", "//*[@id='dateMonthId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433343244343535383534_-0']")
        self.select_dropdown("/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[4]/personal-data-form-custom/div/form/div/div[3]/input-date-picker-custom/ibe-select-date-picker-custom/div/div/fieldset/div/div[3]/ibe-select-custom/div/div[2]/button", "//*[@id='dateYearId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433343244343535383534_-1']")
        self.select_dropdown("/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[4]/personal-data-form-custom/div/form/div/div[4]/ibe-select-custom/div/div[2]/button", "//*[@id='IdDocNationality_7E7E303030312D30312D30317E353334423438324433343244343535383534-1']")   
        self.save_screenshot("C:/Users/LuisYánezMalavé/Pictures/Screenshots/passenger_chd.png")     

    def contact(self): #Diligencia la informacion de contact details
        #Localiza el formulario y realiza scroll.
        form_contact = self.driver.find_element(By.XPATH, "//*[@id='maincontent']/div/div[3]/div/div/contact-container/booking-contact-custom")                                                 
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", form_contact)
        # Seleccionar prefix
        self.select_dropdown("//*[@id='phone_prefixPhoneId']", "//*[@id='phone_prefixPhoneId-1']")
        #Ingresar numero de telefono.
        self.send_keys("//*[@id='phone_phoneNumberId']", "3231536789")
        #Ingresar email.
        self.send_keys("//*[@id='email']", "luis.yanez@flyr.com")
        self.save_screenshot("C:/Users/LuisYánezMalavé/Pictures/Screenshots/contacto.png") 
        
        try:
            confirm_email_element = self.driver.find_element(By.XPATH, "//*[@id='confirmEmail']")
            confirm_email_element.send_keys("luis.yanez@flyr.com")
            print("Campo 'Confirmar Email' encontrado y diligenciado.")
        except NoSuchElementException:
            print("Campo 'Confirmar Email' no está presente. Continuando con el siguiente paso.")
     
    def continue_bton(self): #Localiza el boton continuar y sigue a la siguiente pagina.
        self.click_element("//*[@id='maincontent']/div/div[3]/div/div/contact-container/booking-contact-custom/form/div[2]/ibe-checkbox")
        time.sleep(2)
        self.click_element("//*[@id='maincontent']/div/div[3]/div/div/button-container/div/div/button")

        try:  
        #Espera a que aparezca el botón OK
            self.wait = WebDriverWait(self.driver, 30)
            ok_btn = self.wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/ngb-modal-window/div/div/div/div[3]/button")))
            ok_btn.click()
            print("Botón OK localizado y pulsado")
        
        #Volver a hacer clic en el botón continuar después de cerrar el modal
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='maincontent']/div/div[3]/div/div/button-container/div/div/button"))).click()
        except TimeoutException:
            print("No se encontró el botón OK, continuando con el siguiente paso.")