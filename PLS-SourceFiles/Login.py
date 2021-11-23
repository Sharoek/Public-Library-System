import csv
from User import *

csvmemberfilepath = './data/members.csv'

class Login:
    def __init__(self,role):
        self.role = role
        self.user = User('guest')


    def display(self):
        while True:
            if self.role == 'guest':
                self.user.guestDisplay()
                break
            else:
                print(f'Please login as {self.role} with your username and email:\n')
                username = input('Username:\t')
                email = input('Email:\t')
                output = self.__userLogin(username, email)
                if output:
                    if self.role == 'subscriber':
                        self.user = Subscriber(username,self.role)
                        self.user.display()
                        break
                    elif self.role == 'librarian':
                        self.user = User(username)
                        self.user.Librarian.display()
                        break
                else:
                    print('Wrong Login')
                    break

    def __userLogin(self, username, email):
        xlist = self.__readCSV()
        i = 1
        foundmember = False
        try:
            for i in range(len(xlist)):
                if self.role == xlist[i][11] and username == xlist[i][9] and email == xlist[i][8]:
                    foundmember = True
        except:
                print('Please load the database first')
        return foundmember

    def __readCSV(self):
        with open(csvmemberfilepath, 'r', newline='',  encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            x = list(reader)
        return x

