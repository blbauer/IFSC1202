# Step 1 - Define the class object "Student"
class Student():
# Step 2 - Define the initializer and any default values
	def __init__(self, firstname, lastname, tnumber):
# Step 3 - Define the object attributes for a student
		self.FirstName = firstname
		self.LastName = lastname
		self.TNumber = tnumber
		self.CourseList = []

# Step 1 - Define the class object "Studentlist"
class StudentList ():
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
		print("{:14s}{:14s}{:14s}{:15s}{:50s}{:14s}{:20s}".format("First Name", "Last Name", "T-Number", "Course", "Name", "Room", "Meeting Times"))
		for i in range(len(self.Studentlist)):
			print ("{:14s}{:14s}{:14s}".format(self.Studentlist[i].FirstName, self.Studentlist[i].LastName, self.Studentlist[i].TNumber))
			for j in range(len(self.Studentlist[i].CourseList)):
				print ("{:14s}{:14s}{:14s}{:5s}{:10s}{:50s}{:14s}{:20s}".format("", "", "", self.Studentlist[i].CourseList[j].Department, self.Studentlist[i].CourseList[j].Number, self.Studentlist[i].CourseList[j].Name, self.Studentlist[i].CourseList[j].Room, self.Studentlist[i].CourseList[j].MeetingTimes))
# Read a student file and append the values to the student list
	def add_student_from_file(self, filename):
		studentfile = open(filename)
		x = studentfile.readline()
		while x != "":
			y = x.split(",")
			self.add_student(y[0].strip(), y[1].strip(), y[2].strip())
			x = studentfile.readline()
		studentfile.close()
	
# Step 1 - Define the class object "Course"
class Course():
# Step 2 - Define the initializer and any default values
	def __init__(self, department, number, name, room, meetingtimes):
# Step 3 - Define the object attributes for a Course
		self.Department = department
		self.Number = number
		self.Name = name
		self.Room = room
		self.MeetingTimes = meetingtimes

# Step 1 - Define the class object "Studentlist"
class CourseList ():
# Step 2 - Define the initializer and any default values
	def __init__(self):
# Step 3 - Define the object attributes
# Create an empty course list
		self.CourseList = []
# Step 4 - Define Actions (Methods) associated with the object
# Add a course data to the course list
	def add_course(self, department, number, name, room, meetingtimes):
#		Create a course object
		mycourse = Course(department, number, name, room, meetingtimes)
#		Append course object to list
		self.CourseList.append(mycourse)
#	Add course information to the course list
	def add_course_from_file(self, filename):
		coursefile = open(filename)
		x = coursefile.readline()
		while x != "":
			y = x.split(",")
			self.add_course(y[0].strip(), y[1].strip(), y[2].strip(), y[3].strip(), y[4].strip())
			x = coursefile.readline()
		coursefile.close()
# Find a course by department and number then return the index
	def find_course(self, departmenttofind, numbertofind):
		for i in range(len(self.CourseList)):
			if self.CourseList[i].Department == departmenttofind and self.CourseList[i].Number == numbertofind:
				return i
		return -1		
#--------------------------------------------------------------------
# Main Progam
# Create a Course List
mycourselist = CourseList()
# Read Course List from File
mycourselist.add_course_from_file("11.03 Courses.txt")
# Create a Student List
mystudentlist = StudentList()
# Read Student List from File
mystudentlist.add_student_from_file("11.03 Students.txt")
# Read the Resgistration Information
registrationfile = open("11.03 Registration.txt")
x = registrationfile.readline()
while x != "":
	y = x.split(",")
#	Based on the department and course number, find the index of the course in the course list
	courseindex = mycourselist.find_course(y[1].strip(), y[2].strip())
#	Create a new course object out the selected course object
	mycourse = mycourselist.CourseList[courseindex]
#	Based on the TNumber, find the index of the student in the student list
	studentindex = mystudentlist.find_student(y[0].strip())
#	Append the new course object to the selected student course list
	mystudentlist.Studentlist[studentindex].CourseList.append(mycourse)
	x = registrationfile.readline()
registrationfile.close()
# print Student List
mystudentlist.print_student_list()