import random


# Take a integer input 0 <= n <= 2 and return either rock, paper or scissors
def map(opRoll):
    return {
        0: "Rock",
        1: "Paper",
        2: "Scissors",
    }[opRoll]


def endOfMatch(p, c, t):
    print("Thanks for playing.")
    if (p+c+t) == 0:
        print()
    elif p > c:
        print("You are the winner with a final score of: ", p, " wins, ", c, " losses and ", t, " ties.")
    elif c > p:
        print("You lost with a final score of: ", p, " wins, ", c + " losses and ", t, " ties.")
    elif c == p:
        print("The game ended in a tie!")


def mainloop():
    playerwin = 0
    cpuwin = 0
    ties = 0

    while True :
        # Ask human layer for their input
        playerChoice = input("Type Rock, Paper, or Scissors to play, or type quite to exit the game: ")
        # Check if input is legal and do appropriate action
        if playerChoice == "Quit":
            endOfMatch(playerwin, cpuwin, ties)
            break
        elif playerChoice == ("Rock" or "Paper" or "Scissors"):
            opRoll = random.randint(0, 2)
            opChoice = map(opRoll)
            print("The computer chose: " + opChoice)
            # Choice logic
            if playerChoice == opChoice:
                print("It's a tie")
                ties += 1
            elif playerChoice == "Scissors":
                if opChoice == "Rock":
                    print("Computer wins")
                    cpuwin += 1
                else:
                    print("You win")
                    playerwin += 1
            elif playerChoice == "Rock":
                if opChoice == "Paper":
                    print("Computer wins")
                    cpuwin += 1
                else:
                    print("You win")
                    playerwin += 1
            elif playerChoice == "Paper":
                if opChoice == "Scissors":
                    print("Computer wins")
                    cpuwin += 1
                else:
                    print("You win")
                    playerwin += 1
            else:
                print("An error occurred. ¯\_(ツ)_/¯  ")

        else:
            print("Please enter a valid input.")


# Initialise program
mainloop()
