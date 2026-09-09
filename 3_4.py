#Write a program that determines the distance to a lightning strike based on
#the time elapsed between the flash and the sound of thunder. The speed
#of sound is approximately 1100 ft/ sec and 1 mile is 5280 ft.

def main():
    time = eval(input("Enter time in seconds elapsed between flash and sound of thunder: "))
    distance = 1100 * time / 5280
    print("Distance is", distance, "miles")

main()
