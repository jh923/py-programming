def mainloop():
    MIN = 0
    MAX = 100
    ATTEMPT = 0
    FOUND = False

    while not FOUND:
        GUESS = ((MIN + MAX) // 2)
        print("Is the number %d" % GUESS)
        ANSWER = input("Only write 'higher' or 'lower' or 'yes' ")

        if ANSWER == "higher":
            MIN = GUESS
            ATTEMPT += 1
        elif ANSWER == "lower":
            MAX = GUESS
            ATTEMPT += 1
        elif ANSWER == "yes":
            ATTEMPT += 1
            print("The number was %s, it took %s guesses to find" % (GUESS, ATTEMPT))
            FOUND = True
        else:
            print("Please enter a valid response")


mainloop()
