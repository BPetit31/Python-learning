# Test program from "Learn how to program in Python" - Openclassrooms
annee = input("Saisissez une année : ")
annee = int(annee)
if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
    print("Cette année est bisextile.")
else:
    print("Ce n'est pas une année bisextile.")
    