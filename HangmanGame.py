import random

word_list = [
    "Agra", "Ajmer", "Alwar", "Bhuj", "Delhi", "Daman", "Gaya", "Goa",
    "Imphal", "Kochi", "Kota", "Mandi", "Patna", "Pune", "Salem", "Shimla",
    "Surat", "Udupi", "Vapi"
]

stages = [r'''
      _______
     |/      |
     |      (_)
     |      /|/
     |       |
     |      / /
     |
 ____|____
''', r'''
      _______
     |/      |
     |      (_)
     |      /|/
     |       |
     |      / 
     |
 ____|____
''', r'''
      _______
     |/      |
     |      (_)
     |      /|/
     |       |
     |      
     |
 ____|____
''', r'''
      _______
     |/      |
     |      (_)
     |      /|/
     |       
     |      
     |
 ____|____
''', r'''
      _______
     |/      |
     |      (_)
     |      
     |       
     |      
     |
 ____|____
''', r'''
      _______
     |/      |
     |      
     |      
     |       
     |      
     |
 ____|____
''']

print(r'''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/     
''')

print("Guess the names of Indian Cities and save the hangman!")

lives = len(stages) - 1
choosen_word = random.choice(word_list)
word_length = len(choosen_word)

# Uncomment to debug the chosen word
# print(f"Chosen word: {choosen_word}")

placeholder = ["_"] * word_length
print("".join(placeholder))

game_over = False
correct_letter = []

while not game_over:
    guess = input("Guess a letter: ").lower()
    print(guess)

    found = False

    for letter in range(word_length):
        if choosen_word[letter].lower() == guess:
            placeholder[letter] = choosen_word[letter]
            found = True

    print("".join(placeholder))
    print(f"Lives left: {lives}")

    if guess not in choosen_word.lower():
        lives -= 1
        if lives < 0:
            game_over = True
            print("*==================== You Lose ====================*")
            print(f"The word was: {choosen_word}")

    stage_index = lives if lives >= 0 else 0
    print(stages[stage_index])

    if "_" not in placeholder:
        game_over = True
        print("*==================== You Win =====================*")
