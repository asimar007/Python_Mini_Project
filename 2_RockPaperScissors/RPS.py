import random

def play():
	user = input("Whats your choice? 'r' for Rock 'p' for paper 's' for scissor")
	computer = random.choice(['r','p','s'])

	if user == computer:
		return 'It is a Tie'

	if isWin(user,computer):
		return 'You Won'

	return 'You Lost'

def isWin(player,oponent):
	if (player == 'r' and oponent == 's') or (player == 's' and oponent == 'r') or (player == 'p' and oponent == 'r' ):
		return True

print(play())