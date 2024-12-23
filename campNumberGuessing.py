import random

def main():
    randoNumer = random.randint(1,100)
    userGuess = int(input("Guess a random number from 1-100:"))

    if (randoNumer == userGuess):
        print("You won")

    else:
        print("You lost")
        print(randoNumer)

    
if (__name__=="__main__"):
    main()
         