#!/usr/bin/env python3

import random
import time

rock = 1
paper = 2
scissors = 3
spock = 4
lizard = 5

names = { rock: "rock", paper: "paper", scissors: "scissors", spock: "spock", lizard: "lizard" }
rules = { rock: { lizard: "crushes", scissors: "smashes" },
            paper: { rock:"covers" , spock:"disproves" },
            scissors:{ paper:"cuts" , lizard:"decaptitates" },
            spock: { scissors:"smashes", rock:"vaporizes" },
            lizard:{ paper:"eats", spock:"poisons" }
        }

player_score = 0
computer_score = 0

def start_game():
    print("Let's play a game of Rock, Paper, Scissors.")
    while get_moves():
    	pass
    show_scores()
    
def get_moves():
	player = get_player_move()
	computer = random.randint(1, 5)
	run_comparison(player, computer)
	return play_again()
	
def get_player_move():
	while True:
		print 
		player = input("Rock = 1,\nPaper = 2\nScissors = 3\nSpock = 4\nLizard=5\nMake a move: ")
		try:
			player = int(player)
			if player in (1,2,3,4,5):
				return player
		except ValueError:
			pass
		print("Oops! I didn't understand that. Please enter 1,2,3,4 or 5")


def show_countdown(player, computer):
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1!")
    time.sleep(0.5)
    print("You threw {}".format(names[player]))
    print("Computer threw {}".format(names[computer]))
    print()

def run_comparison(player, computer):
    show_countdown(player, computer)
    global player_score, computer_score
    if player == computer:
        print("It's a tie")
    else:
        if computer in rules[player]:
            print("You win! {} {} {}".format(names[player], rules[player].get(computer), names[computer]))
            player_score += 1
        else:
            print("You lose! {} {} {}".format(names[computer], rules[computer].get(player), names[player]))
            computer_score += 1

def play_again():
	answer = input("Would you like to play again? y/n: ")
	if answer in ("y", "yes"):
		return answer
	else:
		print("Goodbye")

def show_scores():
	global player_score, computer_score
	print("High Scores")
	print("Player: ", player_score)
	print("Computer: ", computer_score)
	
if __name__ == '__main__':
	start_game()
	
	
	
	
	
	
	

