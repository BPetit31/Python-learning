
# It's a simple program that simulate an account creation where user choose his username and password and create an account store in a .yaml file
# Then the user can use his newly created account to log in the program and get a successful message if the informations match from .yaml file to 
# Python.
import tkinter as Tk
from tkinter import *
import pickle
import os
import bissextileGUI

# We create the GUI window, set the size and the tittle
window = Tk()
window.geometry("480x240")
window.title("Maxi outil -en developpement-")

# Creating 3 label area to show username line and password line before setting up the entry
# And one label to ask the user if he don't have an access yet.
EnterUsername = Label(window, text = "Nom utilisateur :")
EnterUsername.pack()
EnterUsername.place(x = 40, y = 30)
EnterPassword = Label(window, text = "Mot de passe :")
EnterPassword.pack()
EnterPassword.place(x = 40, y = 70)
UserNoAccount = Label(window, text = "Pas encore d'accès ? Cliquez sur 'Créer un accès'")
UserNoAccount.pack()
UserNoAccount.place(x = 100, y = 160)
WrongPasswordLabel = Label(window)
WrongPasswordLabel.pack()
WrongPasswordLabel.place(x = 120, y = 100)

# Creating 2 entry to catch the username and the password typed by the user
username = StringVar()
password = StringVar()
EnterUsernameEntry = Entry(window, text = username, width = 20)
EnterUsernameEntry.pack()
EnterUsernameEntry.place(x = 150, y = 33)
EnterPasswordEntry = Entry(window, text = password, width = 20)
EnterPasswordEntry.pack()
EnterPasswordEntry.place(x = 150, y = 73)

# I define the function for the Create Account button that will open a new window
# where the user will create his access (username and password)

def OpenNewAccessWindow():

    newAccessWindow = Toplevel(window)
    newAccessWindow.geometry("400x210")
    newAccessWindow.title("Maxi outil : création nouvel accès utilisateur")

    # Creating new label to inform user he can enter in the entry his new username and password
    InformUser = Label(newAccessWindow, text = "Saisissez votre nouvel identifiant et mot de passe \n dans les champs ci-dessous")
    InformUser.pack()
    InformUser.place(x = 85, y = 10)

    # I create label and entry for the user to type his new username and password
    NewUserLabel = Label(newAccessWindow, text = "Nom d'utilisateur :")
    NewUserLabel.pack()
    NewUserLabel.place(x = 40, y = 50)
    NewPasswordLabel = Label(newAccessWindow, text = "Mot de passe :")
    NewPasswordLabel.pack()
    NewPasswordLabel.place(x = 40, y = 100)
    NewResultLabel = Label(newAccessWindow)
    NewResultLabel.pack()
    NewResultLabel.place(x = 85, y = 170)

    NewUsername = StringVar()
    NewPassword = StringVar()
    NewUserEntry = Entry(newAccessWindow, text = NewUsername, width = 20)
    NewUserEntry.pack()
    NewUserEntry.place(x = 150, y = 53)
    NewPasswordEntry = Entry(newAccessWindow, text = NewPassword, width = 20)
    NewPasswordEntry.pack()
    NewPasswordEntry.place(x = 150, y = 103)

    # Creating the function to encrypt the new password and save the user newly created informations in the .yaml file and close the window
    def NewAccount():
        SavedUsername = NewUsername.get()
        SavedPassword = NewPassword.get()
        with open('users.py', 'w') as userfile:
           pickle.dump(SavedUsername, SavedPassword, userfile)
        NewResultLabel.config(text = "Vos identifiants sont bien crées. Veuillez cliquer sur le bouton 'Quitter'")
    # Building 2 buttons, one to call the NewAccount function, another to quit the window
    NewUserCreateButton = Button(newAccessWindow, text = "Créer accès", command = NewAccount, fg = "green")
    NewUserCreateButton.pack()
    NewUserCreateButton.place(x = 150, y = 120)
    NewUserQuitButton = Button(newAccessWindow, text = "Quitter", command = newAccessWindow.quit)
    NewUserQuitButton.pack()
    NewUserQuitButton.place(x = 315, y = 175)

def OpenConnectSelfWindow():

    ValableUsername = username.get()
    ValablePassword = password.get()
    if ValableUsername == "Benoit" and ValablePassword == "simplon":
        exec(open('bissextileGUI.py').read())
    else:
        WrongPasswordLabel.config(text = "Le mot de passe ne correspond pas", fg = "red")

# We create 2 button, one to log in the program when username and password match those in the .yaml file
# Another button to open a new window where the new user create his username and password
LogInButton = Button(window, text = "Se connecter", command = OpenConnectSelfWindow)
LogInButton.pack()
LogInButton.place(x = 170, y = 100)
CreateAccount = Button(window, text = "Créer un accès", command = OpenNewAccessWindow)
CreateAccount.pack()
CreateAccount.place (x= 165, y = 190)

window.mainloop()

