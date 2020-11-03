import os
import random
import pathlib
from donnees import *
from fonctions import *

# We greet the player and explain the rules
welcome_player = game_rules()
print(welcome_player)

# Here we get the username and the score if the user already got one, if not, it will add it.
player_name = catch_username()
player_score = find_scores()
if player_name not in player_score.keys():
    player_score[player_name] = 0

# The main program
continue_game = "o"
while continue_game != "n":
    print("Joueur {0}: Vous avez {1} point(s).".format(player_name, player_score[player_name]))
    s_word_to_find = random_secret_word()
    found_letter = []
    found_word = find_secret_word(full_word, found_letter)
    p_lives = player_lives
    while s_word_to_find != found_word and p_lives > 0:
        print("Le mot à trouver {0} (il vous reste {1} chance(s).".format(found_word, p_lives))
        p_letter = catch_letter()
        if p_letter in found_letter:
            print("Vous avez déjà sélectionné cette lettre.")
        elif p_letter in s_word_to_find:
            found_letter.append(p_letter)
            print("""Cette lettre se trouve bien dans le mot. Bien joué à vous, on va peut être
            éviter un drame aujourd'hui !"
            """)
        else:
            p_lives -= 1
            print("""Oups mauvais choix, cette lettre n'est pas dans le mot. On va bientôt hisser
            la corde...
            """)
        found_word = find_secret_word(full_word, found_letter)
    
    # We check if the player found the secret word or if he lose
    if s_word_to_find == found_word:
        print("""Coupez moi cette corde, vous avez gagné la partie et sauvé une vie !
        Le mot à trouver était bien {}
         """.format(s_word_to_find))
    else:
        print("Vous avez perdu ! C'est leur de la pendaison !")

    # Here we update the player score and ask if he want to continue the game
    player_score[player_name] += player_lives
    continue_game = input("Vous êtes d'humeur à refaire une partie (O/N) ?")
    continue_game = continue_game.lower()

save_scores(player_score)
print("Et bien ce petit jeu est terminé... Vous avez un score de {} point(s).".format(player_score[player_name]))

os.system("pause")