from Tests.LoginFill import Fill
import os
from Tests.Basic import BasicTools
# data pro formulář
LoginData = [
    ["username", "test123"],
    ["email", "test@test.com"],
    ["password", "heslo123"],
    ["confirm-password", "heslo123"]
]

#testovany html soubor
file = "RegistrationForm.html" #V pripade, ze by se Registration.html nachazel jinde je nutne pouzit relativni cestu

fill_instance = Fill(file)
fill_instance.Fill_strings(LoginData)
fill_instance.Button_click("submit")

