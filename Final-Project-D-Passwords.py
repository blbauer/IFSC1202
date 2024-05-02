#
# User Class
# Attributes:
#       Username
#       Password
#
class User():
    def __init__(self, Username, Password):
        self.Username = Username
        self.Password = Password
#
# UserList Class
# Attributes:
#       UserList - a list of User object
#       FileName- File name of a file containing Usernames and Passwords separated by a comma
#
class UserList():
    def __init__ (self, FileName):
        self.UserList = []
        self.FileName = FileName
#
# ReadUserFile
#   Opens FileName file containing Usernames and Passwords
#   Reads Username and Password
#   Creates a User Object
#   Appends User Object to UserList
#
    def ReadUserFile(self):
        UserFile = open(self.FileName, "r")
        x = UserFile.readline()
        while x != "":
            y = x.split(",")
            self.UserList.append(User(y[0].strip(), y[1].strip()))
            x = UserFile.readline()
        UserFile.close()
#
# WriteUserFile
#   Opens FileName for writing
#   Loops though the UserList
#   Writes Username and Password in .CSV format
#
    def WriteUserFile(self):
        UserFile = open(self.FileName, "w")
        for i in range(len(self.UserList)):
            UserFile.write(self.UserList[i].Username + ", " + self.UserList[i].Password + "\n")
        UserFile.close()
#
# DisplayUserList
#   Prints Username and Password headings from the UserList
#   Loops through the UserList
#   Prints the Unsername and Password of each User object in the UserList
#
    def DisplayUserList(self):
        print("{:15s} {:15s}".format("Username","Password"))
        print("{:15s} {:15s}".format(15*"-", 15*"-"))
        for i in range(len(self.UserList)):
            print("{:15s} {:15s}".format(self.UserList[i].Username, self.UserList[i].Password))
#
# FindUsername
#   Loops through the Userlist looking for a matching UserName
#   Return the index of Username in UserList
#   If Username not found then return -1
#
    def FindUsername(self, UsernameToFind):
	    for i in range(len(self.UserList)):
		    if self.UserList[i].Username == UsernameToFind:
			    return i
	    return -1
#
# ChangePassword
#   Using FindUserName, determine if the Username exists
#   if the Username exists, then update the Password atttibute with the new Password
#
    def ChangePassword(self, Username, Password):
        UsernameIndex = self.FindUsername(Username)
        if UsernameIndex != -1:
            self.UserList[UsernameIndex].Password = Password
#
# AddUser
#   Make sure that the user does not already exist using FindUsername
#   If the user does not exit
#       Create a User object from the Username and Password
#       Append the object to the UserList
#
    def AddUser(self, Username, Password):
        UsernameIndex = self.FindUsername(Username)
        if UsernameIndex == -1:
            self.UserList.append(User(Username.strip(), Password.strip()))
#
# DeleteUser
#   User FindUsername to locate the index of the User in UserList
#   If User was found
#       Delete the User Object from the list
#
    def DeleteUser(self, UsernameToFind):
        UsernameIndex = self.FindUsername(Username)
        if UsernameIndex != -1:
            del self.UserList[UsernameIndex]
#
# Strength
#   Determines the stength of the password. The password gets a point for:
#       Should have at least 8 characters
#       Should contain at least 1 uppercase letter
#       Should contain at least 1 lowercase letter
#       Should include a number
#       Should include a special character
#
    def Strength(self, Password):
        SpecialCharacters = "~!@#$%^&*()_+|-=\{}[]:;<>?/"
        Numbers = "0123456789"
        Score = 0
        LowerCaseFound = False
        UpperCaseFound = False
        SpecialCharacterFound = False
        NumberFound = False

        for i in range(0,len(Password)):
            if Password[i].islower():
                LowerCaseFound = True
            if Password[i].isupper():
                UpperCaseFound = True
            if SpecialCharacters.find(Password[i]) != -1:
                SpecialCharacterFound = True
            if Numbers.find(Password[i]) != -1:
                NumberFound = True

        if len(Password) >= 8:
            Score = Score + 1
        if LowerCaseFound:
            Score = Score + 1
        if UpperCaseFound:
            Score = Score + 1
        if SpecialCharacterFound:
            Score = Score + 1
        if NumberFound:
            Score = Score + 1
        return Score
#
# Main Program
#
#  Create a Userlist Object using a file name
MyUserList = UserList("Final Project Passwords.txt")
#
# Read the file and create the list
MyUserList.ReadUserFile()
#
# Display a menu and get selection
Selection = "0"
while Selection != "6":

    print()
    print("1) Add a New User")
    print("2) Delete an Existing User")
    print("3) Change Password on an Existing User")
    print("4) Display All Users")
    print("5) Save Changes to File")
    print("6) Quit")
    print()
    Selection = input("Enter Selection: ")
    print()
#
# Selection 1 - Add a Mew User
    if Selection == "1":
        Username = input("Enter User Name: ")
#       Error if user already exists
        UsernameIndex = MyUserList.FindUsername(Username)
        if UsernameIndex != -1:
            print("Username Already Exists")
        else:
#           User does not exist
#           Prompt for Password
            print("A Password:\n" +
                    "Should have at least 8 characters\n" + 
                    "Should contain at least 1 uppercase letter\n" +
                    "Should contain at least 1 lowercase letter\n" +
                    "Should include a number\n" +
                    "Should include a special character")
            Password = input("Enter Password: ")
#           Calculate Password strength
            Strength = MyUserList.Strength(Password)
#           Force a Password stength of 5
#           Keep prompting for a password until is has a strength of 5
            while Strength < 5:
                print("This password is weak - Strength = {}".format(Strength))
                Password = input("Enter Password: ")
                Strength = MyUserList.Strength(Password)
#           New Userame and good Password
#           Add User and Password to the UserList
            MyUserList.AddUser(Username, Password)
            print("User Added")
#
# Selection 2 - Delete an Existing User
    elif Selection == "2":
        Username = input("Enter User Name: ")
#       Check to see if User exists
        UsernameIndex = MyUserList.FindUsername(Username)
        if UsernameIndex == -1:
#           User does not exist - print error message
            print("Username Not Found")
        else:
#           Username exists; delete user
            MyUserList.DeleteUser(Username)
            print("User Deleted")
#
# Selection 3 - Change Password on Existing User
    elif Selection == "3":
        Username = input("Enter User Name: ")
#       Check to see if User exists
        UsernameIndex = MyUserList.FindUsername(Username)
        if UsernameIndex == -1:
#           User does not exist - print error message
            print("Username Not Found")
        else:
#           User exists - prompt for passord
            Password = input("Enter Password: ")
#           Calculate Password strength
            Strength = MyUserList.Strength(Password)
#           Force a Password stength of 5
#           Keep prompting for a password until is has a strength of 5
            while Strength < 5:
                print("This password is weak - Strength = {}".format(Strength))
                Password = input("Enter Password: ")
                Strength = MyUserList.Strength(Password)
#           Username exists and good Password
#           Change Password for the User
            MyUserList.ChangePassword(Username, Password)
            print("Password Changed")
#
# Selection 4 - Prints the UserList
    elif Selection == "4":
        MyUserList.DisplayUserList()
#
# Selection 5 - Save the Userlist to the file
    elif Selection == "5":
        MyUserList.WriteUserFile()
        print("Changes Saved")
#
# Select 6 - Quit
    elif Selection == "6":
        pass
#
# Invalid Selection
    else:
        print("Invalid Selection")

print("Good-bye")