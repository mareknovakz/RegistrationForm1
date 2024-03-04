#Class definuje zakladni metody pro praci s automatizovanymi nastroji
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import os
from datetime import datetime
import logging
from Tests.TestDatabase import DBConnector

class BasicTools:
    def __init__(self):
        try:
            self.driver = webdriver.Firefox()  # Deklarace Firefoxu jako výchozího prohlížeče
            # self.driver = webdriver.Chrome()
            logging.basicConfig(level=logging.INFO)
            self.logger = logging.getLogger(__name__)
            self.logger.addHandler(logging.FileHandler('fill_logs.log'))  # Soubor pro ukládání logu
            self.db_connector = DBConnector("Tests/tests_database.db")  # Připojení na DB pro ukládání logu automatu
            self.db_connector.connect_to_database()
            log_message = "Prohlizec byl uspesne inicializovan"
            log_type = "info"
            self.logger.info(f"{datetime.now()} - {log_message}")
        except WebDriverException as e:
            log_message = f"Nastala chyba při inicializaci prohlížeče: {e}"
            log_type = "error"
            self.logger.error(f"{datetime.now()} - {log_message}")

        self.db_connector.insert_into_logs_table(datetime.now(), log_type, log_message)

    #Otevreni html souboru
    def open_html_file(self, file_name):#Na vstupu se definuje testovany html soubor
        try:
            #Pokud se soubor nenachazi v root slozce je nutne misto nazvu zadat jeho relativni cestu
            cwd = os.getcwd()  # aktualni adresar
            path = os.path.join(cwd, file_name)  # Spojuje relativni cestu a absolutni cestu k adresari
            self.driver.get("file:///" + path)  # Otevreni souboru
            log_message = f" - Soubor {file_name} byl úspěšně otevřen."
            log_type = "info"
            self.logger.info(f"{datetime.now()} - {log_message}")
        except WebDriverException as e:
            log_message = f" - Nastala chyba pri otevirani souboru {file_name}: {e}"
            log_type = "error"
            self.logger.error(f" {datetime.now()} - {log_message}")
        self.db_connector.insert_into_logs_table(datetime.now(), log_type, log_message)
        return self.driver
    def screen_shot(self):
        try:
            self.driver.save_screenshot(f"Tests/screens/screenshot_{datetime.now()}.png")
            log_message = f"Snímek obrazovky uložen jako screenshot_{datetime.now()}.png: do Tests/screens ."
            log_type = "info"
            self.logger.info(f"{datetime.now()} - {log_message}")
        except WebDriverException as e:
            log_message = f"Nastala chyba při ukládání snímku obrazovky jako screenshot_{datetime.now()}: {e}"
            log_type = "error"
            self.logger.error(f"{datetime.now()} - {log_message}")
        self.db_connector.insert_into_logs_table(datetime.now(), log_type, log_message)



