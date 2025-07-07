import sys 
import random
from enum import Enum

class RPS(Enum):
     ROCK = 1
     PAPER = 2
     SCISSORS = 3

# print(RPS(2))     
# print(RPS.ROCK)     
# print(RPS['ROCK'])     
# print(RPS.PAPER.value)     

print("")

playerchoice= input("Enter........\n 1 for Rock \n 2 for Paper \n 3 for Scissors:\n\n")

# print(playerchoice)
# print(type(playerchoice))

Player= int(playerchoice)

if Player < 1 or Player > 3 :
     sys.exit("You Must Enter 1, 2,or 3")


computerchoice = random.choice("123")
computer = int(computerchoice)

print("")
print("You Choice " + str(RPS(Player)).replace('RPS.','') +".")
print("Python Choice " + str(RPS(computer)).replace('RPS.','') +".")
print("")

if Player == 1 and computer == 3:
    print("🥳🥳 You Win! 🎉🎆 ")
elif Player == 2 and computer == 1:  
     print("🥳🥳 You Win! 🎉🎆 ")
elif Player == 3 and computer == 2:   
      print("🥳🥳 You Win! 🎉🎆 ")    
elif Player == computer:
     print("😶😶 Tie Game, So Sad! 😵😵")  
else:
     print("🐍🐍🐍  Python Wins, Better Luck Next Time! 🐍🐍🐍")   
