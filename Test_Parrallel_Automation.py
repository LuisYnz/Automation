from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import logging
import sys
import os
from concurrent.futures import ThreadPoolExecutor

#Importaciones locales.
from E1_HomePage import Home_Page1
from E1_SelectFlight import SelectFlight
from E1_Passenger import Passengers_Form
from E1_Services import Servicios
from E1_Seatmap import Seleccion_Asientos
from E1_Payment import Pagos
from Footer_Page import URL_Footer
from HomePage import HomePage
from Select_Flight import Select_Flight
from Passenger_Page import Passenger_Form
from Service_Page import Services
from Seat_Page import Seatmap
from Payment_Page import Payment
from Idioma_Page import Select_Idiomas
from Seleccion_Pos import POS
from Url_Page import URL_Validation

#Ruta donde se guardarán los logs
log_directory = r"C:\Users\LuisYánezMalavé\Desktop\Automatizacion\Logz"
log_file = os.path.join(log_directory, "automation_logs.log")


#Configuración de logs
logging.basicConfig(
    filename=log_file,  #Guarda los logs en la carpeta correcta
    level=logging.INFO,  #Nivel de log (INFO y ERROR)
    format="%(asctime)s - %(levelname)s - %(message)s",  #Formato de los logs
    datefmt="%Y-%m-%d %H:%M:%S"  #Formato de la fecha y hora de los logz
)

console_handler = logging.StreamHandler(sys.stdout) #Muestra los logs en la consola.
console_handler.setLevel(logging.INFO) #Configura el nivel de logs que se mostraran
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s") #Define el formato del log (fecha/hora, nivel del mensaje y contenido).
console_handler.setFormatter(formatter) #Aplica el formato de los logs a la consola.
logging.getLogger().addHandler(console_handler) #Ejecuta los formatos configurados.

#Configuración de multi hilos con ThreadPoolExecutor.
def ejecutar_navegador(options, url, test_suite, browser_type='chrome'): #Define la función con los parametros para la automatización en paralelo.
    if browser_type == 'chrome': #Verifica el valor de la variable y declara la función.
        driver = webdriver.Chrome(options=options) #Permite pasar configuraciones al navegador.
    elif browser_type == 'edge': #Verifica el valor de la variable y declara la función.
        driver = webdriver.Edge(options=options) #Permite pasar configuraciones al navegador.

    driver.get(url) #Le indica al navegador que abra la URL asignada.
    driver.maximize_window() #Maximiza la pagina.

    if test_suite: #Verifica el valor de la variable.
        test_suite(driver) #Ejecuta la función del driver.

    driver.quit() #Cierra el navegador al finalizar la suite.

def ejecutar_suite_pruebas_1(driver):
    try:
        Footer_Page = URL_Footer(driver)
        logging.info("✅ Suite de pruebas 1 iniciada.")

        try:
            Footer_Page.footer1()
            logging.info("✅ Validacion de URL vuelos baratos correcta")
        except Exception as e:
            logging.error(f"❌ Error al realizar la validacion de URL {e}")

        try:
            Footer_Page.footer2()
            logging.info("✅ Validacion de URL somos avianca correcta.")
        except Exception as e:
            logging.error(f"❌ Error al realizar la validacion de URL.: {e}")

        try:
            Footer_Page.footer3()
            logging.info("✅ Validacion de URL informacion legal correcta.")
        except Exception as e:
            logging.error(f"❌ Error al realizar la validacion de URL.: {e}")

        try:
            Footer_Page.footer4()
            logging.info("✅ Validacion de URL politica de privacidad correcta.")
        except Exception as e:
            logging.error(f"❌ Error al realizar la validacion de URL {e}")

    except Exception as e:
        logging.error(f"❌ Error al realizar la validacion de URL.: {e}")

