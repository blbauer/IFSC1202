class Sketch():
    def __init__(self, size):
        # size of the canvas - note that the values go from 0 to size - 1
        self.size = size
        # current x position (0 to size -1)
        self.xpos = 0
        # current y position (0 to size -1)
        self.ypos = 0
        # current direction (U=Up, R=Right, D=Down, L=Left )
        self.direction ="U"
        # pen up or down U=Up, D=Down
        self.pen = "U"
        # canvas has size columns and size rows
        self.canvas=[]
        for i in range(self.size):
           self.canvas.append([' '] * self.size)
        return
    
    def printsketch(self):
        # print the top border
        print("+" + ("-" * self.size) + "+")
        # print from top to bottom
        for i in range (self.size-1,-1,-1):
            # print the left border
            print("|", sep="", end="")
            # print a row of the canvas
            for j in range(self.size):
                print(self.canvas[i][j], sep="", end="")
            # print the right border and a new line
            print("|")
        # print the bottom border
        print("+" + ("-" * self.size) + "+")
        # print the x and y position and the direction
        print("X =", self.xpos, " Y =", self.ypos, " Direction =", self.direction)
        return

    def penup(self):
        # set the pen to up
        self.pen ="U"
        return

    def pendown(self):
        # set the pin to down
        self.pen = "D"
        return

    def turnleft(self):
        # check the current direction and turn to the left
        if self.direction == "U":
            self.direction = "L"
            return
        if self.direction == "L":
            self.direction = "D"
            return
        if self.direction == "D":
            self.direction = "R"
            return
        if self.direction == "R":
            self.direction = "U"
            return
        return
        
    def turnright(self):
        # check the current direction and turn to the left
        if self.direction == "U":
            self.direction = "R"
            return
        if self.direction == "R":
            self.direction = "D"
            return
        if self.direction == "D":
            self.direction = "L"
            return
        if self.direction == "L":
            self.direction = "U"
            return
        return

    def move(self, distance):
        # direction is up
        if self.direction == "U":
            # calculate new x position
            newxpos = self.xpos + distance 
            # make sure you stop at the end of the canvas
            if newxpos >= self.size:
                newxpos = self.size - 1
            # If pen is down, draw the line
            if self.pen == "D":
                for i in range (self.xpos, newxpos + 1):
                    self.canvas[i][self.ypos] = "*"
            # reset to new x position
            self.xpos = newxpos

        # direction is right
        if self.direction == "R":
            # calculate new y position
            newypos = self.ypos + distance
            # make sure you stop at the end of the canvas
            if newypos >= self.size:
                newypos = self.size - 1
            # If pen is down, draw the line
            if self.pen == "D":
                for i in range (self.ypos, newypos + 1):
                    self.canvas[self.xpos][i] = "*"
            # reset to new y position
            self.ypos = newypos

        # direction is down
        if self.direction == "D":
            # calculate new x position - note subtraction
            newxpos = self.xpos - distance
            # make sure you stop at the end of the canvas
            if newxpos < 0:
                newxpos = 0
            if self.pen == "D":
            # If pen is down, draw the line - note negative increment
                for i in range (self.xpos, newxpos - 1, -1):
                    self.canvas[i][self.ypos] = "*"
            # reset to new x position
            self.xpos = newxpos

        # direction is left
        if self.direction == "L":
            # calculate new x position - note subtraction
            newypos = self.ypos - distance
            # make sure you stop at the end of the canvas
            if newypos < 0:
                newypos = 0
            # If pen is down, draw the line - note negative increment
            if self.pen == "D":
                for i in range (self.ypos, newypos - 1, -1):
                    self.canvas[self.xpos][i] = "*"
            # reset to new y position
            self.ypos = newypos
 
# Open the input file and read the first line
inputfile = open("cshape.txt")
commandtext = inputfile.readline()
# create a sketch with the specified size
mysketch = Sketch(int(commandtext))
# read the rest of the commands and run the appropriate method
commandtext = inputfile.readline()
while commandtext != "":
    commandtextvalues = commandtext.split(",")
    command = commandtextvalues[0].strip()
    # pen up command
    if command == "1":
        mysketch.penup()
    # pen down command
    if command == "2":
        mysketch.pendown()
    # turn right command
    if command == "3":
        mysketch.turnright()
    # turn left command  
    if command == "4":
        mysketch.turnleft()
    # move command - note additional parameter
    if command == "5":
        mysketch.move(int(commandtextvalues[1]))
    # print canvas command
    if command == "6":
        mysketch.printsketch()
    commandtext = inputfile.readline()
inputfile.close()
