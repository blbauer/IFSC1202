import math
variable = math.pi
print(f"Using Numeric variable = {variable}")
print(f"|{variable:25}|")
print(f"|{variable:<25}|")
print(f"|{variable:>25}|")
print(f"|{variable:^25}|")
print()
variable = "Python 3.9"
print(f"Using String {variable = }")
print(f"|{variable:25}|")
print(f"|{variable:<25}|")
print(f"|{variable:>25}|")
print(f"|{variable:^25}|")

from math import pi
variable = pi
print(f"Using String variable = {variable}")
print(f"|{variable:=<25}|")
print(f"|{variable:=>25}|")
print(f"|{variable:=^25}|")
print()
variable = "Python 3.9"
print(f"Using String variable = {variable}")
print(f"|{variable:=<25}|")
print(f"|{variable:=>25}|")
print(f"|{variable:=^25}|")

import math
variable = 10
print(f"Using Numeric variable = {variable}")
print(f"This prints without formatting {variable}")
print(f"This prints with formatting {variable:d}")
print(f"This prints also with formatting {variable:n}")
print(f"This prints with spacing {variable:10d}")
print()
variable = math.pi
print(f"Using Numeric variable = {variable}")
print(f"This prints without formatting {variable}")
print(f"This prints with formatting {variable:f}")
print(f"This prints with spacing {variable:20f}")

variable = 4
print(f"Using Numeric variable = {variable}")
print(f"This prints without formatting {variable}")
print(f"This prints with percent formatting {variable:%}")
print()
variable = 403267890
print(f"Using Numeric variable = {variable}")
print(f"This prints with exponential formatting {variable:e}")

variable = 1200356.8796
print(f"Using Numeric variable = {variable}")
print(f"With two decimal places: {variable:.2f}")
print(f"With four decimal places: {variable:.3f}")
print(f"With two decimal places and a comma: {variable:,.2f}")
print(f"With a forced plus sign: {variable:+.2f}")
print()
variable *= -1
print(f"Using Numeric variable = {variable}")
print(f"With two decimal places and a comma: {variable:,.2f}")


print(f'{"Number":>10s}{"Square":>10s}{"Cube":>10s}')
x = 1.0
print(f'{x:10.2f}{x*x:10.2f}{x*x*x:10.2f}')
x = 2.0
print(f'{x:10.2f}{x*x:10.2f}{x*x*x:10.2f}')
x = 3.0
print(f'{x:10.2f}{x*x:10.2f}{x*x*x:10.2f}')

APPLES = .50
BREAD = 1.50
CHEESE = 2.25
numApples = 3
numBread = 10
numCheese = 6
prcApples = numApples * APPLES
prcBread = numBread* BREAD
prcCheese = numCheese * CHEESE
strApples = 'Apples'
strBread = 'Rye Bread'
strCheese = 'Cheese'
total = prcBread + prcCheese + prcApples
print(f'{"My Grocery List":^30s}')
print(f'{"="*30}')
print(f'{strApples:10s}{numApples:10d}{"":5s}${prcApples:>5.2f}')
print(f'{strBread:10s}{numBread:10d}{"":5s}${prcBread:>5.2f}')
print(f'{strCheese:10s}{numCheese:10d}{"":5s}${prcCheese:>5.2f}')
print(f'{"":10s}{"Total:":>10s}{"":5s}${total:>5.2f}')

from math import pi
# String Examples
print("{}".format("hello"))            #|h|e|l|l|o|
print("{:8s}".format("hello"))         #|h|e|l|l|o| | | |
print("{:>8s}".format("hello"))        #| | | |h|e|l|l|o|
print("{:^8s}".format("hello"))        #| |h|e|l|l|o| | |
print("{:^4.2s}".format("hello"))       #| |h|e| |
# Integer Examples
print("{:4d}".format(42))              #| | |4|2|
print("{:04d}".format(42))             #|0|0|4|2|
# Floating Point Examples
print("{:6.2f}".format(pi))            #| | |3|.|1|4|
print("{:06.2f}".format(pi))           #|0|0|3|.|1|4|
print("{:,.2f}".format(123456789.017)) #|1|2|3|,|4|5|6|,|7|8|9|.|0|2|
# Other Examples

one = "one"
two = "two"
three = "three"

print("{} | {} | {}".format("one","two","three"))
print("one = {:s}, two = {:s}, three = {:s}".format(one, two, three))
print("one = {:8s}, two = {:8s}, three = {:8s}".format(one, two, three))
print("one = {:.2s}, two = {:.2s}, three = {:.2s}".format(one, two, three))
print("x{:4.1f}x".format(pi))
print('{:,.2f}'.format(123456789.017))

Hi = 8.5
Lo = -4.4

print("{}{}".format(Hi, Lo))
print("Todays high is {}, the low is {}.".format(Hi, Lo))
print("Todays high is {:8.2f}, the low is {:8.2f}.".format(Hi, Lo))

print("{:^8s}{:^8s}".format("Hi","Low"))
print("{:8.1f}{:8.1f}".format(91.5, 66.4))
print("{:8.1f}{:8.1f}".format(101.5, 55.4))
print("{:8.1f}{:8.1f}".format(8.5, -4.4))