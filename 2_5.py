# 2.5: Modify the convert.py program (Section 2.2) so that it computes and
# prints a table of Celsius temperatures and the Fahrenheit equivalents every
# 10 degrees from 0°C to 100°C.
# convert.py
# A program to convert Celsius temps to Fahrenheit
# by: Susan Computewell
def main() :
    for i in [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
        celsius = i
        fahrenheit = 9/5 * celsius + 32
        print("The temperature is", fahrenheit, "degrees Fahrenheit.")
        print("The temperature is", celsius, "degrees Celsius")
main()
