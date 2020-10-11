import random
deck_of_cards= [[],[],[],[]]
for j in range(4):
     for i in range(13):
         deck_of_cards[j].append(i+1)

playerCards=[int((random.random())*10+1),int((random.random())*10+1)]
cpuCards=[int((random.random())*10 +1),int((random.random())*10+1)]

print(str(playerCards) +"\n " )
print(str(cpuCards[0]) +" ?\n" )

playerScore = 0
for i in range(len(playerCards)):
    playerScore += playerCards[i]


move = None
while move != "stand" and playerScore<21:
    move= input("What do you want? ")
    if(move=="hit"):
        playerDraw = int((random.random())*10+1)
        playerCards.append(playerDraw)
        playerScore+=playerDraw
        print(str(playerCards) +"\n "+ str(playerScore))
print("END")
cpuScore = 0

print("\nPlayer\n"+ str(playerCards)+" Score: "+str(playerScore))

for i in range(len(cpuCards)):
    cpuScore += cpuCards[i]

while cpuScore <17:
    cpuDraw=int((random.random())*10+1)
    cpuCards.append(cpuDraw)
    cpuScore=cpuScore+cpuDraw

print("\nCPU\n"+ str(cpuCards)+" Score: "+str(cpuScore))

if((playerScore>21 and cpuScore>21) or playerScore==cpuScore):
    print("\nPush! No one wins!\n")
elif((playerScore>21 and cpuScore<21) or (playerScore<cpuScore and cpuScore<=21)):
    print("\nCPU Wins!\n")
elif((playerScore<21 and cpuScore>21) or (playerScore>cpuScore and playerScore<=21)):
    print("\nPlayer Wins!\n")

