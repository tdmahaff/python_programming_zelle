import math

def main():
    radius = eval(input("Input radius: "))
    volume = 4/3*math.pi*pow(radius, 3)
    area = 4*math.pi*pow(radius, 2)
    print("Volume is: ", volume, "Area is: ", area)

main()
         
