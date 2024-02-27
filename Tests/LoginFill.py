#Trida definuje metody pro vyplneni formulare
from Tests.Basic import BasicTools as open

class Fill:
    def __init__(self,file_name):
        open.run_test(self,file_name) #Zajisti travle otevreni okna
        #open.open_html_file(self) #Okno jen "problikne"

    def fill_form(self, username,email, password, password_again): #Na vstupu jsou pozadovana data k vyplneni
        self.driver.find_element_by_id('username').send_keys(username)
        self.driver.find_element_by_id('email').send_keys(email)
        self.driver.find_element_by_id('password').send_keys(password)
        self.driver.find_element_by_id('password_again').send_keys(password_again)