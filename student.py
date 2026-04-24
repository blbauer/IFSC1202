class Student:
    def __init__(self, firstname, lastname, tnumber):
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        self.Grades = []

    def RunningAverage(self):
        total = 0
        count = 0
        for grade in self.Grades:
            if grade != "":
                total = total + float(grade)
                count = count + 1
        if count == 0:
            return 0
        else:
            return total / count
    
    def TotalAverage(self):
        total = 0

        for grade in self.Grades:
            if grade == "":
                total = total + 0
            else:
                total = total + float(grade)
        if len(self.Grades) == 0:
            return 0
        else:
            return total / len(self.Grades)

    def LetterGrade(self):
        avg = self.TotalAverage()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"
class StudentList:
    def __init__(self):
        self.Studentlist = []

    def add_student(self, FirstName, LastName, TNumber):
        new_student = Student(FirstName, LastName, TNumber)
        self.Studentlist.append(new_student)

    def find_student(self, TNumber):
        index = 0
        for student in self.Studentlist:
            if student.TNumber == TNumber:
                return index
            index = index + 1
        return -1

    def print_student_list(self):
        print("       First         Last           ID      Running     Semester       Letter")
        print("        Name         Name       Number      Average      Average        Grade")
        print("-----------------------------------------------------------------------------")
        for student in self.Studentlist:
            print(f"{student.FirstName:>12} {student.LastName:>12} {student.TNumber:>12} "
                  f"{student.RunningAverage():>12.2f} {student.TotalAverage():>12.2f} {student.LetterGrade():>12}")

    def add_student_from_file(self, filename):
        file = open(filename, "r")
        for line in file:
            line = line.strip()
            parts = line.split(",")
            firstname = parts[0]
            lastname = parts[1]
            tnumber = parts[2]
            self.add_student(firstname, lastname, tnumber)
        file.close()

    def add_scores_from_file(self, filename):
        file = open(filename, "r")
        for line in file:
            line = line.strip()
            parts = line.split(",")
            tnumber = parts[0]
            score = parts[1]
            index = self.find_student(tnumber)
            if index != -1:
                self.Studentlist[index].Grades.append(score)
        file.close()
studentslist = StudentList()
studentslist.add_student_from_file("11.Project Students.txt")
studentslist.add_scores_from_file("11.Project Scores.txt")
studentslist.print_student_list()