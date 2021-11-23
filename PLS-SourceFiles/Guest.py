from Helper import helper
from Person import *

class Guest(Person):
    def __init__(self, username, role):
        self.username = username
        self.role = role

    def display(self):
        instance = self.init_catalog()
        while True:
            print("\n\n**LOGGED IN AS GUEST***")
            print("\n\nWhat would you like to do?")
            print('[1] Browse Catalog')
            print('[2] Search Catalog')
            print('[3] Register as Subscriber')
            print('[0] Logout')
            choice = helper.checknumbers(0,5)
            if choice == '0':
                break
            if choice == '1':
                instance.browse()
            if choice == '2':
                keyword = input('Search by title or specific author/country/language:\n')
                instance.search(keyword)
            if choice == '3':
                self.addPerson()


