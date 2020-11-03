import os
import pathlib
import pickle  
import random
from donnees import *

# Function to greet the user and explain the rules.
def game_rules():
    welcome_user = """Bienvenue à vous ! Que diriez-vous en cette belle ou moins belle journée de faire un petit pendu ?
Je m'appelle Benoit o/ et je serai votre hôte dans ce petit jeu macabre."""
    explain_rules = """Avant de commencer, je vous explique les règles du jeu. Elles sont simples et mortelles...
Vous devez deviner le mot caché et pour le deviner, vous avez 8 essais.\n
Je vais vous inviter à saisir une lettre que vous pensez être dans le mot qui est caché.
Si cette lettre se trouve dans le mot alors elle apparaitra à la/les position(s) ou elle se situe dans
le mot.\n
Mais attention, si vous me donnez une lettre qui n'est pas dans le mot, et bien... vous decouvrirez vite
pourquoi j'appelle ce jeu "le pendu" *rire sardonique*.
Pour chaque mauvaise lettre saisie, vous perdez 1 essai."""

    print(welcome_user)
    print("--------------------------------------------------------------------------")
    print(explain_rules)
    print("--------------------------------------------------------------------------")

# Function used to catch the player name(username). The username is an 8 alphanumerical characters length. The function will verify
# if only alphanumerical characters are typed and return an error if not. The user will be asked again to type his username.

def catch_username():
    
    username = input("Quel est votre nom ? ")
    # I capitalize the first letter of the username
    username = username.capitalize()
    # Check if username is between 1 and 8 alphanumerical char
    if len(username) > 8 or not username.isalnum():
        print("Veuillez saisir un nom entre 1 et 8 caractères, sans signes particuliers(ex : @!:;).")
        return catch_username()
    else:
        print("Prêt pour un pendu {} ?".format(username))

# The next function choose randomly a word, this is the word the player need to guess. It's chosen from the "donnees.py" 
# "list_words" variable.

def random_secret_word():
    return random.choice(list_words)

# This function catch the letter the player as chose and verify if it's in the secret word or not.

def catch_letter():
    letter = input("Choisissez une lettre : ")
    letter = letter.lower()
    if len(letter) > 1 or not letter.isalnum():
        print("Indiquez une seule lettre de l'alphabet.")
        return catch_letter
    else:
        print("Voyons si cette lettre se trouve dans le mot...")

# The function that return the secret word in function of the letters the player has found or hide the letters which are not
# found yet.
# Je ne suis pas arrive à saisir cette fonction moi-même, je m'inspire donc clairement de celle du cours Openclassroom "Apprenez
# à programmer en Python".

def find_secret_word(full_word, found_letters):
    secret_word = ""
    for letters in full_word:
        if letters in found_letters:
            secret_word += letters
        else:
            secret_word += "*"
    return secret_word

# Find_scores_file is the function that open the "scores" file in read bytes mode. If the file can't be found, it will create
# an empty dictionnary.

def find_scores():
    
    p_scores = {}
    if os.path.getsize("scores") > 0:
        with open("scores", "rb") as f:
            unpickler = pickle.Unpickler(f)
            p_scores = unpickler.load()

# Here i save the player score in write bytes mode into the "scores" file. Using pickler to do this.

def save_scores():
    p_scores = open(scores, "wb")
    serialize = pickle.Pickler(p_scores)
    serialize.dump(pr_scores)
    p_scores.close()