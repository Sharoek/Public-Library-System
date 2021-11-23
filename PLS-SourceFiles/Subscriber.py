from Person import *
from LoanAdministration import *
from Helper import helper

class Subscriber(Person):
    def __init__(self, username, role):
        self.username = username
        self.role = role

    def display(self):
        instance = self.init_catalog()
        while True:
            print('###LOGGED IN AS SUBSCRIBER###')
            print(f'Welcome {self.username}, how can we help you?\n\n')
            print("[1] View Catalog")
            print("[2] Search Catalog")
            print("[3] Return a book")
            print("[0] Go back to login")
            choice = helper.checknumbers(0,3)
            if choice == '1':
                instance.browse()
            if choice == '2':
                keyword = input('Search by title or specific author/country/language:\n')
                instance.search(keyword)
            if choice == '3':
                l = LoanAdministration(self.username)
                l.returnaBook()
            if choice == '0':
                break
