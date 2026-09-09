#The Konditorei coffee shop sells coffee at $10.50 a pound plus the cost
#of shipping. Each order ships for $0.86 per pound + $1.50 fixed cost for
#overhead. Write a program that calculates the cost of an order.

def main():
    pounds = eval(input("Enter # of coffee pounds purchasing: "))
    cost = 11.36 * pounds + 1.5
    print("Cost of the order is", cost)

main()
        
