## Employee Databases Project

### Objective 
Capstone project for Python 101
### Problem
Create an `Employee Management System` that allows users to perform various operations such as adding employees, removing employees, searching for employees, updating employee data, and displaying all employees in the database.
### Implementation
1. Data Container:
   - The employee data should be stored in a dictionary `employee_database`.
   - The `employee_database` should use the employee **position** as the `key` and store **employee information in a tuple** (employee ID, employee name) as `value`.

2. Adding an Employee:
   - Create a function `add_employee` that takes the **database**(dictionary) and employee details **(employee ID, employee name)** as parameters.
   - The **default ID** is 0.
   - The employee `name` and `position` should be **converted to a title case**.
   - The function should add the employee to the database using the employee **position as the key** and store a tuple containing employee information **(employee ID, employee name) as value**.
   - Print a confirmation message and return the database.

3. Removing an Employee:
   - Create a function `remove_employee` that takes the **database**(dictionary) and the **employee position** as parameters.
   - Check if the employee position exists in the database.
   - **If found**, remove the employee from the database, print a confirmation message, and return the database.
   - If the employee position **is not found** in the database, print an error message and return the database.
     
4. Searching for an Employee:
   - Create a lambda function `search_employee` that takes the **database**(dictionary) and the **employee position** as parameters.
   - Check if the employee position exists in the database.
   - If found, return the employee data.
     
5. Displaying Employees:
   - Create a function `display_employees` that takes the **database**(dictionary) as a parameter.
   - Iterate over the database and print each employee's position, ID, and name using (f-string) to create formatted output.
   
6. Updating Employee Data:
   - Create a function `update_employee` that takes the **database**(dictionary), **employee position**, **new name**, and **new ID** as parameters.
   - Create a list`new_data` containing the new ID and new name.
   - Convert the `new_data` to a tuple.
   - Using the **employee position**(key) Update the employee's information by assigning the tuple.
   - Print a confirmation message and return the database.
     
7. User Interface:
   - Create a `while` loop to provide a menu-based interface for interacting with the system.
   - Display a menu with options to add an employee, remove an employee, search for an employee, display all employees, update employee data, and exit the program.  
   - Based on the user's choice, perform the following actions:
       - If the choice is '1', ask the user to enter the employee information(id, name, position) and call the `add_employee()` function.
       - If the choice is '2', ask the user to enter the employee position to remove (should be converted to a title case) and call the `remove_employee()` function, using keyword arguments.
       - If the choice is '3', ask the user to enter the employee position to search (should be converted to a title case) and call the `search_employee()` function.
           - Check if the tuple employee information that was returned is not empty.
           - If not empty, print the information. Else print an error message.
       - If the choice is 4, call the `display_employees()` function to print the database.
       - If the choice is '5', Check if the employee_position is in the database.
           - If found, ask the user to enter the employee information(id, name, position) the name and position should be converted to a title case then call the `update_employee()` function.
           - If it is not found, print an error message.

       - If the choice is '6', print "Thank you for using the program. Goodbye!" and break out of the loop.
       - If the user enters an invalid choice, print "Invalid choice. Please try again."

![edp@4x](https://github.com/SAFCSP-Team/employee-databases-project/assets/148013077/1f10e4a7-a04d-4558-a374-21f14151e713)