def ejecutar_suite_pruebas_2(driver):
    try:
        E1_HomePage = Home_Page1(driver)
        logging.info("✅ Suite de pruebas 2 iniciada.")

        try:
            E1_HomePage.select_idioma()
            logging.info("✅ Idioma seleccionado de forma correcta.")
        except Exception as e:
            logging.error(f"❌ Error al seleccionar idioma.: {e}")

        try:
            E1_HomePage.select_pos()
            logging.info("✅ POS seleccionado correctamente.")
        except Exception as e:
            logging.error(f"❌ Error al seleccionar el POS.: {e}")

        try:
            E1_HomePage.vuelo_ow()
            logging.info("✅ Tipo vuelo OW seleccionado correctamente.")
        except Exception as e:
            logging.error(f"❌ Error al seleccionar el tipo de vuelo.: {e}")

        try:
            E1_HomePage.estacion("Bogota", "Cali")
            logging.info("✅ Origen y destino seleccionado correctamente.")
        except Exception as e:
            logging.error(f"❌ Error al seleccionar origen y destino.: {e}")

        try:
            E1_HomePage.select_fechas()
            logging.info("✅ Fecha seleccionada correctamente.")
        except Exception as e:
            logging.error(f"❌ Error al seleccionar la fecha.: {e}")

        try:
            E1_HomePage.passenger("1", "1", "0")
            logging.info("✅ Pasajeros seleccionados correctamente.")
        except Exception as e:
            logging.error(f"❌ Error al seleccionar pasajeros.: {e}")

        E1_SelectFlight = SelectFlight(driver)
        try:
            E1_SelectFlight.seleccion_vuelo()
            logging.info("✅ Tarifa de vuelo seleccionado correctamente.")
        except Exception as e:
            logging.error(f"❌ Error al seleccionar tarifa de vuelo.: {e}")

        try:
            E1_SelectFlight.continuar_btn()
            logging.info("✅ Continua a la pagina de pasajeros correctamente.")
        except Exception as e:
            logging.error(f"❌ Error al continuar a la pagina de pasajeros.: {e}")

        E1_Passenger = Passengers_Form(driver)
        try:
            E1_Passenger.adt()
            logging.info("✅ Formulario pasajero ADT diligenciado correctamente.")
        except Exception as e:
            logging.error(f"❌ Error al diligenciar el formulario del pasajero ADT.: {e}")

        try:
            E1_Passenger.inf()
            logging.info("✅ Formulario pasajero INF diligenciado correctamente.")
        except Exception as e:
            logging.error(f"❌ Error al diligenciar el formulario del pasajero INF.: {e}")

        try:
            E1_Passenger.youth()
            logging.info("✅ Formulario pasajero YOUTH diligenciado correctamente.")
        except Exception as e:
            logging.error(f"❌ Error al diligenciar el formulario del pasajero YOUTH.: {e}")

        try:
            E1_Passenger.chd()
            logging.info("✅ Formulario pasajero CHD diligenciado correctamente.")
        except Exception as e:
            logging.error(f"❌ Error al diligenciar el formulario del pasajero CHD.: {e}")

        try:
            E1_Passenger.contact()
            logging.info("✅ Formulario contacto diligenciado correctamente.")
        except Exception as e:
            logging.error(f"❌ Error al diligenciar el formulario de contacto.: {e}")

        try:
            E1_Passenger.continue_bton()
            logging.info("✅ Continuar a la pagina de servicios correctamente.")
        except Exception as e:
            logging.error(f"❌ Error al continuar a la pagina de servicios.: {e}")

        E1_Services = Servicios(driver)
        try:
            E1_Services.continuar_btn()
            logging.info("✅ Continua a la pagina seatmap correctamente.")
        except Exception as e:
            logging.error(f"❌ Error al cotinuar a la pagina seatmap.: {e}")
        # Seat Page
        E1_Seatmap = Seleccion_Asientos(driver)

        try:
            E1_Seatmap.asiento_passenger1()
            logging.info("✅ Asiento seleccionado para pasajero 1")
        except Exception as e:
            logging.error(f"❌ Error al seleccionar asiento pasajero 1: {e}")

        try:
            E1_Seatmap.asiento_passenger2()
            logging.info("✅ Asiento seleccionado para pasajero 2")
        except Exception as e:
            logging.error(f"❌ Error al seleccionar asiento pasajero 2: {e}")

        try:
            E1_Seatmap.asiento_passenger3()
            logging.info("✅ Asiento seleccionado para pasajero 3")
        except Exception as e:
            logging.error(f"❌ Error al seleccionar asiento pasajero 3: {e}")

        try:
            E1_Seatmap.go_pay()
            logging.info("✅ Continuar a payment")
        except Exception as e:
            logging.error(f"❌ Error al continuar a payment: {e}")

        E1_Payment = Pagos(driver)
        try:
            E1_Payment.credit_card()
            logging.info("✅ Se realizo el pago correctamente.")
        except Exception as e:
            logging.error(f"❌ Error al realiar el pago.: {e}")

    except Exception as e:
        logging.error(f"❌Error en la Suite de Pruebas 2: {e}") 

