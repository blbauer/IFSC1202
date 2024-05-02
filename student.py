#Jacqueline Suchan
#T00611541

class User ():
    def __init__(self, username, password ):
        self.UserName = username
        self.Password = password

class UserList ():
    def __init__(self, filename ):
        self.FileName = filename
        self.myuserlist = []

    def ReadUserFile(self):
        userfile = open(self.FileName, "r")
        userline = userfile.readline()
        while userline != "":
            userdata = userline.split(",")
            self.myuserlist.append(User(userdata[0].strip(),userdata[1].strip()))
            userline = userfile.readline()
        userfile.close()

    def WriteUserFile(self):
        userlistfile = open("Final Project Passwords.txt", "w")
        for i in range(len(self.myuserlist)):
            userlistfile.write(self.myuserlist[i].UserName + "," + self.myuserlist[i].Password + "\n")
        userlistfile.close()
        print("Data Saved")
        

    def DisplayUserList(self):
        print("{:<15s} {:<15s}".format("Username", "Password"))
        print("{:<15s} {:<15s}".format(15*"-", 15*"-"))
        for i in range(len(self.myuserlist)):
            print("{:<15s} {:<15s}".format(self.myuserlist[i].UserName, self.myuserlist[i].Password))

    def FindUsername(self, username):
        for i in range(len(self.myuserlist)):
            if self.myuserlist[i].UserName == username:
                return i
        return -1

    def ChangePassword(self, username, password):
        usernameindex = self.FindUsername(username)
        if usernameindex != -1:
            self.myuserlist[usernameindex].Password = password
            print("Password Changed")
    
    def AddUser(self, username, passord):
        myuser = User(username, password)
        self.myuserlist.append(myuser)
        print("User Added")

    def DeleteUser(self, username):
        usernameindex = self.FindUsername(username)
        if usernameindex != -1:
            del self.myuserlist[usernameindex]
            print("User Deleted")

    def Strength(self, password):
        specialcharacters = "~!@#$%^&*()_+|-={}[]:;<>?/"
        numbers = "0123456789"
        score = 0
        if len(password) >= 8:
            score += 1

        for i in range(len(password)):
            if password[i].isupper():
                score += 1
                break

        for i in range(len(password)):
            if password[i].islower():
                score += 1
                break

        for i in range(len(password)):
            for j in range(len(numbers)):
                if password[i] == numbers[j]:
                    score += 1
                    break

        for i in range(len(password)):
            for j in range(len(specialcharacters)):
                if password[i] == specialcharacters[j]:
                    score += 1
                    break
        return score

myuserlist= UserList("Final Project Passwords.txt")
myuserlist.ReadUserFile()
maxstrength = 5

while True:
    print("1) Add New User")
    print("2) Delete Existing User")
    print("3) Change Password On An Existing User")
    print("4) Display All Users")
    print("5) Save Changes To File")
    print("6) Quit")
    selection = input("Enter selection: ")
    if selection == "1":
        username = input("Enter username: ")
        usernameindex = myuserlist.FindUsername(username)
        if usernameindex == -1:
            password = input("Enter password: ")
            strength = myuserlist.Strength(password)
            if strength >= maxstrength:
                myuserlist.AddUser(username, password)
            else:
                print("Password is Weak - Strength:", strength)
        else:
            print("User already exists")
    elif selection == "2":
        username = input("Enter username: ")
        usernameindex = myuserlist.FindUsername(username)
        if usernameindex != -1:
            myuserlist.DeleteUser(username)
        else:
            print("Username not found")
    elif selection == "3":
        username = input("Enter username: ")
        usernameindex = myuserlist.FindUsername(username)
        if usernameindex != -1:
            password = input("Enter password: ")
            strength = myuserlist.Strength(password)
            if strength >= maxstrength:
                myuserlist.ChangePassword(username, password)
            else:
                print("Password is Weak - Strength:", strength)
        else:
            print("Username not found")
    elif selection == "4":
        myuserlist.DisplayUserList()
    elif selection == "5":
        myuserlist.WriteUserFile()
    elif selection == "6":
        break
    else:
        print("Invalid Selection")