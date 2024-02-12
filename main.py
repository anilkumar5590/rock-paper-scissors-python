import random as rd
#Randomly Select one chocie for computerValue
Choices=["ROCK","PAPER","SCISSORS"]

#Winner Calculation Funciton
def winner(userValue):
    computerValue=rd.choice(Choices)
    #It's a Tie Case
    if userValue==computerValue:
        print("User Selected "+userValue+" and Computer Selected "+computerValue+": It's A Tie ")
        return 0
    #User Wins Case
    elif((userValue=="ROCK" and computerValue=="SCISSORS") or (userValue=="PAPER" and computerValue=="ROCK") or (userValue=="SCISSORS" and computerValue=="PAPER")):
        print("User Selected "+userValue+" and Computer Selected "+computerValue+": User Wins ")
        return 1
    #Computer Wins Case
    elif((computerValue=="ROCK" and userValue=="SCISSORS") or (computerValue=="PAPER" and userValue=="ROCK") or (computerValue=="SCISSORS" and userValue=="PAPER")):
        print("User Selected "+userValue+" and Computer Selected "+computerValue+": Computer Wins ")
        return 2

 #main funciton   
if __name__=="__main__":
    playerScore,computerScore=0,0
    print("\t\t\t"+"*"*40)
    print("\t\t\t\tROCK  PAPER  SCISSORS")
    print("\t\t\t"+"*"*40)

    totalWins=int(input("Enter Maximum No. of Wins Size: "))
    while(totalWins<=0):
        print("Enter Another Value which is not less than 1: ")
        totalWins=int(input("Enter Maximum No. of Wins Size: "))
    #Loop runs until any one of the score is n
    while(playerScore!=totalWins and computerScore!=totalWins):
        userSelect=input("Enter User Choice(Rock,Paper,Scissors,exit)-> ")
        #USer Selects Rock
        if(userSelect[0]=='R' or userSelect[0]=='r'):
            result=winner("ROCK")
            if(result==0):
                print("Player Score :",playerScore," Vs Computer Score :",computerScore)
            elif(result==1):
                playerScore+=1
                print("Player Score :",playerScore," Vs Computer Score :",computerScore)
            else:
                computerScore+=1
                print("Player Score :",playerScore," Vs Computer Score :",computerScore)
        #User Selsects Paper
        elif(userSelect[0]=='P' or userSelect[0]=='p'):
            result=winner("PAPER")
            if(result==0):
                print("Player Score :",playerScore," Vs Computer Score :",computerScore)
            elif(result==1):
                playerScore+=1
                print("Player Score :",playerScore," Vs Computer Score :",computerScore)
            else:
                computerScore+=1
                print("Player Score :",playerScore," Vs Computer Score :",computerScore)
        #User Selects Scissors
        elif(userSelect[0]=='S' or userSelect[0]=='s'):
            result=winner("SCISSORS")
            if(result==0):
                print("Player Score :",playerScore," Vs Computer Score :",computerScore)
            elif(result==1):
                playerScore+=1
                print("Player Score :",playerScore," Vs Computer Score :",computerScore)
            else:
                computerScore+=1
                print("Player Score :",playerScore," Vs Computer Score :",computerScore)
        #User Selects Exit
        elif(userSelect[0]=='E' or userSelect[0]=='e'):
            break

