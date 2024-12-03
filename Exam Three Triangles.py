# Triangle
from math import sqrt
from math import acos
from math import pi
class Triangle:
    def __init__(self, s1, s2, s3):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

    def type(self):
        if self.s1==self.s2 and self.s2==self.s3:
            return "Equailateral"
        if self.s1==self.s2 or self.s1==self.s3 or self.s2==self.s3:
            return "Isocelese"
        return "Scalene"

    def perimeter(self):
        return self.s1 + self.s2 + self.s3

    def area(self):
        # See https://en.wikipedia.org/wiki/Heron%27s_formula
        s = (self.s1 + self.s2 + self.s3) / 2.0
        return sqrt(s * (s - self.s1) * (s - self.s2) * (s-self.s3))

    def angles(self):
        # See https://www.mathsisfun.com/algebra/trig-solving-sss-triangles.html
        angles= []
        angles.append(acos((self.s2**2 + self.s3**2 - self.s1**2) / (2.0 * self.s2 * self.s3)) * 180 / pi)
        angles.append(acos((self.s1**2 + self.s3**2 - self.s2**2) / (2.0 * self.s1 * self.s3)) * 180 / pi)
        angles.append(acos((self.s1**2 + self.s2**2 - self.s3**2) / (2.0 * self.s1 * self.s2)) * 180 / pi)
        return angles

myTriangleList = []
trianglefile = open("Exam Three Triangles.txt")
triangledata = trianglefile.readline()
while triangledata != '':
    trianglevalues = triangledata.split(",")
    objTriangle = Triangle(float(trianglevalues[0].strip()), float(trianglevalues[1].strip()), float(trianglevalues[2].strip()))
    myTriangleList.append(objTriangle)
    triangledata = trianglefile.readline()

print("{:>12s} {:>10s} {:>10s} {:>10s} {:>10s} {:>10s} {:>10s} {:>10s} {:>10s}".format("Type", "Side 1", "Side 2", "Side 3", "Perimeter", "Area", "Angle 1", "Angle 2", "Angle 3"))
for i in range(len(myTriangleList)):
    print("{:>12s} {:>10.3f} {:>10.3f} {:>10.3f} {:>10.3f} {:>10.3f} {:>10.3f} {:>10.3f} {:>10.3f}".format( myTriangleList[i].type(), myTriangleList[i].s1, myTriangleList[i].s2, myTriangleList[i].s3, myTriangleList[i].perimeter(), myTriangleList[i].area(), myTriangleList[i].angles()[0], myTriangleList[i].angles()[1], myTriangleList[i].angles()[2]))