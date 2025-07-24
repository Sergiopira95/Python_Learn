import random
import os
def run():
  IMAGENES = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
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
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

  DB = [
  "daniel",
"elefante",
  "python",
  "programacion",
  "computadora",  
]
word = random.choice('DB') 
spaces = ["_"] * len(word)
attemps = 6

while True:  
  os.system("clear")
  for character in spaces: 
    print(character, end=" ") 
chousen = input("Elige una letra:")
print(character, end=" ")
print(IMAGENES[attemps])
letter = input("Elige una letra ").upper()

found = False
for idx, character in enumerate(wort):
    if chracater == letter:
         spaces[idx] = letter
         found = True

if not found:
    attemps =- 1

if "_" not in spaces:
  os.system("clear")
  print("Ganaste")
'break'
input()

if attemps == 0:
  os.system("clear")
  print("ganaste")
'break' 
input()





run()