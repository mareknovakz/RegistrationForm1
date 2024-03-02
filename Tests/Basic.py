#Class definuje zakladni metody pro praci s automatizovanymi nastroji
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import os
import logging

class BasicTools:
    def __init__(self):
        try:
            self.driver = webdriver.Firefox() #Deklarace Firefoxu jako vychoziho prohlizece
            #self.driver = webdriver.Chrome()
            logging.basicConfig(level=logging.INFO)
            self.logger = logging.getLogger(__name__)
        except WebDriverException as e:
          self.logger.error("Nastala chyba pri inicializaci prohlizece {e}")

    #Otevreni html souboru
    def open_html_file(self, file_name):#Na vstupu se definuje testovany html soubor
        try:
            #Pokud se soubor nenachazi v root slozce je nutne misto nazvu zadat jeho relativni cestu
            cwd = os.getcwd()  # aktualni adresar
            path = os.path.join(cwd, file_name)  # Spojuje relativni cestu a absolutni cestu k adresari
            self.driver.get("file:///" + path)  # Otevreni souboru
        except WebDriverException as e:
            self.logger.error("Nastala chyba při otevírání souboru: {e}")

        return self.driver



