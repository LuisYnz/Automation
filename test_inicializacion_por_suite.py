#Importacion de librerias.
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time 
import logging
import sys
import os
import obsws_python as obs


# Importaciones locales de archivos POM.
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

log_directory = r"C:\Users\LuisYánezMalavé\Desktop\Automatizacion\Logz" #Variable y ubucación donde se guardara el documento de los logz.
log_file = os.path.join(log_directory, "automation_logs.log") #Genera el documento con la información de los logs.


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

logging.info("Configuración de logs iniciada correctamente.")

def iniciar_driver(navegador="chrome"):
    try:
        if navegador == "chrome": #Verifica y declara la funcion para utilizar el navegador Chrome.
            chrome_options = ChromeOptions() #Permite pasar configuraciones al navegador.
            driver = webdriver.Chrome(options=chrome_options) #Inicia el navegador Chrome.
        elif navegador == "edge": #Verifica y declara la funcion para utilizar el navegador Edge.
            edge_options = EdgeOptions() #Permite pasar configuraciones al navegador.
            driver = webdriver.Edge(options=edge_options) #Inicia el navegador Edge.
        else:
            raise ValueError(f"❌ Navegador {navegador} no soportado.") #Detiene la automatizacion si el navegador ingresado no es valido o configurado.
        
        driver.maximize_window() #Maximiza la pagina del navegador. 
        logging.info(f"✅ Driver {navegador} iniciado correctamente.") #Imprime un logs informativo indicando que se ha inciado el driver.
        return driver #Devuelve el valor de la variable para controlar el navegador.
    except Exception as e: #Captura cualquier error en la instancia.
        logging.error(f"❌ Error al iniciar el driver {navegador}: {e}") #Impreme un logs con error cuando no se inicialiaza el driver.
        return None

#Configuración de OBS (Esta información se puede obtener desde el OBS.)
OBS_HOST = "localhost"
OBS_PORT = 4455
OBS_PASSWORD = ""

def iniciar_grabacion_obs(): #Funcion para iniciar la grabación.
    try:
        ws = obs.ReqClient(host=OBS_HOST, port=OBS_PORT, password=OBS_PASSWORD) #Realiza la concecion del OBS con Python.
        ws.start_record() #Inicia la grabación.
        logging.info("✅ Grabación OBS iniciada.") #Registra un mensaje informativo de la grabación iniciada.
        return ws #Devuelve la variable al detener la grabación.
    except Exception as e:
        logging.error(f"❌ Error al iniciar grabación OBS: {e}")
        return None #Devuelve un valor nulo en caso de que no se pueda iniciar la grabación.

def detener_grabacion_obs(ws): #Funcion para dentener la grabacion.
    if ws: #Verifica si la conexión del OBS se ha iniciado (omitira el bloque si no encuentra conexión)
        try:
            ws.stop_record() #Detiene la grabación.
            logging.info("✅ Grabación OBS detenida.") #Registra un mensaje informativo de la grabación detenenida.
        except Exception as e:
            logging.error(f"❌ Error al detener grabación OBS: {e}")

def ejecutar_suite_pruebas_1(driver): #Declara la función para la ejecucion de pruebas.
    ws_obs = iniciar_grabacion_obs() #Inicia la grabación del OBS en la suite.
    try:
        url = "https://nuxqa4.avtest.ink/es/" #Se asigna la URL en la cual se realizara la automatización.
        driver.get(url) #Le indica al navegador que abra la URL asignada.
        logging.info("✅ Suite de pruebas 1 iniciada.") #Registra un mensaje informativo del inicio de la suite.

        Footer_Page = URL_Footer(driver) #Llama al constructor y la clase del POM.

        try: #Realiaza la ejecución en bloques para atrapar los errores de manera mas ordenada.
            Footer_Page.footer1() #Ejecuta las funciones que realizamos en el POM.
            logging.info("✅ Validacion de URL vuelos baratos correcta.") #Registra un mensaje informativo.
        except Exception as e:
            logging.error(f"❌ Error al realizar la validacion de URL.: {e}") #Registra el mensaje en cuanto al error identificado.

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
            logging.error(f"❌ Error al realizar la validacion de URL.: {e}")
        logging.info("✅ Suite de Pruebas 1 finalizada con éxito.")

    except Exception as e:
        logging.error(f"❌Error en la Suite de Pruebas 1: {e}")
    finally:
        driver.quit()
    detener_grabacion_obs(ws_obs) #Detiene la grabacion del OBS en la suite.

