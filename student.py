students = ['suyash']

def show_menu():
    print('-' * 40)
    print("   STUDENT MANAGEMENT SYSTEM   ")
    print('_' * 40)
    print("\n1. Show students")
    print("2. Add student")
    print("3. Find student")
    print("4. Remove student")
    print("5. Exit")

def show():
    print("Students List:", students)

def add():
    for_add = input("Enter student name: ").lower()
    students.append(for_add)
    print(f"{for_add} added successfully")

def find():
    to_find = input("Enter student name: ").lower()
    if to_find in students:
        print(f"{to_find} is in the list")
    else:
        print(f"{to_find} is not in the list")

def rem():
    for_remove = input("Enter student name: ").lower()
    if for_remove in students:
        students.remove(for_remove)
        print(f"{for_remove} removed successfully")
    else:
        print(f"{for_remove} is not in the list")

while True:
    show_menu()
    choice = input("Enter number between 1 to 5: ")

    if choice == "1":
        show()
    elif choice == "2":
        add()
    elif choice == "3":
        find()
    elif choice == "4":
        rem()
    elif choice == "5":
        print("Thank you for using system!")
        break
    else:
        print("Invalid number, please try again")