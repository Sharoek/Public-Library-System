from LoanAdministration import *

class LoanItem:
    def __init__(self, username):
        self.username = username
        self.LoanAdministration = LoanAdministration(username)

    def get_resultOfLoanExistence(self,id):
        result = self.LoanAdministration.checkLoanitemExist(id)
        return result
    
    def get_Range(self,title):
        result = self.LoanAdministration.getRangeofitem(title)
        return result
    
    def add_Copy(self,book,uuid):
         self.LoanAdministration.addcopyToCSV(book,uuid)        