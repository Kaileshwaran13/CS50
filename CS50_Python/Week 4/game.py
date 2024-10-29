import random

def findGuess(levelAns):

    guess = input("Guess: ")
    if(guess.isdigit()):
        if(int(guess) < levelAns):
            print("Too Small!")
            findGuess(levelAns)
        elif(int(guess) > levelAns):
            print("Too Large!")
            findGuess(levelAns)
        else:
            print("Just Right!")
    else:
        findGuess(levelAns)

def playGame(level):
    levelAns = random.randint(1,level)
    findGuess(levelAns)


def inputData():
    level = input("Level: ")
    if(level.isdigit() and int(level) > 0):
        playGame(int(level))
    else:
        inputData()
inputData()