# Step 1 - Define the class object "Student"
class Student:
# Step 2 - Define the initializer and any default values
    def __init__(self, firstname, lastname, tnumber):
# Step 3 - Define the object attributes
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        # Note - Grades is a list of grades
        self.Scores = []
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

# Step 1 - Define the class object "Studentlist"
class StudentList:
# Step 2 - Define the initializer and any default values
    def __init__(self):
# Step 3 - Define the object attributes
# Create an empty student list
        self.Studentlist = []
# Step 4 - Define Actions (Methods) associated with the object
# Add a student to the list
    def add_student(self, firstname, lastname, tnumber):
#		Create a new student object
        mystudent = Student(firstname, lastname, tnumber)
#		Append student object to list
        self.Studentlist.append(mystudent)
# Find a student in the list and return the index
    def find_student(self, studenttofind):
        for i in range(len(self.Studentlist)):
            if self.Studentlist[i].TNumber == studenttofind:
                return i
        return -1		
# Print the Student list
# Print a Name, then loop through the courses and print the course information
    def print_student_list(self):
        print("{:>12s} {:>12s} {:>12s} {:>12s} {:>12s} {:>12s}".format("First", "Last", "ID", "Running", "Semester", "Letter"))
        print("{:>12s} {:>12s} {:>12s} {:>12s} {:>12s} {:>12s}".format("Name", "Name", "Number", "Average", "Average", "Grade"))
        print("{:>12s} {:>12s} {:>12s} {:>12s} {:>12s} {:>12s}".format("-"*12, "-"*12, "-"*12, "-"*12, "-"*12, "-"*12))
        for i in range(len(self.Studentlist)):
            print ("{:>12s} {:>12s} {:>12s} {:>12.2f} {:>12.2f} {:>12s}".format(self.Studentlist[i].FirstName, self.Studentlist[i].LastName, self.Studentlist[i].TNumber, self.Studentlist[i].RunningAverage(), self.Studentlist[i].TotalAverage(), self.Studentlist[i].LetterGrade()))

# Read a student file and append the values to the student list
    def add_student_from_file(self, filename):
        studentfile = open(filename)
        x = studentfile.readline()
        while x != "":
            y = x.split(",")
            self.add_student(y[0].strip(), y[1].strip(), y[2].strip())
            x = studentfile.readline()
        studentfile.close()

# Read a Score file and append the values to the scores of the corresponding student
    def add_scores_from_file(self, filename):
        scorefile = open(filename)
        x = scorefile.readline()
        while x != "":
            y = x.split(",")
            studentindex = self.find_student(y[0].strip())
            if studentindex != -1:
                self.Studentlist[studentindex].Scores.append(y[1].strip())
            x = scorefile.readline()
        scorefile.close()
#--------------------------------------------------------------------
# Main Progam
# Create a Student List
mystudentlist = StudentList()
# Read Student List from File
mystudentlist.add_student_from_file("11.Project Students.txt")
# Read the Score Information
mystudentlist.add_scores_from_file("11.Project Scores.txt")
# print Student List
mystudentlist.print_student_list()