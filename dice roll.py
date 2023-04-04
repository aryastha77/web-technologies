def dice():
    import random
    roll1=random.randint(1,6)
    roll2=random.randint(1,6)
    total=roll1+roll2
    guess=0
    num_win=0
    num_round=0
    while True:
        num_round+=1
        guess=int(input("enter the total sum of two dices:"))
        if guess== total:
            print(" Cingrats! you have won")
        elif guess>total:
            print("Guess is too high")
        elif guess < total:
            print("guess is too low")
        else:
            print("you lost the game")
        Try_again=input("Do u want to try again?(yes/no)")
        if Try_again=="no":
            print("Over")
            break
    if num_round>0:
        num_win=(num_win/num_round)*100
    print(" you have playes", num_round,"times")
    print("win percentage",num_win)
dice()
