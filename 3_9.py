#Write a program to calculate the area of a triangle given the length of its
#three sides-a, b, and c-using these formulas:
#S = a+b+c / 2
#A= sqrt(s(s- a)(s- b)(s- c))

import math

def main():
    a, b, c = eval(input("Enter a + b + c separated by commas: "))
    s = (a + b + c) / 2
    area = math.sqrt(s * (s-a) * (s-b) * (s-c))
    print("Area is: ", area)

main()