def ejecutar_suite_pruebas_3(driver):
    try:
        home_page = HomePage(driver)
        logging.info("✅ Suite de pruebas 3 iniciada.")
        try:
            home_page.idioma()
            logging.info("✅ Idioma seleccionado correctamente.")
        except Exception as e:
            logging.error(f"❌ Error al seleccionar idioma: {e}")

        try:
            home_page.pos()
            logging.info("✅ POS seleccionado correctamente.")
        except Exception as e:
            logging.error(f"❌ Error al seleccionar POS: {e}")

        try:
            home_page.origen_destino("Aruba", "Bogota")
            logging.info("✅ Origen y destino ingresados.")
        except Exception as e:
            logging.error(f"❌ Error al ingresar origen y destino: {e}")

        try:
            home_page.ingresar_fechas("2025-03-25", "2025-03-30")
            logging.info("✅ Fechas ingresadas.")
        except Exception as e:
            logging.error(f"❌ Error al ingresar fechas: {e}")

        try:
            home_page.pasajeros("1", "1", "0")
            logging.info("✅ Pasajeros seleccionados.")
        except Exception as e:
            logging.error(f"❌ Error al seleccionar pasajeros: {e}")

        # Select Flight Page
        select_flight_page = Select_Flight(driver)

        try:
            select_flight_page.vuelo_ida()
            logging.info("✅ Vuelo de ida seleccionado.")
        except Exception as e:
            logging.error(f"❌ Error al seleccionar vuelo de ida: {e}")

        try:
            select_flight_page.vuelo_vuelta()
            logging.info("✅ Vuelo de regreso seleccionado.")
        except Exception as e:
            logging.error(f"❌ Error al seleccionar vuelo de regreso: {e}")

        try:
            select_flight_page.continuar()
            logging.info("✅ Confirmar continuar a passenger page.")
        except Exception as e:
            logging.error(f"❌ Error al continuar a passenger page: {e}")

        # Passenger Page
        passenger_page = Passenger_Form(driver)

        try:
            passenger_page.adt_form()
            logging.info("✅ Form adulto diligenciado.")
        except Exception as e:
            logging.error(f"❌ Error en Form adulto: {e}")

        try:
            passenger_page.inf_form()
            logging.info("✅ Form bebé diligenciado.")
        except Exception as e:
            logging.error(f"❌ Error en Form bebé: {e}")

        try:
            passenger_page.youth_form()
            logging.info("✅ Form joven diligenciado.")
        except Exception as e:
            logging.error(f"❌ Error en Form joven: {e}")

        try:
            passenger_page.chd_form()
            logging.info("✅ Form niño diligenciado.")
        except Exception as e:
            logging.error(f"❌ Error en Form niño: {e}")

        try:
            passenger_page.contact_form()
            logging.info("✅ Form contacto diligenciado.")
        except Exception as e:
            logging.error(f"❌ Error en Form contacto: {e}")

        try:
            passenger_page.continue_button()
            logging.info("✅ Continuar a servicios.")
        except Exception as e:
            logging.error(f"❌ Error al continuar a servicios: {e}")

        # Service Page
        service_page = Services(driver)

        try:
            service_page.servicio()
            logging.info("✅ Servicios disponibles para contratar.")
        except Exception as e:
            logging.error(f"❌ Error al ver servicios disponibles: {e}")

        try:
            service_page.passenger1_services()
            logging.info("✅ Servicios seleccionados para pasajero 1")
        except Exception as e:
            logging.error(f"❌ Error al seleccionar servicios para pasajero 1: {e}")

        try:
            service_page.passenger2_services()
            logging.info("✅ Servicios seleccionados para pasajero 2")
        except Exception as e:
            logging.error(f"❌ Error al seleccionar servicios para pasajero 2: {e}")

        try:
            service_page.passenger3_services()
            logging.info("✅ Servicios seleccionados para pasajero 3")
        except Exception as e:
            logging.error(f"❌ Error al seleccionar servicios para pasajero 3: {e}")

        try:
            service_page.confirm_boton()
            logging.info("✅ Servicios confirmados.")
        except Exception as e:
            logging.error(f"❌ Error al confirmar servicios: {e}")

        try:
            service_page.continue_btn()
            logging.info("✅ Continuar a seatmap.")
        except Exception as e:
            logging.error(f"❌ Error al continuar a seatmap: {e}")

        seat_page = Seatmap(driver) #SeatPage

        try:
            seat_page.asiento_passenger1()
            logging.info("✅ Asiento seleccionado para pasajero 1")
        except Exception as e:
            logging.error(f"❌ Error al seleccionar asiento pasajero 1: {e}")

        try:
            seat_page.asiento_passenger2()
            logging.info("✅ Asiento seleccionado para pasajero 2")
        except Exception as e:
            logging.error(f"❌ Error al seleccionar asiento pasajero 2: {e}")

        try:
            seat_page.asiento_passenger3()
            logging.info("✅ Asiento seleccionado para pasajero 3")
        except Exception as e:
            logging.error(f"❌ Error al seleccionar asiento pasajero 3: {e}")

        try:
            seat_page.go_pay()
            logging.info("✅ Continuar a payment")
        except Exception as e:
            logging.error(f"❌ Error al continuar a payment: {e}")

        #Llamar metodos de Payment page.
        Payment_Page = Payment(driver)

        try:
            Payment_Page.credit_card()
            logging.info("✅ Se realizo el pago correctamente.")
        except Exception as e:
            logging.error(f"❌ Error al realiar el pago.: {e}")

    except Exception as e:
        logging.error(f"❌ Error general en la Suite de Pruebas 3: {e}")

