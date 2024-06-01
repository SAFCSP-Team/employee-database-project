id_exists = lambda db, emp_id : emp_id in db

def add_employees(db , emp_id ,name,salary,postion = 'Trainee'):
    name = name.title()
    postion = postion.title()
    salary = abs(salary)
    db[emp_id] = (name,postion,salary)
    print(f"Employee {emp_id} added successfully")
    return db

def remove_employee(db , emp_id):
    del db[emp_id]
    print(f"Employee {emp_id} removed successfully")
    return db

def update_employee(db , emp_id , new_name , new_postion, new_salary):
    new_data = (new_name.title(),new_postion.title(),abs(new_salary))
    db[emp_id] = new_data
    print(f"Employee {emp_id} updated successfully")
    return db

def display_employees(db):
    if not db:
        print("no employees in database")
    for emp_id, emp_data in db.items():
        print(f"ID:{emp_id}, Name:{emp_data[0]}, Postion{emp_data[1]},Salary{emp_data[2]}")
employee_database = {}

while True:
    print("Menu")
    print("1. Add employee")
    print("2. Remove employee")
    print("3. Search employee")
    print("4. Update employee")
    print("5. Display employees")
    print("6. Exit")

    choice = int(input("enter your choice"))
    if choice in (1,2,3,4):
        id = int(input("enter Id"))
        check_id = id_exists(employee_database , id)
        if check_id == True and choice != 1:

            if choice == 2:
                employee_database = remove_employee(db = employee_database , emp_id= id)
            elif choice == 3:
                employee = employee_database[id]
                print(f"ID: {id} Name: {employee[0]} Postion: {employee[1]} Salary: {employee[2]}")

            elif choice == 4:
                name = input("enter new name")
                postion = input("enter new postion")
                salery = int(input("enter new salery "))
                employee_database = update_employee(employee_database , id , name , postion , salery )

        elif check_id == False and choice == 1:
            name = input("please enter employee name: ")
            postion = input("please enter employees postion: ")
            salery = int(input("please enter employees salery: "))
            if len(postion) == 0:
                employee_database = add_employees(employee_database , id , name , salery)
            else:
                employee_database = add_employees(employee_database, id, name, salery, postion)
        else:
            print("Id exsists")

    elif choice == 5:
        display_employees(employee_database)

    elif choice == 6:
            print("thanks")
            break
    else:
        print("we dont except this kind of argument")


















