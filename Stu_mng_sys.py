students = []

def add_students():
    count = int(input("Enter no.of Students you want to Enter: "))
    for i in range(count):
        student_id = int(input("Enter Student Id: "))
        student_name = input("Enter Student Name: ")
        student_class =input("Enter Student Class: ")
        for student in students:
            if student["id"] == student_id:
                print("Students Already Exists!")
                break
        else:
            add_data = {
                "id" : student_id,
                "name" : student_name,
                "class" : student_class
            }
        students.append(add_data)
        print("Data Entered Successfully!")
def show_students():
    if len(students) == 0:
        print("No student Found!")
        return
    for student in students:
        print("ID", student["id"] )
        print("Name", student["name"] )
        print("Class", student["class"] )
        print("----------------------------")
def search_student():
    search = int(input("Enter id you want to search student: "))
    found = False
    for student in students:
        if student["id"] == search:
            print("Student Found")
            print(student)
            found = True
            break
    if found == False:
        print("Student NOt found!")
def remove_student():
    rem = int(input("Enter Id you want to remove student: "))
    for student in students:
        if student["id"] == rem:
            students.remove(student)
            print("Student remove successfully!")
            return
    print("Student not found!")
    
while True:
    print("\n Student Management System\n")
    print("1. Add student")
    print("2. show student")
    print("3. search student")
    print("4. remove student")
    choice = input("Enetr your choice: ")
    if choice == "1":
        add_students()
    elif choice == "2":
        show_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        remove_student()
    elif choice == "5":
        print("Exiting program!")
        break
    else:
        print("invalid choice")
