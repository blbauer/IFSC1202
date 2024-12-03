from math import pi
# Step 1 - Define the class object "Ball"
class Ball ():

# Step 2 - Define the initializer and any default values
    def __init__(self, balltype="Basketball", diameter=9.51, pressure=8.0):
        self.BallType = balltype
        self.Diameter = diameter
        self.Pressure = pressure

    def Circumference(self):
       circumference =  pi * self.Diameter
       return circumference 
    
    def ChangePressure(self, pressurechange):
       self.Pressure += pressurechange
       return self.Pressure

myball1 = Ball("Basketball", 9.51, 8.0)
myball2 = Ball("Volleyball", 8.15, 7.5)
myball3 = Ball("Soccerball", 8.65, 9.0)
myball4 = Ball()

print (myball1.BallType, myball1.Diameter, myball1.Pressure, myball1.Circumference())
print (myball2.BallType, myball2.Diameter, myball2.Pressure, myball2.Circumference())
print (myball3.BallType, myball3.Diameter, myball3.Pressure, myball3.Circumference())
print (myball4.BallType, myball4.Diameter, myball4.Pressure, myball4.Circumference()) 

myball1.Diameter = 9.0
print (myball1.BallType, myball1.Diameter, myball1.Pressure, myball1.Circumference())

newpressure = myball1.ChangePressure(1)
print (newpressure)
newpressure = myball1.ChangePressure(1)
print (newpressure)
newpressure = myball1.ChangePressure(1)
print (newpressure)
newpressure = myball1.ChangePressure(1)
print (newpressure)
print (myball1.BallType, myball1.Diameter, myball1.Pressure, myball1.Circumference())
