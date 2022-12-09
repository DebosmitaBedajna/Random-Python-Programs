import random

chosen=random.randint(1,100)
Guess=0
Game={}
Players=[]
while(1):
    print("Welcome to the random number choosing game.Let's see who wins!")
    number=int(input("Enter the number of players: "))
    while number!=0:
        name=input("Enter the name of Player: ")
        Players.append(name)
        number=number-1
    for i in Players:
        Game.update({i:1})
    print("Let's begin!")
    trial=0
    while(trial!=chosen):
        for i in Players:
            trial=int(input("{}'s guess: ".format(i)))
            if trial==chosen:
                print("Congratulations! {} won in {} number of guesses!".format(i,Guess+1))
                break
            else:
                Game.update({i:Guess})
        Guess=Guess+1
    break