# ============================================
# Final Project - Employee Management System
# ============================================

import os

# --------------------------
# Employee Class
# --------------------------
class Employee:
    def __init__(self, emp_num, first, last, address, city, state, zip_code):

        # Validation
        if not isinstance(emp_num, int):
            raise ValueError("Employee Number must be an integer")

        if state.upper() not in valid_states:
            raise ValueError("Invalid state code")

        if not zip_code.isdigit() or len(zip_code) != 5:
            raise ValueError("Zip must be 5 digits")

        # Attributes
        self.emp_num = emp_num
        self.first = first.strip()
        self.last = last.strip()
        self.address = address.strip()
        self.city = city.strip()
        self.state = state.upper().strip()
        self.zip = zip_code.strip()


# Valid states
valid_states = {
    "AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA",
    "KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ",
    "NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT",
    "VA","WA","WV","WI","WY"
}


# --------------------------
# EmployeeList Class
# --------------------------
class EmployeeList:
    def __init__(self, filename):
        self.filename = filename
        self.employees = []
        self.ReadEmployeeFile()

    # Read the employee file
    def ReadEmployeeFile(self):
        if not os.path.exists(self.filename):
            return  # Start with empty list if file doesn't exist

        with open(self.filename, "r") as file:
            for line in file:
                data = [x.strip() for x in line.split(",")]
                if len(data) != 7:
                    continue

                emp_num = int(data[0])
                emp = Employee(emp_num, data[1], data[2], data[3], data[4], data[5], data[6])
                self.employees.append(emp)

    # Write employees to file
    def WriteEmployeeFile(self):
        with open(self.filename, "w") as file:
            for e in self.employees:
                file.write(f"{e.emp_num}, {e.first}, {e.last}, {e.address}, {e.city}, {e.state}, {e.zip}\n")

    # Display all employees
    def DisplayEmployeeList(self):
        print("\nEmployee        First           Last            Address         City            State           Zip")
        print("Number          Name            Name")
        print("--------------- --------------- --------------- --------------- --------------- --------------- ---------------")

        for e in self.employees:
            print(f"{e.emp_num:<15}{e.first:<15}{e.last:<15}{e.address:<15}{e.city:<15}{e.state:<15}{e.zip:<15}")

    # Find employee index by number
    def FindEmployee(self, emp_num):
        for i, e in enumerate(self.employees):
            if e.emp_num == emp_num:
                return i
        return -1

    # Return next employee number
    def NextEmployeeNumber(self):
        if not self.employees:
            return 1
        return self.employees[-1].emp_num + 1

    # Read employee data
    def ReadEmployee(self, emp_num):
        idx = self.FindEmployee(emp_num)
        if idx == -1:
            return None
        e = self.employees[idx]
        return e.emp_num, e.first, e.last, e.address, e.city, e.state, e.zip

    # Add employee
    def AddEmployee(self, first, last, address, city, state, zip_code):
        new_num = self.NextEmployeeNumber()
        e = Employee(new_num, first, last, address, city, state, zip_code)
        self.employees.append(e)

    # Update employee
    def UpdateEmployee(self, emp_num, first, last, address, city, state, zip_code):
        idx = self.FindEmployee(emp_num)
        if idx == -1:
            return False

        self.employees[idx] = Employee(emp_num, first, last, address, city, state, zip_code)
        return True

    # Delete employee
    def DeleteEmployee(self, emp_num):
        idx = self.FindEmployee(emp_num)
        if idx == -1:
            return False
        del self.employees[idx]
        return True


# ============================================
# MAIN PROGRAM LOOP
# ============================================

def main():

    emp_list = EmployeeList("Final Project Employees.txt")

    while True:
        print("\n(A)dd a New Employee")
        print("(D)elete an Existing Employee")
        print("(C)hange an Existing Employee")
        print("(P)rint All Employees")
        print("(S)ave Changes to File")
        print("(Q)uit")

        choice = input("\nEnter Selection: ").upper()

        # ADD EMPLOYEE
        if choice == "A":
            first = input("Enter First Name: ").strip()
            last = input("Enter Last Name: ").strip()
            address = input("Enter Address: ").strip()
            city = input("Enter City: ").strip()
            state = input("Enter State: ").strip().upper()
            zip_code = input("Enter Zip: ").strip()

            try:
                emp_list.AddEmployee(first, last, address, city, state, zip_code)
                print("Employee Added")
            except Exception as e:
                print("Error:", e)

        # DELETE EMPLOYEE
        elif choice == "D":
            num = int(input("Enter Employee Number: "))
            if emp_list.DeleteEmployee(num):
                print("Employee Deleted")
            else:
                print("Employee Number not found")

        # CHANGE EMPLOYEE
        elif choice == "C":
            num = int(input("Enter Employee Number: "))
            idx = emp_list.FindEmployee(num)

            if idx == -1:
                print("Employee not found")
                continue

            e = emp_list.employees[idx]

            while True:
                print("\n(F)irst Name")
                print("(L)ast Name")
                print("(A)ddress")
                print("(C)ity")
                print("(S)tate")
                print("(Z)ip")
                print("(B)ack to Main Menu")

                c2 = input("Enter Selection: ").upper()

                if c2 == "F":
                    e.first = input("Enter First Name: ")

                elif c2 == "L":
                    e.last = input("Enter Last Name: ")

                elif c2 == "A":
                    e.address = input("Enter Address: ")

                elif c2 == "C":
                    e.city = input("Enter City: ")

                elif c2 == "S":
                    new_state = input("Enter State: ").upper()
                    if new_state in valid_states:
                        e.state = new_state
                    else:
                        print("Invalid state")

                elif c2 == "Z":
                    new_zip = input("Enter Zip: ")
                    if new_zip.isdigit() and len(new_zip) == 5:
                        e.zip = new_zip
                    else:
                        print("Zip must be 5 digits")

                elif c2 == "B":
                    break

        # PRINT EMPLOYEES
        elif choice == "P":
            emp_list.DisplayEmployeeList()

        # SAVE TO FILE
        elif choice == "S":
            emp_list.WriteEmployeeFile()
            print("Changes Saved")

        # QUIT
        elif choice == "Q":
            print("Good-bye")
            break

        else:
            print("Invalid selection.")


# Run program
main()
