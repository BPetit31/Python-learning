import os  # We import the OS module to use variables and functions to speak with
           # our OS

# program to know if it's a leap year or no
def main():
    annee = input("Saisissez une année : ")
    annee = int(annee)
    if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
        print("L'année saisie est bissextile.")
    else:
        print("L'année saisie n'est pas bissextile.")

while True:
    main()
    if input("Voulez-vous recommencer ? (O/N) ").strip().upper() != "O":
        break

os.system("pause") # We ask the programme to stay in pause and prevent closing from Windows
