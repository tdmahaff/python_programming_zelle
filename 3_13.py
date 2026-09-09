#Write a program to sum a series of numbers entered by the user. The
#program should first prompt the user for how many numbers are to be
#summed. The program should then prompt the user for each of the numbers
#in turn and print out a total sum after all the numbers have been
#entered. Hint: Use an input statement in the body of the loop.

def main():

    num = eval(input("Enter how many numbers are to be summed: "))

    count = 0
    sum = 0
    
    while count < num:
        sum += eval(input("Enter number to be summed: "))
        count += 1

    print("Sum is ", sum)

main()
