
class book:
    def __init__(self, title, author, genre, year_published):
        self.title = title
        self.author = author
        self.genre = genre
        self.year_published = year_published
    def makebook(self):
        return f"The book is called {self.title}. \nThe author of this book is {self.author}. \nThe Genre is {self.genre}.\nIt was published in {self.year_published}"
WOT10C = book("War Of The 10 Cheeses", "Martin Notchess", "Action", "2057")
def main():
    library = []
    Booknum = 0
    while True:
        Booknum += 1
        curyear = int(input("What year has existence happened at the moment that your input is being entered into this program?\n"))
        maketitle = input("What is the title of the book?\n")
        makeauthor = input("Who is the author?\n")
        makegenre = input("What is the genre?\n")
        makeyear = int(input("What year was it published in?\n"))
        newbook = book(maketitle, makeauthor, makegenre, makeyear)
        print(newbook.makebook())
        if makeyear < curyear - 50:
            print("This book is OLD")
        yes = input("Would you like to continue?(yes or no)\n")
        library.append(f"This is book number {Booknum} Title : {newbook.title} Author : {newbook.author} Genre : {newbook.genre} Year Published : {newbook.year_published}")
        if yes == "yes":
            continue
        else:
            no = input("Would you like to see all the books?(yes or no)\n")
            if no == "yes":
                print(library)
            break
main()