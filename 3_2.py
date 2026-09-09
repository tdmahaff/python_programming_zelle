#Write a program that calculates the cost per square inch of a circular pizza,
#given its diameter and price. The formula for area is A = pi*r^2

import math

def main():
    diameter = eval(input("Enter diameter value: "))
    price = eval(input("Enter price: "))
    area = math.pi * (diameter / 2) ** 2
    cost = area / price
    print("Cost per square inch is ", cost)

main()
    
