class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("The books present in library are:  ")
        for book in self.books:
            print("* " +book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Plese keep it safe and return within 30 days.")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry! Either this book is not available or this book is alredy been issued to someone else.\
             Please wait untill the book will available.")
            return False

    def returnBooks(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this book ! Hope you get some valuable things from it !")


class Student:
    
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return or add: ")
        return self.book


if __name__ == "__main__":
    centraLibrary = Library(["Algorithm", "Django", "Clrs", "Python Notes"])
    student = Student()
    centraLibrary.displayAvailableBooks()
    while(True):
        welcomeMsg = ''' \n         ======= Welcome to Central Library ======= 
                Please Choose an Option:
                1. List all the books.
                2. Request a book.
                3. Return/Add a book.
                4. Exit from library.
        '''
        print(welcomeMsg)
        a = int(input("Enter a choice: "))
        if a == 1:
            centraLibrary.displayAvailableBooks()
        elif a == 2:
            centraLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centraLibrary.returnBooks(student.returnBook())
        elif a == 4:
            print("Thanks for Choosing Central Library. Have a great day ahead!")
            exit()
        else:
            print("Invalid choice!")

       