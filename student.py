FILENAME = "Final Project employees.txt"

class Employee:
    def __init__(self, employeenumber, first, last, address, city, state, zip):
        self.employeenumber = int(employeenumber)
        self.first = first 
        self.last = last 
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip 

class EmployeeList:
    def __init__(self, filename):
        self.EmployeeList = []
        self.FileName = filename

    def UpdateEmployee(self, employeenumber, first, last, address, city, state, zip):
        index = self.FindEmployee(employeenumber)

        if index == -1:
            print("Errer: Employee does not Exist")
        else:
            self.EmployeeList[index].FirstName = first
            self.EmployeeList[index].LastName = last
            self.EmployeeList[index].Address = address
            self.EmployeeList[index].City = city
            self.EmployeeList[index].State = state
            self.EmployeeList[index].Zip = zip 

            print("Employee Updated")
    
    def AddEmployee(self, first, last, address, city, state, zip):
        employeenumber = self.NextEmployeeNumber()

        emp = Employee(employeenumber, first, last, address, city, state, zip)
        self.EmployeeList.append(emp)

        print("Employee Added")

    def ReadEmployeeFile(self):
        try:
            file = open(self.FileName, "r")

            for line in file:
                line = line.strip()

                if line != "":
                    data = line.split(",")

                    emp = Employee(
                        int(data[0].strip()),
                        data[1].strip(),
                        data[2].strip(),
                        data[3].strip(),
                        data[4].strip(),
                        data[5].strip(),
                        data[6].strip()
                    )
                    self.EmployeeList.append(emp)
            file.close()
        except FileNotFoundError:
            print("Employee file not found. Starting with empty list.")
    def WriteEmployeeFile(self):
        file = open(self.FileName, "w")

        for emp in self.EmployeeList:
            file.write(
                str(emp.EmployeeNumber) + "," +
                emp.FirstName + "," +
                emp.LastName + "," +
                emp.Address + "," +
                emp.City +","+
                emp.State +","+
                emp.Zip +"\n" 
            )
        file.close()
        print("Changes Saved to File")

    def DisplayEmployeeList(self): 
        print(f"{'Employee Number':<15}{'First':<12}{'Last':<12}{'Address':<28}{'City':<18}{'State':<24}{'Zip':<8}")
        print("-" *110)

        for emp in self.EmployeeList:
            print(
                f"{emp.employeenumber:<8}"
                f"{emp.first:<12}"
                f"{emp.last:<12}"
                f"{emp.address:<28}"
                f"{emp.city:<18}"
                f"{emp.state:<24}"
                f"{emp.zip:<8}"
            )
        def ReadEmployee(self, employeenumber):
            index = self.FindEmployee(employeenumber)

            if index == -1:
                return None
            else:
                emp = self.EmployeeList[index]
                return emp
        def AddEmployee(self, FirstName, LastName, Address, City, State, Zip):
            employeenumber = self.NextEmployeeNumber()

            emp = Employee(employeenumber, FirstName, LastName, Address, City, State, Zip)

            self.EmployeeList.Append(emp)

            print("Employee Added")

        def UpdateEmployee(self, employeenumber, FirstName, LastName, Address, City, State, Zip):
            index = self.FindEmployee(employeenumber)

            if index == 1:
                print("Errer: Employee Does Not Exist")
            else:
                self.EmployeeList[index].FirstName = FirstName
                self.EmployeeList[index].LastName = LastName
                self.EmployeeList[index].Address = Address
                self.EmployeeList[index].City = City
                self.EmployeeList[index].State = State
                self.EmployeeList[index].Zip = Zip

                print("Employee Updated")
    def DeleteEmployee(self, employeenumber):
        index = self.FindEmployee(employeenumber)

        if index == -1:
            print("Eror: Employee Does Not Exist")
        else: 
            self.EmployeeList.pop(index)
            print("Employee Deleted")
    def FindEmployee(self, employeenumber):
        for i in range(len(self.EmployeeList)):
            if self.EmployeeList[i].employeenumber == int(employeenumber):
                return i
            
        return -1 
    def NextEmployeeNumber(self):
        if len(self.EmployeeList) ++ 0:
            return 1
        else: 
            return self.EmployeeList[-1].employeenumber +1 
        
def load_employees():
    employees = []

    try:
        file = open(FILENAME, "r")

        for line in file:
            print("READING LINE:", line)
            line = line.strip()

            if line !="":
                data = line.split(",")
                print("SPLIT DATA:", data)

                emp = Employee(
                    data[0].strip(),
                    data[1].strip(),
                    data[2].strip(),
                    data[3].strip(),
                    data[4].strip(),
                    data[5].strip(),
                    data[6].strip()
                )

                employees.append(emp)

        file.close()

    except FileNotFoundError: 
        print("No employee file found. Starting empty.")
    
    return employees

def save_emp(employees):
    file = open(FILENAME, "w")

    for emp in employees:
        file.write(
            str(emp.employeenumber) + "," +
            emp.first +"," +
            emp.last + "," +
            emp.address + "," +
            emp.city + "," +
            emp.state + "," +
            emp.zip +"\n"
        )
    file.close()
    print("Changes Saved to File")

