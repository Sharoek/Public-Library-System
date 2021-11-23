import shutil
import os
import uuid
import json
from Book import *
from Helper import helper
from Person import *


jsonfilepath = './data/booksset1.json'
csvmemberfilepath = './data/members.csv'
csvfilepath = './data/loan.csv'



class Librarian(Person):
    def __init__(self, username, role):
        self.username = username
        self.role = role

    def display(self):
        instance = self.init_catalog()
        while True:
            print('###LOGGED IN AS LIBRARIAN###')
            print(f'Welcome {self.username}, what would you like to do?\n\n')
            print("[1] Make Backup")
            print("[2] Restore Backup")
            print("[3] Add a user")
            print("[4] Add a book")
            print("[5] View Catalog")
            print("[6] Search Catalog")
            print("[0] Go back to login")
            choice = helper.checknumbers(0,6)
            if choice == '1':
                self.makeBackup()
            if choice == '2':
                self.restoreBackup()
            if choice == '3':
                self.addPerson()
            if choice == '4':
                self.add_Book()
            if choice == '5':
                instance.browse()
            if choice == '6':
                keyword = input('Search by title or specific author/country/language:\n')
                instance.search(keyword)
            if choice == '0':
                break



    def makeBackup(self):
        print('****Checking all the files****')
        if os.path.isfile('./data/booksset1.json'):
            print('****Making a backup of the catalog****')
            original = './data/booksset1.json'
            target = './data/backupbooksset1.json'
            shutil.copyfile(original, target)
        else:
            print('****FAILED TO MAKE BACKUP OF CATALOG FILE****')

        if os.path.isfile('./data/loan.csv'):
            print('****Making a backup of the borrowed books****')
            original = './data/loan.csv'
            target = './data/backuploan.csv'
            shutil.copyfile(original, target)
        else:
            print('****FAILED TO MAKE BACKUP OF LOAN FILE****')

        if os.path.isfile('./data/members.csv'):
            print('****Making a backup of all the users****')
            original = './data/members.csv'
            target = './data/backupmembers.csv'
            shutil.copyfile(original, target)
            print('****Backup has been made****')
        else:
            print('****FAILED TO MAKE BACKUP OF MEMBER FILE****')

    def restoreBackup(self):
        print('****Checking if there is a backup available****')
        if os.path.isfile('./data/backupbooksset1.json'):
            print('****Backup Available****')
            print('****Restoring now****')
            print('****Restoring the catalog****')
            original = './data/backupbooksset1.json'
            target = './data/booksset1.json'
            shutil.copyfile(original, target)
        else:
            print('****FAILED TO RESTORE CATALOG FILE****')

        if os.path.isfile('./data/backuploan.csv'):
            print('****Restoring of the borrowed books****')
            original = './data/backuploan.csv'
            target = './data/loan.csv'
            shutil.copyfile(original, target)
        else:
            print('****FAILED TO RESTORE LOAN FILE****')

        if os.path.isfile('./data/backupmembers.csv'):
            print('****Restoring of all the users****')
            original = './data/backupmembers.csv'
            target = './data/members.csv'
            shutil.copyfile(original, target)
            print('****System has been restored****')
            print('****DONE****')
        else:
            print('****FAILED TO RESTORE MEMBER FILE****')

    def add_Book(self):
        print('To add a book we need some information')
        author = input('Author:\t')
        country = input('Country:\t')
        imageLink = input('Imagelink:\t')
        language = input('Language:\t')
        link = input('Link:\t')
        pages = helper.checknumbers(1,12000,'Pages:\t')
        title = input('Title:\t')
        Year = helper.checknumbers(1,2021,'Year:\t')
        copies = helper.checknumbers(1,6,'Copies:\t')
        dict =  self.__createDict(author,country,imageLink,language,link,pages,title,Year,copies)
        self.__addtoJSON(dict)
        print('You have succesfully added a book to the catalog')

    def __addtoJSON(self, my_dict):
        b = Book()
        li = b.loadBooks()
        li.append(my_dict)
        with open(jsonfilepath, 'w') as f:
            json.dump(li, f, indent=1)

    def __createDict(self,author, country, imagelink, language, link, pages, title, year, copies):
        book_dict = {
        "author" : author,
        "country" : country,
        "imageLink" : imagelink,
        "language" : language,
        "link" : link,
        "pages" : pages,
        "title" : title,
        "year" : year,
        "copies" : copies
        }
        j = 1
        while j <= int(copies):
            book_dict[f'copies_id{j}'] = str(uuid.uuid4())
            j+=1
        return book_dict


    def addPerson(self):
        print('To register as user you need to fill in a view fields:')
        gender = input('Gender:\t')
        nameset = input('Nationality:\t')
        givenname = input('GivenName:\t')
        surname = input('Surname:\t')
        address = input('StreetAddress:\t')
        zipcode = input('Zipcode:\t')
        city = input('City:\t')
        email = input('Email:\t')
        username = input('Username:\t')
        number = input('TelephoneNumber:\t')
        id = self.random_id()
        print('Role:\n[0] subscriber\n[1] librarian\n')
        choice = helper.checknumbers(0,2)
        if choice == '0':
            role = 'subscriber'
        if choice == '1':
            role = 'librarian'
        while self.checkID(id):
            id = self.random_id()
        personlist= [id, gender,nameset,givenname,surname,address,zipcode,city,email,username,number,role]
        self.addPersonTocsv(personlist)
        print(f'You have successfully registered a {role}')


