#Write a program that computes the molecular weight of a carbohydrate (in
#grams per mole) based on the number of hydrogen, carbon, and oxygen
#atoms in the molecule. The program should prompt the user to enter the
#number of hydrogen atoms, the number of carbon atoms, and the number
#of oxygen atoms. The program then prints the total combined molecular
#weight of all the atoms based on these individual atom weights:
#Atom Weight
#(grams I mole)
#H 1.00794
#c 12.0107
#0 15.9994
#For example, the molecular weight of water (H20) is: 2(1.00794) +
#15.9994 = 18.01528.

def main():
    
    hydrogen_gpm = 1.00794
    carbon_gpm = 12.0107
    oxygen_gpm = 15.9994
    num_hydrogen = eval(input("Enter # of hydrogen atoms: "))
    num_carbon = eval(input("Enter # of carbon atoms: "))
    num_oxygen = eval(input("Enter # of oxygen atoms: "))
    print("Molecular weight is ", num_hydrogen * hydrogen_gpm + num_carbon * carbon_gpm + oxygen_gpm * num_oxygen)

main()
