#Trida definuje metody pro vyplneni formulare
import logging
from datetime import datetime
from Tests.Basic import BasicTools
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from Tests.TestDatabase import DBConnector

class Fill:
    def __init__(self, html_file):
        self.basic_tools = BasicTools() #Inicializuje otevreni prohlizece
        self.basic_tools.open_html_file(html_file)
        self.driver = self.basic_tools.driver
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self.logger.addHandler(logging.FileHandler('fill_logs.log')) #Soubor pro ukladani logu
        self.db_connector = DBConnector("Tests/tests_database.db")#Pripojeni na DB pro ukladani logu automatu
        self.db_connector.connect_to_database()

        #Metoda nacte matici dat
#1. sloupec obsahuje jmena prvku
#2. sloupec obsahuje data k vyplneni
    def Fill_strings(self, data):
        for row in data:  # Cyklus postupne dohleda a doplni jeden element
            if len(row) != 2:
                self.logger.error(
                    f"{datetime.now()} - Chyba: Matice musí obsahovat 2 sloupce se jménem prvku a s daty.")
                return

            name, value = row
            try:
                element = self.driver.find_element(By.NAME, name)
                element.send_keys(value)
                log_message = f"Hodnota '{value}' byla úspěšně vyplněna do prvku s názvem '{name}'."
                log_type = "info"
                self.logger.info(f"{datetime.now()} - {log_message}")
            except NoSuchElementException as e:
                log_message = f"Prvek s jménem '{name}' nebyl nalezen: {e}"
                log_type = "error"
                self.logger.error(f"{datetime.now()} - {log_message}")
            self.db_connector.insert_into_logs_table(datetime.now(), log_type, log_message)
            self.basic_tools.screen_shot() #Pridany screenshot

    def Button_click(self, name_button):
        try:
            self.driver.find_element(By.NAME, name_button).click()
            log_message = f"Tlačítko '{name_button}' bylo úspěšně stisknuto."
            log_type = "info"  # Typ logu pro úspěšné stisknutí tlačítka
            self.logger.info(f"{datetime.now()} - {log_message}")
        except NoSuchElementException as e:
            log_message = f"Tlačítko s jménem '{name_button}' nebylo nalezeno: {e}"
            log_type = "error"
            self.logger.error(f"{datetime.now()} - {log_message}")
        self.db_connector.insert_into_logs_table(datetime.now(), log_type, log_message)


