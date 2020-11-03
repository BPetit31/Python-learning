import os
import random
import math
# ZCasino is a simple casino roulette app. You bet an $ amount on red or black slot and the random function will do the job.
# Get *3 rewards if you get the good number and only a 50% return of your bet if you get the good color. Else you lose your bet.

#partie de code rajoutée après correction sur tuto Openclassrooms
wallet = 500 #You have 500$ at the beginning of the game
continue_game = True #Bool who's True while you continue the game
#fin du rajout de code

print("Vous entrez dans un casino à l'ambiance cosy et agréable. Vous avez", wallet, "$ dans votre portefeuille. Vous vous asseyez à la table de roulette.")

while continue_game:

    numb_answer = -1
    while numb_answer < 0 or numb_answer > 49:
        numb_answer = int(input("Choisissez un chiffre entre 0 et 49 :"))
        try:
            numb_answer = int(numb_answer)
        except ValueError:
            print("Veuillez saisir un nombre entre 0 et 49.")
            numb_answer = -1
            continue
        if numb_answer < 0:
            print("Vous ne pouvez pas choisir un nombre négatif.")
        if numb_answer > 49:
            print("Ce nombre est supérieur à 49. Choisissez un nombre entre 0 et 49.")

    bet_answer = 0
    while bet_answer <= 0 or bet_answer > wallet:
        bet_answer = input("Combien souhaitez-vous miser ?")
        try:
            bet_answer = int(bet_answer)
        except ValueError:
            print("Vous n'avez pas saisi un nombre.")
            bet_answer = -1
            continue
        if bet_answer > wallet:
            print("Vous ne pouvez pas miser autant, vous n'avez que ", wallet, "$")
        if bet_answer <= 0:
            print("Veuillez saisir un nombre positif")
    else:
        print("Quel excellent choix !")

    rand_number = random.randrange(0, 50)
    print("Rien ne va plus, faites vos jeux ! Le numéro gagnant est le :", rand_color, rand_number, ".")
    if numb_answer == rand_number:
        print("BRAVO ! Vous avez gagné 3 fois votre mise :", bet_answer * 3, "$")
        wallet += bet_answer
    else:
        print("Pas de chance pour cette fois. Please come again !")
        wallet -= bet_answer

    if wallet <= 0:
        print("Vous êtes à sec ! Dehors l'ami.")
        continue_game = False
    else:
        print("Vous avez désormais :", wallet, "$")
        leave = input("Voulez-vous quitter le casino (oui/non) ?")
        if leave == "OUI" or leave == "OUI":
            continue_game = False

os.system("pause")