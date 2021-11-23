from Guest import *
from Subscriber import *
from Librarian import *


class User:
    def __init__(self, username):
        self.username = username
        self.Guest = Guest(username, 'guest')
        self.Subsriber = Subscriber(username, 'subscriber')
        self.Librarian = Librarian(username, 'librarian')
    
    def guestDisplay(self):
        return Guest.display(self.Guest)
    
    def subcriberDisplay(self):
        return Subscriber.display(self.Subsriber)

    def librarianDisplay(self):
        return Librarian.display(self.Librarian)