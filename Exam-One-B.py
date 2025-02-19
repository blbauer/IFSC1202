from random import randint
name = input("What is your name: ")

computerscore = 0
personscore = 0

while personscore < 30 and computerscore < 30:
    print("#"*20)
    roll = input("Press enter to roll the die " + name + " ")
    personroll = randint(1,6)
    computerroll = randint(1,6)
    print(name, "rolled a", personroll)
    print("Computer rolled a", computerroll)
    if personroll == 1:
        personscore = 0
        print("Oops", name, "has to start over")
    else:
        personscore = personscore + personroll
    if computerroll == 1:
        computerscore = 0
        print("Oops Computer has to start over")
    else:
        computerscore = computerscore + computerroll
    print(name + "'s", "Score:", personscore)
    print("Computer's Score:", computerscore)

print("#"*20)
if personscore > computerscore:
    print(name, "Wins")
else:
    print("Computer Wins")