def ejecutar_suite_pruebas_4(driver):
    try:
        idioma_page = Select_Idiomas(driver)
        logging.info("✅ Suite de pruebas 4 iniciada.")

        try:
            idioma_page.idiomas()
            logging.info("✅ Idiomas seleccionado correctamente.")
        except Exception as e:
            logging.error(f"❌ Error al seleccionar los idiomas: {e}")
        
    except Exception as e:
            logging.error(f"❌Error en la Suite de Pruebas 4: {e}")

def ejecutar_suite_pruebas_5(driver):  
    try:
        seleccion_pos = POS(driver)
        logging.info("✅ Suite de pruebas 5 iniciada.")
        try:
            seleccion_pos.pos_list()
            logging.info("✅ Lista de pos seleccionados")
        except Exception as e:
            logging.error(f"❌ Error al seleccionar la lista de POS: {e}")

    except Exception as e:
        logging.error(f"❌Error en la Suite de Pruebas 5: {e}")

def ejecutar_suite_pruebas_6(driver):
    try:
        logging.info("✅ Suite de pruebas 6 iniciada.")
        Url_Page = URL_Validation(driver)
        try:
            Url_Page.header1()
            logging.info("✅ Validacion de URL ofertas de vuelos correcta.")
        except Exception as e:
            logging.error(f"❌ Error al realizar la validacion de URL.: {e}")

        try:
            Url_Page.header2()
            logging.info("✅ Validacion de URL ofertas nueva ruta correcta.")
        except Exception as e:
            logging.error(f"❌ Error al realizar la validacion de URL.: {e}")

        try:
            Url_Page.header3()
            logging.info("✅ Validacion de URL correcta.")
        except Exception as e:
            logging.error(f"❌ Error al realizar la validacion de URL.: {e}")

    except Exception as e:
        logging.error(f"❌Error en la Suite de Pruebas 6: {e}")

