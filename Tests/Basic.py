#Class definuje zakladni metody pro praci s automatizovanymi nastroji
from selenium import webdriver
import os

class BasicTools:
    def __init__(self):
        self.driver = webdriver.Firefox() #Definuje

    def open_html_file(self, file_name):#Na vstupu se definuje testovany html soubor
        current_directory = os.path.dirname(__file__) #Definuje cestu
        file_path = os.path.join(current_directory, '..', file_name) #Nalezne absolutni cestu k souboru na disku
        self.driver.get('file://' + file_path)# "secte" absolutni cestu ke slozce s cestou relativni,

    def run_test(self,file_name):
        self.open_html_file(file_name) #Zajisti trvale otevreni prohlizece Firefox


