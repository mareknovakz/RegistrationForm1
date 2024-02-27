#Prostredi vyhrazene pro provolavani automatu
from Tests.LoginFill import Fill
from Tests.Basic import BasicTools

#bt = BasicTools()
#bt.run_test('RegistrationForm.html')

fi = Fill('RegistrationForm.html')
fi.fill_form('test','test@test.com','testpass','testpass')
