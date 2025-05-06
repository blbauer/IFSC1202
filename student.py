class Sketch:
    def init(self, size):
        self.size = size
        self.xpos = 0 
        self.ypos = 0 
        self.direction = 'U' 
        self.pen = 'U' 
        self.canvas =[[' ' for in range(size)] for in range(size)] 

def printsketch(self): 
    print('+' + '-' * self.size + '+') 
    for row in range(self.size - 1, -1, -1): line = '|' for col in range(self.size): 
line +=self.canvas[row][col] line += '|' print(line) 
print('+' + '-' * self.size + '+') 
print(f'Position: ({self.xpos}, {self.ypos}) 
Direction: {self.direction} 
Pen: {self.pen}') def penup(self): self.pen = 'U' def pendown(self): self.pen = 'D'