def ejecutar_suite_pruebas_2(driver):  #Declara la función para la ejecucion de pruebas.
    ws_obs = iniciar_grabacion_obs() #Inicia la grabación del OBS en la suite.
    try:
        url = "https://nuxqa4.avtest.ink/es/"
        driver.get(url)
        logging.info("✅ Suite de pruebas 2 iniciada.")

        E1_HomePage = Home_Page1(driver) #Llama al constructor y la clase del POM.

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

        E1_SelectFlight = SelectFlight(driver) #Llama a los metodos de select flight.
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

        E1_Passenger = Passengers_Form(driver) #Llama a los metodos de passenger.
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

        E1_Services = Servicios(driver) #Llama a los metodos de services.
        try:
            E1_Services.continuar_btn()
            logging.info("✅ Continua a la pagina seatmap correctamente.")
        except Exception as e:
            logging.error(f"❌ Error al cotinuar a la pagina seatmap.: {e}")
       
        E1_Seatmap = Seleccion_Asientos(driver) #Llama a los metodos de seatmap.

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

        E1_Payment = Pagos(driver) #Llama a los metodos de payment.
        try:
            E1_Payment.credit_card()
            logging.info("✅ Se realizo el pago correctamente.")
        except Exception as e:
            logging.error(f"❌ Error al realiar el pago.: {e}")

        logging.info("✅ Suite de Pruebas 2 finalizada con éxito.")

    except Exception as e:
        logging.error(f"❌Error en la Suite de Pruebas 2: {e}")
    finally:
        driver.quit() #Cierra el navegador al finalizar la suite.
    detener_grabacion_obs(ws_obs) #Detiene la grabacion del OBS en la suite.

def ejecutar_suite_pruebas_3(driver):  #Declara la función para la ejecucion de pruebas.
    ws_obs = iniciar_grabacion_obs() #Inicia la grabación del OBS en la suite.
    try:
        url = "https://nuxqa4.avtest.ink/es/"
        driver.get(url)
        logging.info("✅ Suite de Pruebas 3 iniciada.")

        home_page = HomePage(driver) #Llama al constructor y la clase del POM.

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

        select_flight_page = Select_Flight(driver) # Llama a los metodos de select flight

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

        passenger_page = Passenger_Form(driver) #Llama a los metodos de passenger.

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

        service_page = Services(driver) #Llama a los metodos de services.

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

        seat_page = Seatmap(driver) #Llama a los metodos de Seatmap.

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

        Payment_Page = Payment(driver)  #Llamar metodos de Payment page.

        try:
            Payment_Page.credit_card()
            logging.info("✅ Se realizo el pago correctamente.")
        except Exception as e:
            logging.error(f"❌ Error al realiar el pago.: {e}")

        logging.info("✅ Suite de Pruebas 3 finalizada con éxito.")

    except Exception as e:
        logging.error(f"❌ Error general en la Suite de Pruebas 3: {e}")

    finally:
        driver.quit() #Cierra el navegador al finalizar la suite.
    detener_grabacion_obs(ws_obs) #Detiene la grabacion del OBS en la suite.

