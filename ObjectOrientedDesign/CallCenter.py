#Three Levels Employees: respondent, manager, director

# Data Structure for the Employees 
from contextlib import redirect_stderr


class Employee():
    def __init__(self, status, title):
        self.status = status # Available, Not Available
        self.title = title

# Class for Call Center.  Sets Employees, prints out the current employees, and assigns calls.
class CallCenter():
    def __init__(self):
        self.employees = self.setEmployees()

    def setEmployees(self):
        employees = []
        titles = ["Respondent", "Manager", "Director"]

        for i in range(8):
            e = Employee("Available", titles[0])
            employees.append(e)
        
        e = Employee("Available", titles[1])
        employees.append(e)
        e = Employee("Available", titles[2])
        employees.append(e)

        return employees

    def getEmployees(self):
        for i in self.employees:
            print(i.title, i.status)

    def dispatchCall(self):
        # Assigns call to the first respondent available
        for employee in self.employees():
            if (employee.status == "Available"):
                employee.status = "Unavailable"
                return employee
    
    def redirectCall(self, employee):
        next = ""

        if (employee.title == "Respondent"):
            next = "Manager"
        elif (employee.title == "Manager"):
            next = "Director"
        
        for e in self.employees:
            if (e.title == next and e.status == "Available"):
                return e
            else:
                if (next == "Director"):
                    return None
                self.redirectCall(next)
                


e = CallCenter()
e.getEmployees()