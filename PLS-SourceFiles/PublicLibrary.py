from Helper import helper
from DataManagement import *
from Login import *

class PublicLibrary:
    def __init__(self):
        self.role = 'guest'
        self.login = Login('guest')

    def welcome(self):
        while True:
            print("###WELCOME TO SHAROEK PLS###")
            print("\nPlease login\n")
            print("[1] login as a guest")
            print("[2] login as a librarian")
            print("[3] login as a subscriber")
            print("[4] Data Management")
            print("[0] Exit the program")

            choice = helper.checknumbers(0,5)
            self.check_choice(choice)

    def check_choice(self,ch):
        if ch == '0':
            exit()
        elif ch == '1':
            self.login.display()
        elif ch == '2':
            self.login = Login('librarian')
            self.login.display()
        elif ch == '3':
            self.login = Login('subscriber')
            self.login.display()
        elif ch == '4':
            d = datamanagement()
            x = d.display()

    if __name__ == '__main__':
       welcome()
    







