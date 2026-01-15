class student:
    
    def __init__(self, id, name, mark):
        self.id = id
        self.name = name
        self.mark = mark

    def __str__(self):
        return f"ID : {self.id} | Name : {self.name} | Mark : {self.mark}"

class student_manager:

    def __init__(self):
       self.students = {}

    def add_student(self):

        try:
            id = int(input("enter student's id : "))
            if id in self.students:
                print("id already exists !")
                return 
            name = input("enter name of the student : ")
            mark = float(input("enter mark of the student : "))
            self.students[id] = student(id, name, mark)
            print("student added successfully")

        except ValueError:
            print("invalid input ! please enter correct values !")

    def view_student(self):

        if not self.students:
            print("no student found ! ")
            return 
        print("\n --------------------- student list -------------------------")

        for i in self.students.values():
            print(i)

    def search_student(self):

        try:
            id = int(input("enter student's id : "))
            if id in self.students:
                s = self.students[id]
                print(s)
            else:
                print("not found !")

        except ValueError:
            print("enter a valid id !")

    def update_student(self):
        
        try:
            id = int(input("enter student's id to update : "))
            if id in self.students:
                self.students[id].name = input("enter the name to update : ")
                self.students[id].mark = float(input("enter mark to update : "))
                print("updated successfully !")
            else:
                print("not found !")
        
        except ValueError:
            print("enter valid id !")            

    def delete_student(self):
        
        try:
            id = int(input("enter student's id to delete : "))
            if id in self.students:
                del self.students[id]
                print("student detail deleted successfully !")
            else:
                print("not found !")    
        
        except ValueError:
            print("invalid id !")        

    def save_to_file(self):

        with open("student.txt", 'w') as file:
            for i in self.students.values():
                file.write(f"{i.id},{i.name},{i.mark} \n")

        print("data saved successfully !")
        
    def load_from_file(self):
        
        try:
            with open("student.txt", 'r') as file:
                for i in file:
                    id, name, mark = i.strip().split(",")
                    self.students[int(id)] = student(int(id), name, float(mark))

            print("data loaded successfully !")

        except FileNotFoundError:
            print("no previous data found !")

def main_menu():

    manager = student_manager()
    manager.load_from_file()

    while True:
        print("\n ---------------student management menu-------------------")
        print("1.add student")
        print("2.view student")
        print("3.search student")
        print("4.save to file")
        print("5.update student")
        print("6.delete student")
        print("7.exit")

        choice = input("enter your choice : ")
        if choice == '1':
            manager.add_student()
        elif choice == '2':
            manager.view_student()
        elif choice == '3':
            manager.search_student() 
        elif choice == '4':
            manager.save_to_file()
        elif choice == '5':
            manager.update_student()
        elif choice == '6':
            manager.delete_student()        
        elif choice == '7':
            manager.save_to_file()
            print("exiting program ...........")
            break
        else:
            print("invalid choice!")                   

main_menu()