#Write a program that accepts two points (see previous problem) and determines
#the distance between them.
#distance= sqrt((x2- x1)^2 + (y2- y1)^2)

import math

def main():
    x1, y1 = eval(input("Enter x1, comma, then y1: "))
    x2, y2 = eval(input("Enter x2, comma, then y2: "))
    distance = math.sqrt((x2-x1) ** 2 + (y2-y1) ** 2)
    print("Distance is", distance)

main()
