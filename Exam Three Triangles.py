import math
class Triangle():
    def __init__(self, float1, float2, float3):
        self.s1 = float1
        self.s2 = float2
        self.s3 = float3

    def type(self):
        if(self.s1 == self.s2 and self.s2 == self.s3):
            return "Equilateral"
        elif(self.s1 == self.s2 or self.s2 == self.s3 or self.s1 == self.s3):
            return "Isoceles"
        elif(self.s1 != self.s2 and self.s2 != self.s3 and self.s1 != self.s3):
            return "Scalene"
    
    def perimeter(self):
        perimetertotal = self.s1 + self.s2 + self.s3
        return perimetertotal
    
    def area(self):
        s = (self.s1 + self.s2 + self.s3)/2
        areatotal = math.sqrt(s*(s - self.s1)*(s - self.s2)*(s - self.s3))
        return areatotal
    
    def angles(self):
        angle1 = math.acos(((self.s2*self.s2)+(self.s3*self.s3)-(self.s1*self.s1))/(2*self.s2*self.s3))
        angle2 = math.acos(((self.s1*self.s1)+(self.s3*self.s3)-(self.s2*self.s2))/(2*self.s1*self.s3))
        angle3 = math.acos(((self.s2*self.s2)+(self.s1*self.s1)-(self.s3*self.s3))/(2*self.s2*self.s1))
        angle1 = angle1*(180/math.pi)
        angle2 = angle2*(180/math.pi)
        angle3 = angle3*(180/math.pi)
        Angles = [angle1, angle2, angle3]
        return Angles
    

TriangleList = []

inputFile = "Exam Three Triangles.txt"
input = open(inputFile, 'r')
x = input.readline()
while (x != ""):
    TriangleFile = x.split(",")
    string_with_numbers = TriangleFile[2]
    numbers_only = ""
    for char in string_with_numbers:
        if char.isdigit():
            numbers_only += char
    S1 = float(TriangleFile[0])
    S2 = float(TriangleFile[1])
    S3 = float(numbers_only)
    TriangleList.append(Triangle(S1, S2, S3))
    x = input.readline()
input.close()

print("        Type     Side 1     Side 2     Side 3  Perimeter       Area    Angle 1    Angle 2    Angle 3")
for p in range(len(TriangleList)):
    area = "{:.3f}".format(TriangleList[p].area())
    perimeter = "{:.3f}".format(TriangleList[p].perimeter())
    Angles = [] 
    Angles = TriangleList[p].angles()
    TriType = TriangleList[p].type()
    Side1 = "{:.3f}".format(TriangleList[p].s1)
    Side2 = "{:.3f}".format(TriangleList[p].s2)
    Side3 = "{:.3f}".format(TriangleList[p].s3)
    Angle1 = "{:.3f}".format(Angles[0])
    Angle2 = "{:.3f}".format(Angles[1])
    Angle3 = "{:.3f}".format(Angles[2])
    print(TriType.rjust(12) , Side1.rjust(10) , Side2.rjust(10) , Side3.rjust(10) , perimeter.rjust(10) , area.rjust(10), Angle1.rjust(10), Angle2.rjust(10), Angle3.rjust(10))
   