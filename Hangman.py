import random

word_list = ["ardvardk", "baboon", "camel"]
chosen_word = random.choice(word_list)

lives = 6

display = []
word_length = len(chosen_word)
for n in range(word_length):
    display.append("_")
print(display)

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter:\n").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        print(f"A wrong guess!\nYou have {lives} lives left.")
        if lives == 0:
            end_of_game = True
            print("You lose!")

    print(display)
    if "_" not in display:
        end_of_game = True
        print("You win!")