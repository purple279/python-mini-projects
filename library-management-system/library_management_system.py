class book:
    def __init__(self, id, title, author, genre, orquantity, afquantity):
        self.id = id 
        self.title = title
        self.author = author
        self.genre = genre
        self.orquantity = orquantity
        self.afquantity = afquantity
    def __str__(self):
        return f" {self.id} | {self.title} | {self.author} | {self.genre} | {self.orquantity} | {self.afquantity}"

class book_manager:
    
    def __init__(self):
        self.books = {}
 
    def add_book(self):
        
        try:
            id = int(input("enter id : "))
            if id in self.books:
                print("id already exists")
                return    
            title = input("enter title : ")
            author = input("enter author : ")
            genre = input("enter genre : ")
            orquantity = int(input("enter original quantity : "))
            afquantity = int(input("enter after borrow quantity : "))
            self.books[id] = book(id, title, author, genre, orquantity, afquantity)  
            print("data saved successfully !")
        
        except ValueError:
            print("enter a valid value !")    
    
    def view_book(self):
        if not self.books:
            print("no books found !")
            return
        print("------------------------------------***BOOKS***-----------------------------------------")
        for i in self.books.values():
            print(i)

    def search_book(self):
        
        try:
            id = int(input("enter id to search : "))
            if id in self.books:
                s = self.books[id]
                print(s)
            else:
                print("ID doesn't exist !")    
        
        except ValueError:
            print("enter valid value !")        

    def return_book(self):

        try:
            id = int(input("enter id to return : "))
            if id in self.books:
                s = self.books[id]
                s.afquantity += 1
                print(s)
                print("data saved successfully !")
            else:
                print("ID doesn't exist !")    
        
        except ValueError:
            print("enter valid value !")        

        
    def borrow_book(self):

        try:
            id = int(input("enter id to return : "))
            if id in self.books:
                s = self.books[id]
                if s.afquantity > 0:
                    s.afquantity -= 1
                    print(s)
                    print("data saved successfully !")
                else:
                    print("no books found ! please come later !")    
            else:
                print("ID doesn't exist !")    
        
        except ValueError:
            print("enter valid value !")        


    def update_book(self):
        
        try:
            id = int(input("enter id to update : "))
            if id not in self.books:
                print("id doesn't exist !")
                return    
            print("title, author, genre, original quantity, available quantity")
            s = self.books[id]
            up = input("enter what to change : ")
            if up == 'title':
                title = input("enter title to update : ")
                s.title = title
            elif up == 'author':    
                author = input("enter author : ")
                s.author = author
            elif up == 'genre':    
                genre = input("enter genre : ")
                s.genre = genre
            elif up == 'original quantity':    
                orquantity = int(input("enter original quantity : "))
                s.orquantity = orquantity
            elif up == 'available quantity':    
                afquantity = int(input("enter after borrow quantity : "))
                s.afquantity = afquantity
            else:
                print("requested doesn't match the given words !")      
            print("data saved successfully !")
        
        except ValueError:
            print("enter a valid value !")   

    def delete_book(self):
        
        try:
            id = int(input("enter the id to delete : "))
            if id in self.books:
                del self.books[id]
                print("book deleted successfully !")
            else:
                print("not found !")    
        
        except ValueError:
            print("enter a valid id !")        

    def save_book(self):
        
        with open("book.txt", "w") as file:
            for i in self.books.values():
                file.write(f"{i.id}, {i.title}, {i.author}, {i.genre}, {i.orquantity}, {i.afquantity} \n")

        print("data saved successfully !")         
 
    def load(self):
        
        try:
            with open("book.txt", 'r') as file:
                for i in file:
                    id, title, author, genre, orquantity, afquantity = i.strip().split(',')
                    self.books[int(id)] = book(int(id), title, author, genre, int(orquantity), int(afquantity))
        
        except FileNotFoundError:
            print("no previous data found !")            

def main():

    manager = book_manager()
    manager.load()
    
    while True:
        print("1. add book")
        print("2. view all book")
        print("3. search book")
        print("4. return book")
        print("5. borrow book")
        print("6. update book")
        print("7. delete book")
        print("8. save/load")
        print("9. exit")
        
        choice = input("enter the choice : ")
        if choice == '1':
            manager.add_book()
        elif choice == '2':
            manager.view_book()
        elif choice == '3':
            manager.search_book()
        elif choice == '4':
            manager.return_book()
        elif choice == '5':
            manager.borrow_book()
        elif choice == '6':
            manager.update_book()
        elif choice == '7':
            manager.delete_book()            
        elif choice == '8':
            manager.save_book()    
        elif choice == '9':
            manager.save_book()
            print("exiting program ................. ")
            break
        else:
            print("invalid choice ! please enter correct choice !")

main()

