class Book:
    def __init__(self,title,author,no_of_copies):
        self.title = title
        self.author = author
        self.no_of_copies = no_of_copies
        self.borrowed = []


    def display_details(self):
        print("Title of the book : ",self.title," \n Author : ", self.author,"\n No. of Available Copies: ", self.no_of_copies)

    def is_book_available(self):
         if self.no_of_copies:
            print("Yes , Book is Available")
         else:
             print("No")
    
    def borrow_book(self):
        if self.no_of_copies:
            self.borrowed.append(self)
            self.no_of_copies -= 1
            print("Book is borrowed")
        else:
            print("Book is not available")
    
    def return_book(self):
        if self in self.borrowed:
            self.borrowed.remove(self)
            self.no_of_copies -=1
            print("Book is returned")
        else:
            print("Book is not Borrowed")


class Library:
    def __init__(self):
        self.books = []
        self.members = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def remove_book(self, book):
        self.books.remove(book)

    def display_books(self):
        if self.books:
            print("Available Books are :")
            for i in self.books:
                print(i)
        else:
            print("No Books Available")

    def add_member(self,name):
        self.members.append(name)

    def remove_member(self,name):
        self.members.remove(name)
        
    def display_members(self):
        if self.members:
            print("Available Members are :")
            for i in self.members:
                print(i)
        else:
            print("No members Available")


class Member:
    def __init__(self,mem_id,name):
        self.name = name
        self.mem_id = mem_id
        self.is_subscribed = False
        
        
    def add_membership(self):
        if self.is_subscribed:
            print("Already Subscribed")
        else:

            self.is_subscribed = True
            print("Membership is Added")

    def remove_membership(self):
        if self.is_subscribed:
           
            self.is_subscribed = False
            print("Membership is Removed")
        else:
            print(" There is no Subscription")
        
   
l = Library()
m1 = Member(1234567,"John")
m1.add_membership()
l.add_member("John")
m2 = Member(2345678,"Ria")
m2.add_membership()
l.add_member("Ria")

b1 = Book("Wings of Fire", " Dr. Abdul Kalam",34)
l.add_book("Wings of Fire")
b2 = Book("Gitanjali", " Rabindranth Tagore",20)
l.add_book("Gitanjali")


l.display_books() 
l.display_members()       
    