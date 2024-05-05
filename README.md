## Employee Database Project

### Objective 
Capstone project for Python 101
### Problem
Create an `Employee Management System` that allows users to perform various operations such as adding employees, removing employees, searching for employees, updating employee data, and displaying all employees in the database.
### Implementation
1. Data Container:
   - The employee data should be stored in a dictionary `employee_database`.
   - The `employee_database` should use the employee **ID** as the `key` and store **employee information in a tuple** (employee position, employee name, employee salary) as `value`.

2. Adding an Employee:
   - Create a function `add_employee` that takes the **database**(dictionary) and employee details **(employee ID, employee position, employee name , employee salary)** as parameters.
   - The **default position** is Trainee.
   - The employee `name` and `position` should be **converted to a title case** and the salary should be an absolute value.
   - If the employee ID does not exist in the database add the employee to the database using the **employee ID** as the key and store a tuple containing employee information **(employee position, employee name, employee salary ) as value**. Print a confirmation message and return the database.
   - Else if the employee ID does exist in the database print an error message and return the database.

3. Removing an Employee:
   - Create a function `remove_employee` that takes the **database**(dictionary) and the **employee ID** as parameters.
   - Check if the employee ID  exists in the database.
   - **If found**, remove the employee from the database, print a confirmation message, and return the database.
   - If the employee ID  **is not found** in the database, print an error message and return the database.
     
4. Searching for an Employee:
   - Create a lambda function `search_employee` that takes the **database**(dictionary) and the **employee ID** as parameters.
   - Check if the employee ID  exists in the database.
   - If found, return the employee data.
     
5. Displaying Employees:
   - Create a function `display_employees` that takes the **database**(dictionary) as a parameter.
   - Iterate over the database and print each employee's position, ID, name, and salary using (f-string) to create formatted output.
   
6. Updating Employee Data:
   - Create a function `update_employee` that takes the **database**(dictionary), **employee ID**, **new name**,**new salary** ,and **new position** as parameters.
   - Create a list`new_data` containing the new position, new salary, and new name.
   - Convert the `new_data` to a tuple.
   - Using the **employee ID **(key) Update the employee's information by assigning the tuple.
   - Print a confirmation message and return the database.
     
7. User Interface:
   - Create a `while` loop to provide a menu-based interface for interacting with the system.
   - Display a menu with options to add an employee, remove an employee, search for an employee, display all employees, update employee data, and exit the program.  
   - Based on the user's choice, perform the following actions:
       - If the choice is '1', ask the user to enter the employee information(id, name, position, salary) and call the `add_employee()` function.
       - If the choice is '2', ask the user to enter the employee ID  to remove and call the `remove_employee()` function, using keyword arguments.
       - If the choice is '3', ask the user to enter the employee ID  to search and call the `search_employee()` function.
           - Check if the tuple employee information that was returned is not empty.
           - If not empty, print the information. Else print an error message.
       - If the choice is 4, call the `display_employees()` function to print the database.
       - If the choice is '5', Check if the employee_ID is in the database.
           - If found, ask the user to enter the employee information(name, position, salary) the name and position should be converted to a title case then call the `update_employee()` function.
           - If it is not found, print an error message.

       - If the choice is '6', print "Thank you for using the program. Goodbye!" and break out of the loop.
       - If the user enters an invalid choice, print "Invalid choice. Please try again."

![edp@4x](https://github.com/SAFCSP-Team/employee-databases-project/assets/148013077/1f10e4a7-a04d-4558-a374-21f14151e713)
