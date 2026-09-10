#A Fibonacci sequence is a sequence of numbers where each successive
#number is the sum of the previous two. The classic Fibonacci sequence
#begins: 1, 1, 2, 3, 5, 8, 13, . . .. Write a program that computes the nth
#Fibonacci number where n is a value input by the user. For example, if
#n = 6, then the result is 8.

def fibonacci(n):

    a, b = 1, 1

    for i in range(n-1):
        a, b = b, a + b
    return a

n = eval(input("Enter n: "))
print("The fibonacci number is ", fibonacci(n))
