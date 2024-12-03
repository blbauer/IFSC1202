class Student:
    def __init__(self, firstname, lastname, tnumber):
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        self.Grades = []
    def RunningAverage(self):
      rtotal = 0
      count = 0
      for grade in self.Grades:
        if grade != "":
          count += 1
          rtotal += int(grade)
      if count == 0:
        return 0
      return rtotal / count

    def TotalAverage(self):
      ttotal=0
      for grade in self.Grades:
        if grade == "":
          ttotal+=0
        else:
          ttotal+=int(grade)
      if len(self.Grades) == 0:
        return 0
      return ttotal / len(self.Grades)

    def LetterGrade(self):
      tavg = self.TotalAverage()
      match (tavg):
        case _ if tavg >= 90:
          return "A"
        case _ if tavg >= 80:
          return "B"
        case _ if tavg >= 70:
          return "C"
        case _ if tavg >= 60:
          return "D"
        case _ if tavg < 60:
          return "F"

class StudentList:
    def __init__(self):
        self.Studentlist = []
    def add_student(self, firstname, lastname, tnumber):
        self.Studentlist.append(Student(firstname, lastname, tnumber))
    def find_student(self, tnumber):
        for student in self.Studentlist:
            if student.TNumber == tnumber:
                return self.Studentlist.index(student)
        return -1
    def print_student_list(self):
      spacer = "-" * 12
      print("{:>12} {:>12} {:>12} {:>12} {:>12} {:>12}".format("First", "Last", "ID", "Running", "Semester", "Letter"))
      print("{:>12} {:>12} {:>12}{:>12} {:>12} {:>12}".format("Name","Name","Number","Average","Average","Grade"))
      print("{:12} {:12} {:12} {:12} {:12} {:12}".format(spacer,spacer,spacer,spacer,spacer,spacer))
      for student in self.Studentlist:
        print("{:>12}".format(student.FirstName), end=" ")
        print("{:>12}".format(student.LastName), end=" ")
        print("{:>12}".format(student.TNumber), end=" ")
        print("{:>12.2f}".format(student.RunningAverage()), end=" ")
        print("{:>12.2f}".format(student.TotalAverage()), end=" ")
        print("{:>12}".format(student.LetterGrade()))
    def add_student_from_file(self, filename):
        with open(filename, "r") as f:
            for line in f:
                firstname, lastname, tnumber = line.strip().split(",")
                self.add_student(firstname, lastname, tnumber)
    def add_scores_from_file(self, filename):
        with open(filename, "r") as f:
            for line in f:
                tnumber, grade = line.strip().split(",")
                index = self.find_student(tnumber)
                if index != -1:
                    self.Studentlist[index].Grades.append(grade)


#Main
studentlist = StudentList()
studentlist.add_student_from_file("11.Project Students.txt")
studentlist.add_scores_from_file("11.Project Scores.txt")
studentlist.print_student_list()