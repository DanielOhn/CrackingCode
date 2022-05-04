class Book():
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author 
        self.pages = pages
        self.currentPage = 1
    
    def gotoPage(self, page_number):
        self.currentPage = page_number
        return self.currentPage

    def printCurrent(self):
        info = "{0} by {1}.  You are on page {2} out of {3}.".format(self.name, self.author, self.currentPage, self.pages)
        return info


    def __str__(self):
        info = "{0} by {1}.".format(self.name, self.author)
        return info


class Reader():
    def __init__(self):
        self.books = []
        self.selected = None

    def addBook(self, book):
        self.books.append(book)
        return book

    def removeBook(self, book):
        self.books.pop(book)
        return book
    
    def readBook(self, book):
        if book in self.books:
            self.selected = book
        else:
            print("No book bruh")

    def turnPage(self, page):
        # Add +1 or -1 page if just going to next page, else go to the specific page
        if (self.selected != None):
            if (self.selected.pages <= page > 0):
                self.selected.currentPage = page
            else:
                print("Invalid page number.")
        else:
            print("No book selected.")

