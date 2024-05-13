## Employee Database Project

### Objective 
Determine if the learner has completed all requirements for Python 101 and is ready to progress to a higher level by successfully building a robust application.
### Problem
Create an `Employee Management System` that allows users to perform various operations such as adding employees, removing employees, searching for employees, updating employee data, and displaying all employees in the database.
### Implementation
**Data Container** 
- The employee data should be stored in a dictionary `employee_database`.
- The `employee_database` should use the employee **ID** as the `key` and store **employee information in a tuple** (employee position, employee name, employee salary) as `value`.
     
**Check if the ID exists**
- Create a lambda function `id_exists` that takes the **database**(dictionary) and **employee ID** as parameters.
- The function should return true if the employee ID is in the database.  

**Adding an Employee**
- Create a function `add_employee` that takes the **database**(dictionary) and employee details **(employee ID, employee position, employee name , employee salary)** as parameters.
- The **default position** is Trainee.
- The employee `name` and `position` should be **converted to a title case** and the salary should be an absolute value.
- The function should add the employee to the database using the **employee ID** as the key and store a tuple containing employee information **(employee name, employee position, employee salary ) as value**. Print a confirmation message and return the database.

**Removing an Employee**
- Create a function `remove_employee` that takes the **database**(dictionary) and the **employee ID** as parameters.
- Remove the employee from the database, print a confirmation message, and return the database.
        
**Updating Employee Data**
- Create a function `update_employee` that takes the **database**(dictionary), **employee ID**, **new name**,**new position** ,and **new salary** as parameters.
- Create a list`new_data` containing the new name, new position, and new salary.
- Convert the `new_data` to a tuple.
- Using the **employee ID**(key) to update the employee's information by assigning the tuple.
- Print a confirmation message and return the database.
  
**Displaying Employees**
- Create a function `display_employees` that takes the **database**(dictionary) as a parameter.
- Iterate over the database and print each employee's ID, name, position, and salary using (f-string) to create formatted output.
     
**User Interface**
- Create a `while` loop to provide a menu-based interface for interacting with the system.
- Display a menu with options to add an employee, remove an employee, search for an employee, update employee data, display all employees, and exit the program.  
- Based on the user's choice, perform the following actions:
     - If the choice is between 1 and 4 ask the user to enter the employee ID and check if the ID exists by calling the `id_exists` function.
          - If the ID exists and the choice is not 1 call the appropriate function and pass the required parameters, Based on the user's choice.
            
               **a.** If the choice is '2', call the `remove_employee()` function, using keyword arguments.
            
               **b.** If the choice is '3', create a tuple containing the information of the employee ID in the database and print the data.
            
               **c.** If the choice is '4', ask the user to enter the employee information(name, position, salary) the name and position should be converted to a title case, and the salary should be an absolute value and call the `update_employee()` function.
     
          - If the ID doesn't exist and the choice is 1, ask the user to enter the employee information(name, position, salary) and call the `add_employee()` function.
       
          - Any other entrance print "The ID is unavailable"

     - If the choice is '5', call the `display_employees()` function to print the database.
     - If the choice is '6', print "Thank you for using the program. Goodbye!" and break out of the loop.
     - If the user enters an invalid choice, print "Invalid choice. Please try again."
 
  

![edp@4x](https://github.com/SAFCSP-Team/employee-database-project/assets/148013077/079a21ac-9c73-4e93-bb7a-081a7c666cb9)
