# Created by Samiyanur Islam
# All rights reserved to Samiyanur Islam
# October 2020

import random
def main():
	# Welcomes the user to the game
	input("Welcome to Rock, Paper, Scissors! Press Enter to start.")
	print()
	again()
	print()


def fun():  # regular outline for RPS
	computermove = random.randint(1, 3)
	playermove = int(
		input("What is your move: Type (1 for rock/2 for paper/3 for scissors):"))
	print("The computer chose", computermove)
	if computermove == playermove:
		print("It's a Tie!")
	elif playermove == 1 and computermove == 3:
		print("Player wins!")
	elif playermove == 1 and computermove == 2:
		print("Computer wins!")
	elif playermove == 2 and computermove == 1:
		print("Player wins!")
	elif playermove == 2 and computermove == 3:
		print("Computer wins!")
	elif playermove == 3 and computermove == 2:
		print("Player wins!")
	elif playermove == 3 and computermove == 1:
		print("Computer wins!")
	print()
	x = repeat()  # asks to play again


def easy():  # function that allows player to win everytime.
	computermove = random.randint(1, 3)
	playermove = int(
		input("What is your move: Type (1 for rock/2 for paper/3 for scissors):"))
	print("The computer chose", computermove)
	if playermove == 1:
		computermove = 3
		print("Player wins!")
	elif playermove == 2:
		computermove = 1
		print("Player wins!")
	elif playermove == 3:
		computermove = 2
		print("Player wins!")
	elif playermove == computermove:
		print("Its a tie.")
	else:
		print("Player wins.")
	print()
	x = repeat()  # asks to play again


def difficult():  # mode 2 which is difficult and takes makes it impossible for the player to win
	computermove = random.randint(1, 3)
	playermove = int(
		input("What is your move: Type (1 for rock/2 for paper/3 for scissors):"))
	print("The computer chose", computermove)
	if playermove == computermove:
		print("Its a tie.")
	elif playermove == 1:
		computermove = 2
		print("Computer wins!")
	elif playermove == 2:
		computermove = 3
		print("Computer wins!")
	elif playermove == 3:
		computermove = 1
		print("Computer wins!")
	else:
		print("Player wins.")
	print()
	x = repeat()  # asks to play again


def mirror():  # mode 3 which is mirror, intakes what the player used last move and playes it for next round
	# asks for how many rounds since the value of 1st round is needed for mirror
	rounds = int(input("How many rounds do you want to play? "))
	oldmove = random.randint(1, 3)
	for i in range(rounds):
		playermove = int(
			input("What is your move: Type (1 for rock/2 for paper/3 for scissors):"))
		computermove = oldmove
		print("The computer chose", computermove)
		if rounds == 0:
			fun()
			return playermove
		if rounds > 1:
			if playermove == computermove:
				print("Its a tie.")
			elif computermove == 1 and playermove != 2:
				computermove == playermove
				print("Computer wins!")
			elif computermove == 2 and playermove != 3:
				computermove == playermove
				print("Computer wins!")
			elif computermove == 3 and playermove != 1:
				computermove == playermove
				print("Computer wins!")
			else:
				print("Player wins!")
		oldmove = playermove
	rounds += 1
	print()
	x = repeat()  # asks to play again


def again():  # funtion that asks what mode the user wants to play
	# asks user what mode to play
	i = str(input("Type the mode you would like to play(fun/easy/difficult/mirror): "))
	#implements the mode accordingly to what user chose to play
	if i == "easy":
		easy()
	elif i == "difficult":
		difficult()
	elif i == "fun":
		fun()
	elif i == "mirror":
		mirror()
	return i  # returns the value of i


def repeat():     # function that asks the user whether they want to play again
	playrpsagain = str(input('Do you want to play again? Type Yes or No: '))
	if playrpsagain.lower() == 'yes':
		again()  # implements the again function
	elif playrpsagain.lower() == 'no':
		print('Goodbye!')
		return ""  # exits the system
	else:
		print('Invalid Command.')


main()
