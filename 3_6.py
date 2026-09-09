#Two points in a plane are specified using the coordinates (x1,y1) and
#(x2,y2). Write a program that calculates the slope of a line through two
#(non-vertical) points entered by the user.
#slope = y2 - y1 / x2 - x1

def main():
    x1, y1 = eval(input("Enter x1, comma, then y1: "))
    x2, y2 = eval(input("Enter x2, comma, then y2: "))
    slope = (y2 - y1) / (x2 - x1)
    print("Slope is ", slope)

main()
