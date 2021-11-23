from datetime import date
from datetime import timedelta
from Book import *
from Helper import *
csvfilepath = './data/loan.csv'
import csv


class LoanAdministration:
    def __init__(self,username):
        self.duedate = None
        self.loandate = None
        self.username = username

    def addcopyToCSV(self,book, uuid):
        self.loandate = date.today()
        self.duedate = self.loandate + timedelta(days=21)
        loanlist = [book, uuid, str(self.loandate), str(self.duedate),self.username]
        self.__addLoanitem(loanlist)

    def getRangeofitem(self, title):
        total = 0
        x = self.__openCSV()
        i = 0
        for i in range(len(x)):
            if title == x[i][0]:
                total+=1
        return total

    def __addLoanitem(self, list):
        with open(csvfilepath, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(list)

    def checkLoanitemExist(self,item):
        x = self.__openCSV()
        i = 0
        for i in range(len(x)):
            #UUID
            if item == x[i][1]:
                return True
        return False

    def __openCSV(self):
        with open(csvfilepath, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            x = list(reader)
        return x

    def printtable(self,text):
        bold = '\033[1m'
        endbold = '\033[0m'
        str = bold + text + endbold
        return(str)

    def returnaBook(self):
        x = self.__openCSV()
        i = 0
        total = 1
        foundcopie = False
        id = False
        for i in range(len(x)):
            if x[i][4] == self.username:
                print( self.printtable("Title:"), x[i][0])
                print( self.printtable("UUID:"), x[i][1])
                print( self.printtable("Loandate:"),x[i][2])
                print( self.printtable("Duedate:"),x[i][3])
                total +=1
                print('\n')
                foundcopie = True
            i+=1
        if foundcopie == False:
            print('You have not borrowed anything yet')
        print('[0] Go back')
        if foundcopie == True:
            print('[1] Return a book')
        choice = helper.checknumbers(0,1)
        if choice == '1' and foundcopie == True:
            choice = input('Please use the UUID\t')
            for i in range(len(x)):
                if x[i][1] == choice:
                    l = list(filter(lambda x:x[1] != choice,x))
                    with open(csvfilepath, 'w', newline='') as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerows(l)
                    print('You have succesfully returned a copie\n')
                    id = True
                    break
            if id == False:
                print('Wrong UUID')
        if choice == '0':
            return 0



