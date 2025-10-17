import random

word_bank = []

with open("word_bank.txt", "r") as file: 
    for line in file:
        word_bank.append(line.strip().upper()) # parse file, strip whitespace, convert to uppercase and add each word to word_bank
        
chosen_word = random.choice(word_bank)

misplaced_letters = []
incorrect_letters = []
attempts = 6
current_attempt = 1

def count_letters(word):   # helper function to count occurrences of each letter in a word
  letter_count = {}
  for letter in word:
    if letter in letter_count:
      letter_count[letter] += 1
    else:
      letter_count[letter] = 1
  return letter_count

print("""-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                                             WORDLE
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

RULES:\n
* You have 6 attempts to guess the 5-letter word.

* After each guess, you'll receive feedback:
  - Correct letters in the correct position will be filled in.
  - Positions where the letter is incorrect will be shown as an underscore (_).
  - You will be told which letters from your guess are in the word but not in the correct position.
  - You will be told which letters from your guess are not in the word.\n""")

while current_attempt <= attempts:   # main game loop
  
  print(f"\nATTEMPT {current_attempt}")
  
  guess = input("Enter your guess: ").strip().upper() # get user input, strip whitespace, convert to uppercase
  
  print("\n"+guess)
  
  if len(guess) != 5 or not guess.isalpha():                  # input validation
    print("Invalid input. Please enter a 5-letter word.\n")
    continue
  
  index = 0
  game_state = "_____" # initialize game state with underscores for unguessed letters
  
  for letter in guess:
    
    if letter == chosen_word[index]:
      game_state = game_state[:index] + letter + game_state[index+1:] # update game state with correctly guessed letter
      
      if letter in misplaced_letters:
        misplaced_letters.remove(letter) # remove letter from misplaced if now correctly placed
      
    elif letter in chosen_word and not (misplaced_letters) and (count_letters(guess).get(letter) < 2): # check for misplaced letters while avoiding duplicates
      misplaced_letters.append(letter)
      
    elif letter not in chosen_word and letter not in incorrect_letters:
      incorrect_letters.append(letter) # add to incorrect letters if not already present
      
    index += 1
  
  print(game_state) # display updated game state after each guess
  
  print(f"""\n\nFEEDBACK: \n
* Misplaced Letters: {misplaced_letters}\n
* Incorrect Letters: {incorrect_letters}\n""")
    
  current_attempt += 1
  
  if guess == chosen_word:
    print(f"""\n\U0001F973 \U0001F389 CONGRATULATIONS! You guessed the word '{chosen_word}' correctly! \U0001F973 \U0001F389""")
    break
  
if current_attempt > attempts:
  print(f"""\n\U0001F622 \U0001F494 SORRY! You've used all your attempts. The correct word was '{chosen_word}'. \U0001F622 \U0001F494""")