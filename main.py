from wonderwords import RandomWord
import colorama
from colorama import Fore

r = RandomWord()
random_word = r.word(word_min_length=5, word_max_length=15)
colorama.init(autoreset=True)

print(f"Go and guess the {len(random_word)} lettered word, you fool!!")
print("You have 5 points to start with! every correct word +1, every wrong word -2 \n")
print(f"{len(random_word) * ' _ '} \n")

points = 5
letter_lst = ['_'] * len(random_word)
letters_indexes = {}
incorrect_letters = []

for letter_index in range(len(random_word)):
    if random_word[letter_index] not in letters_indexes:
        letters_indexes[random_word[letter_index]] = [letter_index]
    else:
        letters_indexes[random_word[letter_index]].extend([letter_index])

while points > 0:
    guess_type = False
    user_guess = input('Guess your letter:')
    if len(user_guess) > 1:
        print("you think you can cheat you little SCUM ?, try again! -1 for being a bad boy")
        points = points - 1

    if user_guess in random_word:
        print(f"correct the letter {user_guess} is in the word, +1 point!")
        guess_type = True
        points = points + 1
        for index in letters_indexes[user_guess]:
            letter_lst[index] = user_guess
        print(' '.join(letter_lst))

    else:
        print(f"{user_guess} is a wrong letter -2 point")
        incorrect_letters.append(user_guess)
        points = points - 2

    if guess_type:
        color = Fore.GREEN
        symbol = '↑'
    else:
        color = Fore.RED
        symbol = '↓'
    print(f"""Your score is: {color}{points} {symbol}""")
    print('\n')