def ejecutar_suite_pruebas_4(driver): #Declara la función para iniciar la suite.
    ws_obs = iniciar_grabacion_obs() #Inicia la grabación del OBS en la suite.
    try:
        url = "https://nuxqa4.avtest.ink/es/"
        driver.get(url)
        logging.info("✅ Suite de pruebas 4 iniciada.")

        idioma_page = Select_Idiomas(driver) #Llama al constructor y la clase del POM.

        try:
            idioma_page.idiomas()
            logging.info("✅ Idiomas seleccionado correctamente.")
        except Exception as e:
            logging.error(f"❌ Error al seleccionar los idiomas: {e}")
        
        logging.info("✅ Suite de Pruebas 4 finalizada con éxito.")

    except Exception as e:
        logging.error(f"❌Error en la Suite de Pruebas 4: {e}")
    finally:
        driver.quit() #Cierra el navegador al finalizar la suite.
    detener_grabacion_obs(ws_obs) #Detiene la grabacion del OBS en la suite.

def ejecutar_suite_pruebas_5(driver): #Declara la funcion para incializar la suite.
    ws_obs = iniciar_grabacion_obs() #Inicia la grabación del OBS en la suite.
    try:
        url = "https://nuxqa4.avtest.ink/es/"
        driver.get(url)
        logging.info("✅ Suite de pruebas 5 iniciada.")
        
        seleccion_pos = POS(driver) #Llama al constructor y la clase del POM.
        try:
            seleccion_pos.pos_list()
            logging.info("✅ Lista de pos seleccionados")
        except Exception as e:
            logging.error(f"❌ Error al seleccionar la lista de POS: {e}")
        
        logging.info("✅ Suite de Pruebas 5 finalizada con éxito.")

    except Exception as e:
        logging.error(f"❌Error en la Suite de Pruebas 5: {e}")
    finally:
        driver.quit() #Cierra el navegador al finalizar la suite.
    detener_grabacion_obs(ws_obs) #Detiene la grabacion del OBS en la suite.

def ejecutar_suite_pruebas_6(driver): #Declara la funcion para iniciar la suite.
    ws_obs = iniciar_grabacion_obs() #Inicia la grabación del OBS en la suite.
    try:
        url = "https://nuxqa4.avtest.ink/es/"
        driver.get(url)
        logging.info("✅ Suite de pruebas 6 iniciada.")
        
        Url_Page = URL_Validation(driver)  #Llama al constructor y la clase del POM.
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
        logging.info("✅ Suite de Pruebas 6 finalizada con éxito.")

    except Exception as e:
        logging.error(f"❌Error en la Suite de Pruebas 6: {e}")
    finally:
        driver.quit() #Cierra el navegador al finalizar la suite.
    detener_grabacion_obs(ws_obs) #Detiene la grabacion del OBS en la suite.
   
def ejecutar_todas_las_suites(): #Se ejecutan las suite 1, 3 y 5 con Navegador Edge y las Suite 2, 4 y 6 con Chrome.
    try:
        driver = iniciar_driver("edge") #Inicia la función en el navegador.
        if driver: #Verifica que se permita iniciar el driver.
            ejecutar_suite_pruebas_1(driver) #Inicia la ejecución de la suite.
    except Exception as e: #Ejecuta la variable cuando se encuentran errores.
            print(f"❌ No se pudo inicializar la Suite 1.")
    try:
        driver = iniciar_driver("edge")
        if driver:
            ejecutar_suite_pruebas_3(driver)
    except Exception as e:
            print(f"❌ No se pudo inicializar la Suite 3.")

    try:
        driver = iniciar_driver("edge")
        if driver:
            ejecutar_suite_pruebas_4(driver)
    except Exception as e:
            print(f"❌ No se pudo inicializar la Suite 4.")

    try:
        driver = iniciar_driver("chrome")
        if driver:
            ejecutar_suite_pruebas_2(driver)
    except Exception as e:
            print(f"❌ No se pudo inicializar la Suite 2.")

    try:
        driver = iniciar_driver("chrome")
        if driver:
            ejecutar_suite_pruebas_5(driver)
    except Exception as e:
            print(f"❌ No se pudo inicializar la Suite 5.")

    try:
        driver = iniciar_driver("chrome")
        if driver:
            ejecutar_suite_pruebas_6(driver)
    except Exception as e:
            print(f"❌ No se pudo inicializar la Suite 6.")

if __name__ == "__main__": #Ejecuta las suites de prueba.
    ejecutar_todas_las_suites()