# ---------------------------------------------------------
# Final Project - Employee Management System
# Uses: Final Project Employees.txt
# ---------------------------------------------------------

class Employee:
    def __init__(self, emp_num, first, last, address, city, state, zip_code):
        self.emp_num = int(emp_num)
        self.first = first
        self.last = last
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip_code


class EmployeeList:
    def __init__(self, filename):
        self.filename = filename
        self.employees = []
        self.ReadEmployeeFile()

    # ---------------------------------------------------------
    # Load Employees from File
    # ---------------------------------------------------------
    def ReadEmployeeFile(self):
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    fields = [x.strip() for x in line.split(",")]
                    if len(fields) == 7:
                        emp = Employee(*fields)
                        self.employees.append(emp)
        except FileNotFoundError:
            print("File not found. Starting with an empty list.")

    # ---------------------------------------------------------
    # Save Employees to File
    # ---------------------------------------------------------
    def WriteEmployeeFile(self):
        with open(self.filename, "w") as file:
            for emp in self.employees:
                file.write(f"{emp.emp_num}, {emp.first}, {emp.last}, {emp.address}, "
                           f"{emp.city}, {emp.state}, {emp.zip}\n")
        print("Changes Saved")

    # ---------------------------------------------------------
    # Display All Employees
    # ---------------------------------------------------------
    def DisplayEmployeeList(self):
        print("\nEmployee Number  First Name     Last Name      Address           City            State   Zip")
        print("-" * 90)
        for e in self.employees:
            print(f"{e.emp_num:<16}{e.first:<15}{e.last:<15}{e.address:<18}{e.city:<15}{e.state:<8}{e.zip}")
        print()

    
            if emp.emp_num == emp_num:
                return i
        return -1

    # ---------------------------------------------------------
    # Next employee number
    # ---------------------------------------------------------
    def NextEmployeeNumber(self):
        if not self.employees:
            return 1
        return self.employees[-1].emp_num + 1

    # ---------------------------------------------------------
    # Add employee
    # ---------------------------------------------------------
    def AddEmployee(self, first, last, address, city, state, zip_code):
        emp_num = self.NextEmployeeNumber()
        new_emp = Employee(emp_num, first, last, address, city, state, zip_code)
        self.employees.append(new_emp)
        print("Employee Added")

    # ---------------------------------------------------------
    # Delete employee
    # ---------------------------------------------------------
    def DeleteEmployee(self, emp_num):
        index = self.FindEmployee(emp_num)
        if index == -1:
            print("Error: Employee Not Found")
        else:
            del self.employees[index]
            print("Employee Deleted")

    # ---------------------------------------------------------
    # Update employee
    # ---------------------------------------------------------
    def UpdateEmployee(self, emp_num):
        index = self.FindEmployee(emp_num)
        if index == -1:
            print("Error: Employee Not Found")
            return

        emp = self.employees[index]

        while True:
            print("\n(F)irst Name")
            print("(L)ast Name")
            print("(A)ddress")
            print("(C)ity")
            print("(S)tate")
            print("(Z)ip")
            print("(B)ack to Main Menu")
            choice = input("\nEnter Selection: ").upper()

            if choice == "F":
                emp.first = input("Enter First Name: ")
            elif choice == "L":
                emp.last = input("Enter Last Name: ")
            elif choice == "A":
                emp.address = input("Enter Address: ")
            elif choice == "C":
                emp.city = input("Enter City: ")
            elif choice == "S":
                st = input("Enter State (2 letters): ").upper()
                if len(st) == 2 and st.isalpha():
                    emp.state = st
                else:
                    print("Invalid State!")
            elif choice == "Z":
                z = input("Enter Zip (5 digits): ")
                if len(z) == 5 and z.isdigit():
                    emp.zip = z
                else:
                    print("Invalid Zip Code!")
            elif choice == "B":
                break
            else:
                print("Invalid Entry")


# ---------------------------------------------------------
# MAIN MENU
# ---------------------------------------------------------
def main():
    employees = EmployeeList("Final Project Employees.txt")

    while True:
        print("(A)dd a New Employee")
        print("(D)elete an Existing Employee")
        print("(C)hange an Existing Employee")
        print("(P)rint All Employees")
        print("(S)ave Changes to File")
        print("(Q)uit")
        choice = input("\nEnter Selection: ").upper()

        if choice == "A":
            first = input("Enter First Name: ")
            last = input("Enter Last Name: ")
            address = input("Enter Address: ")
            city = input("Enter City: ")
            state = input("Enter State: ").upper()
            zip_code = input("Enter Zip: ")
            employees.AddEmployee(first, last, address, city, state, zip_code)

        elif choice == "D":
            try:
                emp_num = int(input("Enter Employee Number: "))
                employees.DeleteEmployee(emp_num)
            except ValueError:
                print("Invalid Number")

        elif choice == "C":
            try:
                emp_num = int(input("Enter Employee Number: "))
                employees.UpdateEmployee(emp_num)
            except ValueError:
                print("Invalid Number")

        elif choice == "P":
            employees.DisplayEmployeeList()

        elif choice == "S":
            employees.WriteEmployeeFile()

        elif choice == "Q":
            print("Good-bye")
            break

        else:
            print("Invalid Selection\n")


main()