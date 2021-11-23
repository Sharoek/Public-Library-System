import os.path
import json
import random
import uuid
jsonfilepath = './data/booksset1.json'

class Book:
    #Every item is a book
    def __init__(self):
        pass

    def loadBooks(self):
        with open(jsonfilepath, encoding='utf-8') as f:
            data = json.load(f)
            return data

    def random_gen(self):
        return random.randrange(2, 7)

class BookItem(Book):
    #a book can have multiple copies
    #Wat heeft een BOokitem , = copies amount en copie ID 

    def loadDatabase(self):
        b = self.__createDatabase()
        with open(jsonfilepath, mode='w') as f:
            json.dump(b, f, indent=1)
    
    def __createDatabase(self):
        book = self.loadBooks()
        i = 0
        for i in range(len(book)):
            j = 1
            book[i]['link'] = book[i]['link'].replace("\n", "")
            book[i]['copies'] = self.random_gen()
            while j <= int(book[i]['copies']):
                book[i][f'copies_id{j}'] = str(uuid.uuid4())
                j+=1

        return book





