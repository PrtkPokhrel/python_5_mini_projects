import random

words = ['python', 'america', 'computer', 'pratik', 'keyboard']

# Randomly choses the words from the list
chosen_word = random.choice(words)
word_display = ['_' for _ in chosen_word]
attempts = 8  # Number of allowed attempt

print("Welcome to hangman" "")
print(word_display)


while attempts > 0 and '_'in word_display:
    print('\n'+' '.join(word_display))
    guess = input("Guess a letter: ").lower()

    if guess in chosen_word:
        for index,letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess

    else:
        print("You have guessed incorrectly!")
        attempts -= 1

if "_" not in word_display:
    print("You win!")
    print(' '.join(word_display))
else:
    print("You run out of attempt")
    print("You lose!")