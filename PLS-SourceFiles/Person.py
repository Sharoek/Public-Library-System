import csv
import random
from Catalog import *

csvmemberfilepath = './data/members.csv'
class Person:

    def __init__(self,username, role, catalog):
        self.username = username
        self.role = role
        self.catalog = catalog

    def addPersonTocsv(self,person):
        with open(csvmemberfilepath, 'a', newline='',  encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(person)

    def init_catalog(self):
        self.catalog = Catalog(self.username, self.role, None)
        return self.catalog

    def addPerson(self):
        print('To register as subscriber you need to fill in a view fields:')
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
        role = 'subscriber'
        while self.checkID(id):
            id = self.random_id()
        personlist= [id, gender,nameset,givenname,surname,address,zipcode,city,email,username,number,role]
        self.addPersonTocsv(personlist)
        print('You have been registered as subscriber')

    def random_id(self):
        return random.randrange(1, 99)

    def checkID(self, id):
        with open(csvmemberfilepath, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for i in reader:
                if id in i:
                    return(True)





