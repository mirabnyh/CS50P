from random import randint
import sys

def main():
    l = get_level()
    x = randint(1,l)
    while True:
        try:
            guess = int(input("Guess: "))
            if guess < x:
                print("Too small!")
            elif guess > x:
                print("Too large!")
            else:
                sys.exit("Just right!")
        except ValueError:
            pass
        
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level <= 0:
                continue
            return level
        except ValueError:
            pass

main()
