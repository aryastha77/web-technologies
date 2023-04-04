def game():
    import random
    num = random.randint(1,20)
    print(" You have five guess to figure out what is the correct number")
    for guesses in range (1,6):
        guess=int(input(" Guess #" + str(guesses) + ":"))
        
        if guess<num:
            print(" You are thinking too low")
        elif guess>num:
            print(" you are thinking too high")
        else:
            print(f" Congratulations! You guessed the correct number {num}")
    if guess!=num:
        print("Sorry, your chances are finished. The number was",num)
game()
