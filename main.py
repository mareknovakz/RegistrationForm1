#Prostredi vyhrazene pro provolavani automatu
from Tests.LoginFill import Fill
from Tests.Basic import BasicTools

BT = BasicTools()
BT.run_test('RegistrationForm.html')

#testing_page = Fill('RegistrationForm.html')
#Fill.fill_form('test','test@test.cz','heslo123','heslo1234')