#Write a program that finds the average of a series of numbers entered by
#the user. As in the previous problem, the program will first ask the user
#how many numbers there are. Note: The average should always be a float,
#even if the user inputs are all ints.

def main():

    num = eval(input("Enter how many numbers are to be summed: "))

    count = 0
    sum = 0
    
    while count < num:
        sum += eval(input("Enter number to be summed: "))
        count += 1

    average = float(sum) / num;

    print("Average is ", average)

main()
