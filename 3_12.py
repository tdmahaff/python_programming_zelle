#Write a program to find the sum of the cubes of the first n natural numbers
#where the value of n is provided by the user.

def main():

    n = eval(input("Enter value n for sum of cubes of first n natural numbers: "))

    sum = 0
    
    for i in range(1, n):
        sum += i ** 3

    print("Sum of cubes of first n natural numbers is: ", sum)

main()
