#Write a program that approximates the value of pi by summing the terms
#of this series: 4/1- 4/3 + 4/5- 4/7 + 4/9- 4/11 + . . . The program should
#prompt the user for n, the number of terms to sum, and then output the
#sum of the first n terms of this series. Have your program subtract the
#approximation from the value of math. pi to see how accurate it is.

import math

def main():

    n = eval(input("Enter number of terms to sum: "))

    sum = 0

    for i in range(n):
        sum += 4 / (2 * i + 1) * -1 ** (i)

    print("Sum is ", sum)
    print("Accuracy is ", math.pi - sum)

main()
