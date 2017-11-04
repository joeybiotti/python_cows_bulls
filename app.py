import random 

def compare_nums(nums, user_guess):
    cowbull = [0,0]
    for i in range(len(nums)):
        if num[i] == user_guess[i]:
            cowbull[1]+=1
        else:
            cowbull[0]+=1
    return cowbull

if __name__ == "__main__":
    playing = True
    player = str(random.randint(0,9999))
    guesses = 0

    print("Wanna play a game... of cowbull?!")
    print("A random number will be generated")
    print("For every number guessed in the wrong place, you get a cow. If you get it in the right place, you get a bull.")
    print("The game ends when you get four bulls.")
    print("Easy, right?")
    print("Type 'exit' at any prompt to exit the game")

    while playing:
        user_guess = input("Guess a number: ")
        if user_guess == "exit": 
            break #user quit game 
        cowbullcount = compare_nums(nums, user_guess)
        guesses += 1

        print("You have "+ str(cowbullcount[0] + " cows, and " + str(cowbullcount[1])+ " bulls."))

        if cowbullcount[1] == 4:
            playing = False
            print("You've won. This time.")
            break #game ends. user won. 
        else:
            print("WRONG. Guess again.")