def run_in_parallel(): #Define la función que ejecutara la suites en paralelo.

    chrome_options = ChromeOptions() #Pasa las configuraciones al navegador.

    edge_options = EdgeOptions() #Pasa las configuraciones al navegador.

    with ThreadPoolExecutor(max_workers=2) as executor: #Ejecuta la suite de pruebas 1 en paralelo.
        print("✅ Ejecutando Suite 1 en Chrome y Edge")
        future_chrome_suite1 = executor.submit(ejecutar_navegador, chrome_options, "https://nuxqa4.avtest.ink/es/", ejecutar_suite_pruebas_1, 'chrome') #Ejecuta la suite en segundo plano con las configuraciones dadas.
        future_edge_suite1 = executor.submit(ejecutar_navegador, edge_options, "https://nuxqa4.avtest.ink/es/", ejecutar_suite_pruebas_1, 'edge') #Ejecuta la suite en segundo plano con las configuraciones dadas.

        # Esperar a que ambas suites terminen antes de continuar con la siguiente fase
        future_chrome_suite1.result() #Espera que la automatización de la suite finalice antes de continuar.
        print("✅ Suite de prueba 1 ejecutada correctamente en Chrome")
        future_edge_suite1.result()
        print("✅ Suite de prueba 1 ejecutada correctamente en Edge")

    with ThreadPoolExecutor(max_workers=2) as executor: #Ejecuta la suite de pruebas 2
        print("✅ Ejecutando Suite 2 en Chrome y Edge")
        future_chrome_suite2 = executor.submit(ejecutar_navegador, chrome_options, "https://nuxqa4.avtest.ink/es/", ejecutar_suite_pruebas_2, 'chrome')
        future_edge_suite2 = executor.submit(ejecutar_navegador, edge_options, "https://nuxqa5.avtest.ink/es/", ejecutar_suite_pruebas_2, 'edge')
       
        # Esperar a que ambas suites terminen antes de finalizar
        future_chrome_suite2.result()
        print("✅ Suite de prueba 2 ejecutada correctamente en Chrome")
        future_edge_suite2.result()
        print("✅ Suite de prueba 2 ejecutada correctamente en Edge")

    #Ejecuta la suite de pruebas 3
    with ThreadPoolExecutor(max_workers=2) as executor:
        print("✅ Ejecutando Suite 3 en Chrome y Edge")
        future_chrome_suite3 = executor.submit(ejecutar_navegador, chrome_options, "https://nuxqa4.avtest.ink/es/", ejecutar_suite_pruebas_3, 'chrome')
        future_edge_suite3 = executor.submit(ejecutar_navegador, edge_options, "https://nuxqa5.avtest.ink/es/", ejecutar_suite_pruebas_3, 'edge')

        # Esperar a que ambas suites terminen antes de finalizar
        future_chrome_suite3.result()
        print("✅ Suite de prueba 3 ejecutada correctamente en Chrome")
        future_edge_suite3.result()
        print("✅ Suite de prueba 3 ejecutada correctamente en Edge")

    #Ejecuta la suite de pruebas 4
    with ThreadPoolExecutor(max_workers=2) as executor:
        print("✅ Ejecutando Suite 4 en Chrome y Edge")
        future_chrome_suite4 = executor.submit(ejecutar_navegador, chrome_options, "https://nuxqa4.avtest.ink/es/", ejecutar_suite_pruebas_4, 'chrome')
        future_edge_suite4 = executor.submit(ejecutar_navegador, edge_options, "https://nuxqa5.avtest.ink/es/", ejecutar_suite_pruebas_4, 'edge')

        # Esperar a que ambas suites terminen antes de finalizar
        future_chrome_suite4.result()
        print("✅ Suite de prueba 4 ejecutada correctamente en Chrome")
        future_edge_suite4.result()
        print("✅ Suite de prueba 4 ejecutada correctamente en Edge")

    #Ejecuta la suite de pruebas 5
    with ThreadPoolExecutor(max_workers=2) as executor:
        print("✅ Ejecutando Suite 5 en Chrome y Edge")
        future_chrome_suite5 = executor.submit(ejecutar_navegador, chrome_options, "https://nuxqa4.avtest.ink/es/", ejecutar_suite_pruebas_5, 'chrome')
        future_edge_suite5 = executor.submit(ejecutar_navegador, edge_options, "https://nuxqa5.avtest.ink/es/", ejecutar_suite_pruebas_5, 'edge')

        # Esperar a que ambas suites terminen antes de finalizar
        future_chrome_suite5.result()
        print("✅ Suite de prueba 5 ejecutada correctamente en Chrome")
        future_edge_suite5.result()
        print("✅ Suite de prueba 5 ejecutada correctamente en Edge")

    #Ejecuta la suite de pruebas 6
    with ThreadPoolExecutor(max_workers=2) as executor:
        print("✅ Ejecutando Suite 6 en Chrome y Edge")
        future_chrome_suite6 = executor.submit(ejecutar_navegador, chrome_options, "https://nuxqa4.avtest.ink/es/", ejecutar_suite_pruebas_6, 'chrome')
        future_edge_suite6 = executor.submit(ejecutar_navegador, edge_options, "https://nuxqa4.avtest.ink/es/", ejecutar_suite_pruebas_6, 'edge')

        # Esperar a que ambas suites terminen antes de finalizar
        future_chrome_suite6.result()
        print("✅ Suite de prueba 6 ejecutada correctamente en Chrome")
        future_edge_suite6.result()
        print("✅ Suite de prueba 6 ejecutada correctamente en Edge")

run_in_parallel() #Llamada a la función para ejecutar en paralelo