def get_nonempty(prompt):
    value = input(prompt).strip()

    while value =="":
        print("Error: This field cannot be blank.")
        value = input(prompt).stip()

    return value 

def get_state():
    state = input("Enter State: ").strip().upper()

    while state =="":
        print("Error: State cannot be blank.")
        state = input("Enter State: ").strip()
        
    return state 

def get_zip():
    zip = input("Enter Zip:").strip()
    while len(zip) != 5 or not zip.isdigit():
        print("Error: Zip must be 5 digits.")
        zip = input("Enter Zip:").strip()
    
    return zip 

def find_employee(employees, employeenumeber):
    for i in range(len(employees)):
        if employees[i].employeenumber == employeenumeber:
            return i 
    
    return -1

def get_next_employee_number(employees):
    if len(employees) ==0:
        return 1 
    
    last_employee = employees[-1]
    return last_employee.employeenumber +1

def add_employee(employees):
    employeenumber = get_next_employee_number(employees)

    first = get_nonempty("Enter First Name: ")
    last = get_nonempty("Enter Last Name: ")
    address = get_nonempty("Enter Address: ")
    city = get_nonempty("Enter City: ")
    state = get_state()
    zip = get_zip()

    emp = Employee(employeenumber, first, last, address, city, state, zip)
    employees.append(emp)

    print("Employee Added")

def delete_employee(employees):
    emp_num = int(input("Enter Employee Number to Delete: "))
    
    index = find_employee(employees, emp_num)

    if index ==-1: 
        print("Error: Employee does not exist.")
    else:
        employees.pop(index)
        print("Employee Deleted")

def change_employee(employees):
    employeenumber = int(input("Enter Enployee Number to Change: "))

    index = find_employee(employees, employeenumber)

    if index == -1:
        print("Error: Employee does not exist.")
        return 
    choice = ""

    while choice != "B":
        print("\n(F)irst Name")
        print("(L)ast Name")
        print("(A)ddress")
        print("(C)ity")
        print("(S)tate")
        print("(Z)ip")
        print("(B)ack to Main Menu")

        choice = input("\nEnter Selection: ").strip().upper()

        if choice == "F":
            employees[index].first = get_nonempty("Enter New First Name: ")
            print("Employee Changed")

        elif choice == "L": 
            employees[index].first = get_nonempty("Enter New Last Name: ")
            print("Employee Changed")

        elif choice == "A":
            employees[index].address= get_nonempty("Enter New Address: ")
            print("Employee Changed")
        
        elif choice =="C":
            employees[index].city= get_nonempty("Enter New City: ")
            print("Employee Changed")

        elif choice =="S":
            employees[index].state = get_nonempty("Enter New State: ")
            print("Employee Changed")
        
        elif choice =="Z":
            employees[index].zip = get_zip()
            print("Employee Changed")

        elif choice =="B":
            print("Returning to Main Menu")
        
        else: 
            print("Invalid Selection")

def print_employees(employees):
    print()
    print("{:<8}{:<12}{:<20}{:<15}{:<12}{:<8}".format("Emp#", "First", "Last", "Address", "City", "State", "Zip"))
    print("-" *87)

    for emp in employees:
     print(
        f"{emp.employeenumber:<8}"
        f"{emp.first:<12}"
        f"{emp.last:<12}"
        f"{emp.address:<20}"
        f"{emp.city:<15}"
        f"{emp.state:<12}"
        f"{emp.zip:<8}"
    )

def main ():
    employees = EmployeeList("Final Project Employees.txt")
    employees.ReadEmployeeFile()

    choice =""

    while choice != "Q":
        print("\n(A)dd a New Employee")
        print("(D)elete an Existing Employee")
        print("(C)hange an Exisitng Employee")
        print("(P)rint all Employees")
        print("(S)ave Changes to File")
        print("(Q)uit")

        choice = input("\nEnter Selection: ").strip().upper()

        if choice == "A":
            first = input("Enter First Name: ").strip()
            last = input("Enter Last Name: ").strip()
            address = input("Enter Address: ").strip()
            city = input("Enter City: ").strip()
            state = input("Enter State: ").strip()
            zip = input("Enter Zip: ").strip() 

            employees.AddEmployee(first, last, address, city, state, zip)

        elif choice == "D":
            employeenumber = int(input("Enter Employee Number To Delete: "))
            employees.DeleteEmployee(employeenumber)

        elif choice == "C":
            employeenumber = int(input("Enter Employee Numer to Change: "))
            
            if employees.FindEmployee(employeenumber) == -1:
                print("Error: Employee does not Exist")
            else: 
                first = input("Enter New First Name: ").strip()
                last = input("Enter New Last Name: ").strip()
                address = input("Enter New Address: ").strip()
                city = input("Enter New City: ").strip()
                state = input("Enter New State: ").strip().upper()
                zip = input("Enter New Zip: ").strip()

                employees.UpdateEmployee(employeenumber, first, last, address, city, state, zip)
        
        elif choice == "P":
            employees.DisplayEmployeeList()

        elif choice == "S":
            employees.WriteEmployeeFile()

        elif choice == "Q": 
            print("Goodbye. Have a Great Summer! :) ")

        else: 
            print("Invalid selection")

main()