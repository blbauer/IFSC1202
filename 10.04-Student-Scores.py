# Step 1 - Define the class object "Student"
class Student:
# Step 2 - Define the initializer and any default values
    def __init__(self, firstname, lastname, tnumber, scores):
# Step 3 - Define the object attributes
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        # Note - Grades is a list of grade strings
        self.Scores = scores
# Step 4 - Define Actions (Methods) associated with the object
# Running Average - average of non-blank scores
    def RunningAverage(self):
        totalscore = 0.0
        totalcount = 0
        for i in range(len(self.Scores)):
            if self.Scores[i].strip() != "":
                totalcount += 1
                totalscore += float(self.Scores[i])
        return totalscore / totalcount
# Total Average - average of all scores - blank score counted as zero        
    def TotalAverage(self):
        totalscore = 0.0
        for i in range(len(self.Scores)):
            if self.Scores[i].strip() != "":
                totalscore += float(self.Scores[i])
        return totalscore / len(self.Scores)
# Letter Grade depends on Total Average
    def LetterGrade(self):
        totalaverage = self.TotalAverage()
        if totalaverage >= 90:
            return "A"
        if totalaverage >= 80:
            return "B"
        if totalaverage >= 70:
            return "C"
        if totalaverage >= 60:
            return "D"
        return "F"
# Step 5 - Create 3 instances of Student using the data file
studentsfile = open("10.04 StudentScores.txt")
print("{:>12s} {:>12s} {:>12s} {:>12s} {:>12s} {:>12s}".format("First", "Last", "ID", "Running", "Semester", "Letter"))
print("{:>12s} {:>12s} {:>12s} {:>12s} {:>12s} {:>12s}".format("Name", "Name", "Number", "Average", "Average", "Grade"))
print("{:>12s} {:>12s} {:>12s} {:>12s} {:>12s} {:>12s}".format("-"*12, "-"*12, "-"*12, "-"*12, "-"*12, "-"*12))
x = studentsfile.readline()
while x!="":
    y = x.split(",")
# Note that the grades is a slice of the input line, beginning at the fourth value
    Student1 = Student(y[0].strip(), y[1].strip(), y[2].strip(), y[3:])
    print("{:>12s} {:>12s} {:>12s} {:>12.2f} {:>12.2f} {:>12s} ".format(Student1.FirstName, Student1.LastName, Student1.TNumber, Student1.RunningAverage(), Student1.TotalAverage(), Student1.LetterGrade()))
    x = studentsfile.readline()
studentsfile.close()
