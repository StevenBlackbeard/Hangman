import random

print('H A N G M A N')
play = input('Type "play" to play the game, "exit" to quit:')

while play == "play":
    word_in = random.choice(['python', 'java', 'kotlin', 'javascript'])
    word_out = ["-"] * len(word_in)
    count_out = word_out.count("-")
    count_tries = 0
    word_tries = []

    while count_tries < 8 and count_out > 0:
        print()
        print("".join(word_out))
        letter_in = input("Input a letter: ")

        if len(letter_in) != 1:
            print("You should input a single letter")
            continue
        elif not letter_in.islower():
            print("Please enter a lowercase English letter")
            continue
        elif letter_in in word_tries:
            print("You've already guessed this letter")
            continue
        elif letter_in in word_in:
            if letter_in not in word_out:
                for j in range(len(word_in)):
                    if letter_in == word_in[j]:
                        word_out[j] = word_in[j]
                count_out = word_out.count("-")
            else:
                print("No improvements")
                count_tries += 1
                count_out = word_out.count("-")
        else:
            print("That letter doesn't appear in the word")
            count_tries += 1
            count_out = word_out.count("-")

        # add to word tried
        word_tries += letter_in

    # outcome
    if count_out == 0:
        print("You guessed the word!")
        print("You survived!")
    else:
        print("You lost!")

    play = input('Type "play" to play the game, "exit" to quit:')