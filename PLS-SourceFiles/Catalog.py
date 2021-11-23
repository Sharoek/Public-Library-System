import os.path
import json
import random
from Helper import helper
from Book import *
from LoanItem import *

jsonfilepath = './data/booksset1.json'

class Catalog:
    def __init__(self,username,role,book):
     self.username = username
     self.role = role
     self.book = book
     self.LoanItem = LoanItem(username)


    def instance_Book(self):
        self.book = Book()
        return self.book

    def addBook(self,dict):
        if self.role == 'librarian':
            newdata = self.loadjson()
            newdata.append(dict)
            with open(jsonfilepath, 'w') as f:
                json.dump(newdata, f, indent=1)

    def printtable(self,text):
        bold = '\033[1m'
        endbold = '\033[0m'
        str = bold + text + endbold
        return(str)

    def browse(self):
        book = self.instance_Book()
        data = book.loadBooks()
        i = 0
        while i <= len(data):
            print( self.printtable("Title:"), data[i]['title'])
            print( self.printtable("Author:"), data[i]['author'])
            print( self.printtable("Language:"), data[i]['language'])
            print('\n')
            if i < len(data):
                print('[1] Go to next page')
            if i > 0:
                print('[2] Go back a page')
            print('[3] See book details')
            print('[0] Exit')
            choice = helper.checknumbers(0,3)
            if choice == '3':
                if self.fullbook(data,i) == 0:
                    break
            if choice == '2':
                i-=1
            if choice == '1':
                i+=1
            if choice == '0':
                return 0


    def fullbook(self,l,i):
        borrowed = self.LoanItem.get_Range(l[i]['title'])
        total = str(l[i]['copies'] - borrowed)
        print( self.printtable("Author:"), l[i]['author'])
        print( self.printtable("Country:"), l[i]['country'])
        print( self.printtable("Language:"),l[i]['language'])
        print( self.printtable("Link:"), l[i]['link'])
        print( self.printtable("Pages:"), l[i]['pages'])
        print( self.printtable("Title:"), l[i]['title'])
        print( self.printtable("Year:"), l[i]['year'])
        print( self.printtable("Copies:"), total + '/' ,l[i]['copies'])
        if total == '0':
            print('Unfortunately all the copies have been borrowed ')
        print('\n')

        print('[1] Go back')

        if self.role == 'subscriber' and int(total) > 0:
            print('[2] Loan a copy of this book')
        choice = helper.checknumbers(1,2)
        if choice == '1':
            return 1
        if choice == '2' and self.role == 'subscriber':
            self.LoanItem.add_Copy(l[i]['title'],self.__getRandomid(l,i))
            print('You have sucessfully loaned 1 copy of this book')


    def __getRandomid(self,l,index):
        max = int(l[index]['copies'])
        m = random.randrange(1,max+1)
        randomid = l[index][f'copies_id{m}']
        while self.LoanItem.get_resultOfLoanExistence(randomid):
            m = random.randrange(1,max+1)
            randomid = l[index][f'copies_id{m}']
        return randomid


    def search(self,item):
        book = self.instance_Book()
        data = book.loadBooks()
        itemexist = False
        item = item.upper()
        i = 0
        index = 0
        for i in range(len(data)):
            if item in data[i]['title'].upper() or item == data[i]['author'].upper() or item == data[i]['country'].upper() or item == data[i]['language'].upper():
                index +=1
        i = 0
        j = 1
        while i < len(data):
            if item in data[i]['title'].upper() or item == data[i]['author'].upper() or item == data[i]['country'].upper() or item == data[i]['language'].upper():
                itemexist = True
                print(f"Found: {j}/{index}")
                print( self.printtable("Title:"), data[i]['title'])
                print( self.printtable("Author:"), data[i]['author'])
                print( self.printtable("Language:"), data[i]['language'])
                print('\n')
                if j >= 1 and j < index:
                    print('[1] Go to next page')
                if j <= index and j >= 2:
                    print('[2] Go back a page')
                print('[3] See book details')
                print('[0] Exit')
                choice = helper.checknumbers(0,3)
                if choice == '2' and j > 1:
                    i-=1
                    j-=1
                if choice == '1' and j < index:
                    i+=1
                    j+=1
                if choice == '3':
                    if self.fullbook(data,i) == 0:
                        break
                if choice == '0':
                    return 0
            else:
                i+=1
        if itemexist == False:
            print('The catalog does not contain the search key')



