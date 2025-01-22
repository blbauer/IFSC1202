import re

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class UserList:
    def __init__(self, filename):
        self.filename = filename
        self.userlist = []
        self.read_user_file()

    def read_user_file(self):
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    username, password = line.strip().split(',')
                    user = User(username, password)
                    self.userlist.append(user)
        except FileNotFoundError:
            print(f"{self.filename} not found. Starting with an empty user list.")

    def write_user_file(self):
        with open(self.filename, 'w') as file:
            for user in self.userlist:
                file.write(f"{user.username},{user.password}\n")
        print("Changes Saved.")

    def display_user_list(self):
        if not self.userlist:
            print("No users to display.")
        else:
            print(f"{'Username':<15} {'Password':<15}")
            print("-" * 30)
            for user in self.userlist:
                print(f"{user.username:<15} {user.password:<15}")

    def find_username(self, username):
        for i, user in enumerate(self.userlist):
            if user.username == username:
                return i
        return -1

    def change_password(self, username, password):
        index = self.find_username(username)
        if index != -1:
            self.userlist[index].password = password
            print("Password Changed.")
        else:
            print("Username Not Found.")

    def add_user(self, username, password):
        if self.find_username(username) == -1:
            new_user = User(username, password)
            self.userlist.append(new_user)
            print("User Added.")
        else:
            print("Username Already Exists.")

    def delete_user(self, username):
        index = self.find_username(username)
        if index != -1:
            del self.userlist[index]
            print("User Deleted.")
        else:
            print("Username Not Found.")

    def strength(self, password):
        score = 0
        if len(password) >= 8:
            score += 1
        if re.search(r'[A-Z]', password):
            score += 1
        if re.search(r'[a-z]', password):
            score += 1
        if re.search(r'[0-9]', password):
            score += 1
        if re.search(r'[~!@#$%^&*()_+|\-={}[\]:;<>?]', password):
            score += 1
        return score

def main():
    userlist = UserList('Final Project Passwords.txt')
    
    while True:
        print("\nMenu:")
        print("1) Add a New User")
        print("2) Delete an Existing User")
        print("3) Change Password on an Existing User")
        print("4) Display All Users")
        print("5) Save Changes to File")
        print("6) Quit")
        selection = input("Enter Selection: ")

        if selection == '1':
            username = input("Enter user ID: ")
            if userlist.find_username(username) != -1:
                print("Username Already Exists")
            else:
                password = input("Enter password: ")
                while userlist.strength(password) < 5:
                    print(f"This password is weak - {userlist.strength(password)}")
                    password = input("Enter a stronger password: ")
                userlist.add_user(username, password)

        elif selection == '2':
            username = input("Enter user ID to delete: ")
            userlist.delete_user(username)

        elif selection == '3':
            username = input("Enter user ID: ")
            if userlist.find_username(username) == -1:
                print("Username Not Found.")
            else:
                password = input("Enter new password: ")
                while userlist.strength(password) < 5:
                    print(f"This password is weak - {userlist.strength(password)}")
                    password = input("Enter a stronger password: ")
                userlist.change_password(username, password)

        elif selection == '4':
            userlist.display_user_list()

        elif selection == '5':
            userlist.write_user_file()

        elif selection == '6':
            print("Exiting program.")
            break

        else:
            print("Invalid Selection")

if __name__ == "__main__":
    main()