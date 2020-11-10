from os import *
import tkinter as Tk
from tkinter import *



# Create the root window
window = Tk()

# Set the window dimension and her title
window.geometry("480x240")
window.title("Année bissextile ou pas ?")

# We create a text to ask user to enter a year number
ask_user_label = Label(window, text = "Veuillez saisir une année :", font = ('calibri', 20, 'bold'))
ask_user_label.pack()

# Creating new label where the result of calculLYONOT function is shown, leap year or not ?
resultLabel = Label(window, font = ('calibri', 16, 'bold'))
resultLabel.pack()
resultLabel.place(x = 115, y = 120)

# Creating the area where the user can type the year number
yearEntry = IntVar()
user_entry = Entry(window, textvariable = yearEntry, width = 20)
user_entry.pack()

# Function to calculate if the year is a leap year or not
def calculLYONOT():
    x = int(yearEntry.get())
    if x % 400 == 0 or x % 4 == 0 and x % 100 != 0:
        resultLabel.config(text= "{} est une année bissextile".format(x), fg= "green")
    else:
        resultLabel.config(text= "{} n'est pas une année {} bissextile".format(x, "\n"), fg= "red")

# Setting a button that the user click to calculate if it's a leap year or not
btnCalculate = Button(window, text = "Calculer", command = calculLYONOT)
btnCalculate.pack()

# Setting a button to quit the program
btnQuit = Button(window, text = "Quitter", command = window.quit, font = ('calibri', 16, 'bold'))
btnQuit.pack()
btnQuit.place(x = 380, y = 180)





window.mainloop()