import datetime 

def add_expanse(amt, cat):
    date = datetime.date.today()
    with open("expanses.txt", "a") as file:
        file.write(f"{date},{amt},{cat}\n")
    print("expanses added successfully")

def view_expanses():
    total = 0
    try:
        with open("expanses.txt", "r") as file:
            for i in file:
                if i.count(",") != 2:
                    continue
                date, amount, category = i.strip().split(",")
                total += float(amount)
                print(f"{date} | {category} | ₹{amount}\n")
            print("total expanses :₹",total)    
    except FileNotFoundError:
        print("file not found error !")    

while True:
    print("1.Add expenses")
    print("2.View expanses")
    print("3.Exit")
    choice = input('enter the choice: ')
    if choice == '1':
        amt = float(input("enter the amount: "))
        cat = input("enter the category: ")
        add_expanse(amt, cat)
    elif choice == '2':
        view_expanses()
    elif choice == '3':
        break
    else:
        print("invalid choice !")        
