#A program that simulates n games of raquetball to check whuich player has higher wins.
from random import*
def simNGames(n,probA,probB):
        winsA=winsB=0
        for i in range(n):
            serving="A"
            scoreA=0
            scoreB=0
            while scoreA!=15 and scoreB!=15:
                if serving=="A":
                    if random()<probA:
                        scoreA+=1
                    else:    
                        serving="B"
                else:
                     if random()<probB:
                        scoreB+=1
                      
                     else:
                        serving="A"          
                
            if scoreA>scoreB:
                winsA+=1
                        
            else:
                winsB+=1
                   
        return winsA,winsB
print("This program simulates a game of racquetball between 2 players")
probA=eval(input("Enter the probability of player A that wins a serve: "))
probB=eval(input("Enter the probability of player B that wins a serve: "))
n=eval(input("Enter how many games to simulate: "))
winsA,winsB = simNGames(n,probA,probB)

print(n," games were simulated.")
print("wins for A: ",winsA,"the percentage is: ", round(winsA/n*100,2))
print("wins for B: ",winsB, "the percentage is: ",round( winsB/n*100,2))
    
