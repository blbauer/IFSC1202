#Jacqueline Suchan
#T00611541

class Student ():
    def __init__(self, firstname, lastname, tnumber, scores):
        self.FirstName = firstname
        self.Lastname = lastname
        self.TNumber = tnumber
        self.Grades = scores

    def RunningAverage(self):
        total = 0
        numberofgrades = 0
        for i in range (len(self.Grades)):
            if self.Grades[i] != "":
                total = total + float(self.Grades[i])
                numberofgrades += 1
        RunningAverage = total / numberofgrades
        return RunningAverage
    
    def TotalAverage(self):
        numberofgrades = len(self.Grades)
        total = 0
        for i in range (len(self.Grades)):
            if self.Grades[i] != "":
                total = total + float(self.Grades[i])
        TotalAverage = total / numberofgrades
        return TotalAverage
    
    
    def LetterGrade(self):
        scores = self.TotalAverage()
        if scores >= 90:
            return "A"
        if scores >= 80:
            return "B"
        if scores >= 70:
            return "C"
        if scores >= 60:
            return "D"
        if scores < 60:
            return "F"
        
studentfile = open("10.Project Student Scores.txt", 'r')
line = studentfile.readline()
while line != "":
    grades = line.split(",")
    mystudent = Student(grades[0],grades[1],grades[2],grades[3:])
    print("{:>12s} {:>12s} {:>12s} {:>12.2f} {:>12.2f} {:>12s}".format(mystudent.FirstName, mystudent.Lastname, mystudent.TNumber, mystudent.RunningAverage(), mystudent.TotalAverage(), mystudent.LetterGrade()))
    print(mystudent.FirstName)
    print(mystudent.Lastname)
    print(mystudent.TNumber)
    print(mystudent.RunningAverage())
    print(mystudent.TotalAverage())
    print(mystudent.LetterGrade())
    line = studentfile.readline()