import random


#Guess the Number (computer) 

def guess_user(x):
	random_number = random.randint(1,x)
	guess = 0
	while guess != random_number:
		guess = int(input(f'Guess a Number between 0 and {x}:'))
		if guess < random_number:
			print("Sorry! Guess Again. It is too Low")
		elif guess > random_number:
			print("Sorry! Guess Again. It is too High")
	print(f"Yeah,Correct:={random_number}")


#Guess the Number (user)

def guess_computer(x):
	low = 1
	high = x
	feedback = ''
	while feedback != 'c':
		if low != high:
			guess = random.randint(low,high)
		else:
			guess = low
		feedback = input(f'Is {guess} too high(H),too low(L) or Correct').lower()
		if feedback == 'h':
			high = guess-1
		elif feedback == 'l':
			low = guess+1
	print(f'Yah,The Computer Guess Your Number{guess},Correctly')
guess_computer(1000)