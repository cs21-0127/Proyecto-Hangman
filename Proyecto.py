import random
import os

draw = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''','''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def random_word():
    words = []
    with open("words.txt", "r") as f:
        for line in f:
            words.append(line.rstrip())
    return random.choice(words)

def saved_words():    
    word = random_word()
    unknown_word = "_"*len(word) 
    return word, unknown_word

def replace_letter(word, unknown_word, letter):
    number_of_letters = word.count(letter)
    beginning = 0
    for i in range (number_of_letters):
        position = word.find(letter, beginning)
        unknown_word = unknown_word[:position] + letter + unknown_word[position + 1:]
        beginning = position + 1
    return unknown_word

def hangman():
    print("""
    Bienvenido al videojuego Hangman! Presione la tecla Enter para empezar.
    """)
    input()
    os.system("clear")
    word, unknown_word = saved_words()
    fails = 0
    print(draw[0])
    while unknown_word != word and fails <= 3:
        print("Palabra: " + unknown_word)
        guess = input("Introduzca una letra: ")
        os.system("clear")
        if guess in word:
            unknown_word = replace_letter(word, unknown_word, guess)
            print(draw[fails])
        else:
            fails += 1
            print(draw[fails])        

    if unknown_word == word:
        print("Adivinaste la palabra! " + unknown_word)
    else:
        print("Lo siento, la palabra era: " + word)

def run():
    hangman()

if __name__ == "__main__":
    run()
