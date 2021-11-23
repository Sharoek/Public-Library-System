from Helper import helper
from Book import BookItem
import uuid
import json
import csv
import random
import os

csvmemberfilepath = './data/members.csv'
jsonfilepath = './data/booksset1.json'
csvfilepath = './data/loan.csv'

class datamanagement:
    def display(self):
        while True:
            print('What would you like to do?')
            print('[1] Initiate Database')
            print('[0] Exit')

            choice = helper.checknumbers(0,1)
            if choice == '0':
                break
            if choice == '1':
                Database = BookItem()
                self.initiate_pDatabase()
                Database.loadDatabase()
                self.__addCsvHeader()
                print('###Database initiated###')


    
    def __edit_pDatabase(self):
        l = self.__create_pDatabase()
        fields = ['subscriber', 'librarian']
        i = 0
        for i in range(len(l)):
            if i == 0:
                l[0].append('Role')
            else:
                l[i].append(random.choice(fields))
        return l

    def initiate_pDatabase(self):
        if self.__check_Roles() == False:
            l = self.__edit_pDatabase()
            with open(csvmemberfilepath, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(l)

    def __create_pDatabase(self):
        with open(csvmemberfilepath, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            csv_list = list(reader)
        return csv_list

    def __check_Roles(self):
        li = self.__create_pDatabase()
        try:
            if li[0][11] == 'Role':
                return True
        except:
            return False

    def __checkCSV(self):
            if os.path.isfile(csvfilepath):
                return True
            return False

    def __addCsvHeader(self):
        if self.__checkCSV() == False:
            header = ['Book','UUID','Loandate','Duedate','Borrower']
            with open(csvfilepath, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(header)

   

