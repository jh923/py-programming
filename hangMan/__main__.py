import random

WORDS = ["london", "tokyo", "hong kong", "new york", "canterbury", "paris"]

def mainloop():
    print("City name hang man")
    num = random.randint(0, 5)
    ANSWER = WORDS[num]
    wrong = []
    right = []
    FOUND = write(ANSWER, right)

    print("The layout of the city name is: %s" % FOUND)
    while True:
        # Lost the game
        if len(wrong) == 6:
            print("You guessed wrong to many times. The answer was %s." % ANSWER)
            break
        if ''.join(FOUND) == ANSWER:
            print("You have successfully guessed the city name %s, only making %s mistakes." % (ANSWER, len(wrong)))
            break
        # Input a letter
        INPUT = input("Please enter a character. ")
        # Validate input
        if len(INPUT) != 1:
            print("Please enter one letter at a time")
        elif len(INPUT) == 0:
            print("Please enter a letter")
        else:
            # CHeck if imputed letter is in the name of the city, if so
            if (INPUT in wrong) or (INPUT in right):
                print("You have already already guessed teh character '%s'." % INPUT)
            elif INPUT in ANSWER:
                print("%s is in the name" % INPUT)
                right.append(INPUT)
                FOUND = write(ANSWER, right)
                print("So far the city name looks like ths: %s, and you have made %s incorrect guesses being: %s."
                      % (FOUND, len(wrong), wrong))
            else:
                wrong.append(INPUT)
                print("So far the city name looks like ths: %s, and you have made %s incorrect guesses being: %s."
                      % (FOUND, len(wrong), wrong))


# fill in the found letters. Currently a bug with the space key
def write(word, letterList):
    result = ["_"] * len(word)
    for i in range(len(letterList)):
        for j in range(len(word)):
            if letterList[i] == word[j]:
                result[j] = letterList[i]
            if letterList[i] == " ":
                result[j] = " "
    return result


mainloop()