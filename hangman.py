import random
import hangmanstages

word_list = ['apple', 'banana', 'cherry', "pineapple", "class", "superior", "maryam", "python", "datascience"]

choice = random.choice(word_list)
print("You have 6 lives")
lives = 6
display = ['_' for _ in range(len(choice))]
print(display)

game_over = False
while not game_over:
    guess = input("guessed a letter: ").lower()
    for position, letter in enumerate(choice):
        if letter == guess:
            display[position] = guess
    print(display)
    
    if guess not in choice:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You Lose!....")
    
    if '_' not in display:
        game_over = True
        print("You Win!.....")
    
    print(hangmanstages.stages[lives])

