#Trida definuje metody pro vyplneni formulare
import logging
from Tests.Basic import BasicTools
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class Fill:
    def __init__(self, html_file):
        self.basic_tools = BasicTools()  # Vytvoření instance třídy BasicTools
        self.driver = self.basic_tools.driver  # Získání ovladače
        self.basic_tools.open_html_file(html_file)  # Otevření HTML souboru
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

#Metoda nacte matici dat
#1. sloupec obsahuje jmena prvku
#2. sloupec obsahuje data k vyplneni
    def Fill_strings(self, data):
        for row in data: #Cyklus postupne dohleda a doplni jeden element
            if len(row) != 2:
                self.logger.error("Chyba: Matice musi obsahovat 2 sloupce se jmenem prvku a s daty.")
                return

            name, value = row
            try:
                element = self.driver.find_element(By.NAME, name)
                element.send_keys(value)
            except NoSuchElementException as e:
                self.logger.error(f"Prvek s jménem '{name}' nebyl nalezen:{e}")

    def Button_click(self, name_button):
        try:
            self.driver.find_element(By.NAME, name_button).click()
        except NoSuchElementException as e:
            self.logger.error(f"Prvek s jménem '{name_button}' nebyl nalezen: {e}")


