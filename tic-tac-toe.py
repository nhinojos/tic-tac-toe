from tkinter import N
import numpy as np
import random


##Intial variables
#Game board.
move_record=np.full((3,3),' ')
#Allowed moves, including a new function.
def permissibleMoves():
	move_options=[]
	options=np.where(move_record==' ')
	for i in range(len(options[0])):
		move_options.append([options[0][i],options[1][i]])
	return move_options
move_options=permissibleMoves()



##Secondary functions for the Tic-Tac-Toe game. 
#Displays the board given a list of moves. 
def boardDisplay():
	print("   A|B|C")
	print("   —————")
	#Row construction
	for i in range(3):
		row=[str(i+1),'|',' ',' ','|',' ','|',' ']
		for j in range(3):
			row[3+2*j]=move_record[i,j]
		print(''.join(row))
	return



#Ensures a user's response is valid. If not, ask again. 
def validResponse(prompt,valid_answers):
	valid=False
	while valid==False:
		answer=str(input(prompt)).lower()
		if answer in valid_answers:
			valid=True
		else:
			print("That is not a valid repsonse.")
	return answer



#Determines if the game is Won. Returns True if so, False otherwise.  
def gameWon():
	x_o=['x','o']
	for t in x_o:
		for n in range(3):
			#Row win
			if all(move==t for move in move_record[n]):
				return True
			#Column win
			if all(move==t for move in move_record[:,n]):
				return True
		#Diagonal win
		if all(move==t for move in np.diag(move_record)) or all(move==t for move in np.diag(np.flipud(move_record))):
			return True
	return False




#Bots change to game board.
	#Easy Bot (0) chooses random option to play.
	#Medium Bot (1) passively prevents loss. Otherwise, Medium Bot also chooses randomly.
	#Hard Bot (2) passively prevents loss AND will win when opportunity is readily available.
	#Impossible Bot (3) uses the ultimate strategy to ultimately win and never lose. 


##Primary Game Function
def ticTacToe():
	
	#Intialization
	print("Welcome to Tic-Tac-Toe!")
	print("")

	#Tutorial for program
	tutorial=validResponse('Would you like a tutorial on how to use this program? (y/n)',{'y','yes','n','no'})
	if tutorial in {'y','yes'}:
		print("")
		print('This program simulates the classic game Tic-Tac-Toe')
		print('Below is a visual display of starting game board')
		boardDisplay()
		print("You can make moves based on column labels ABC and row labels 123")
		print("For example, the center position would be labeled B2")
		print()
	print("Let's Begin.")


	##Pre-game quesitons.
	#Asks for difficulty, converts to number
		#Easy Bot chooses random option to play.
		#Medium Bot passively prevents loss. Otherwise, Medium Bot also chooses randomly.
		#Hard Bot passively prevents loss AND will win when opportunity is readily available.
		#Impossible Bot uses the ultimate strategy to ultimately win and never lose. 
	difficulty=validResponse("Which difficulty would you prefer? (easy/medium/hard/impossible)",['easy','medium','hard','impossible'])
	#Asks user if they would like to go first.
	user_first=validResponse("Would you like to go first? (y/n)",['y','n'])
	if user_first=='y':
		turn=0
		user_first=True
	else:
		turn=1
		user_first=False
	
	#Esablish piece type for each player
	user_type=validResponse("Which piece would you like to be? (x/o)",['x','o'])
	if user_type=='o':
		bot_type='x'
	else:
		bot_type='o'
	print("Here is the initial game board:")
	boardDisplay()

	##Begin Game
	game_won=False
	while game_won==False:
		#Player's Turn
		if turn%2==0:
			#Player's Decision
			print("User's Turn!")
			print('turn ==',turn)
			#Determining allowed moves.
			move_options=permissibleMoves()
			#Converting to alphanumerical format and appending to list.
			alph=['a','b','c']
			options_alphnum=[]
			for pos in move_options:
				options_alphnum.append(str(alph[pos[1]])+str(pos[0]+1))
			#Printing allowed moves for user.
			print("You can make the following moves:")
			options_string=''
			for m in sorted(options_alphnum):
				options_string+=m+' '
			print(options_string)
			print("")
			#Committing user's decision to game board.
			choice=validResponse("Where would you like to move?",options_alphnum)
			move=move_options[options_alphnum.index(choice)]
			move_record[move[0],move[1]]=user_type
			boardDisplay()

		#Bot's Turn
		else:
			print(difficulty.capitalize()+" Bot's turn!")
			print('turn ==',turn)
			print("Calculating...")
			#3-way sequence strategization
			strategized=False
			if difficulty in ['medium','hard','impossible']:
				#Iterates through different versions of move_record.
				sequence_list=[move_record,np.transpose(move_record),[np.diag(move_record)],[np.diag(np.flipud(move_record))]]
			
				#Impossible Bot
				#Employs the perfect strategy to never lose, and maybe even win!
				if difficulty=='impossible':
					#User goes first
					if user_first==True and turn>0:
						#Bot's first move
						if turn==1:
							#Prefer your move to be in the center,B2
							if move_record[1,1]!=user_type:
								move_record[1,1]=bot_type
							#If not, bottom right corner, C3
							else:
								move_record[2,2]=bot_type
							strategized=True
						#Bot's second move
						elif turn==3:
							#If bot in center.
							if move_record[1,1]==bot_type:
								#If user in opposing diagonols, place piece on upper middle, B1
								if (move_record[0,2]==user_type and move_record[2,0]==user_type) or (move_record[0,0]==user_type and move_record[2,2]==user_type):
									move_record[0,1]=bot_type
									strategized=True
								else:
									#If user in 2 sides, place piece in corner connecting to sides, preventing win. 
									for i in range(2):
										if move_record[i,i+1]==move_record[i+1,i] and move_record[i,i+1]==user_type:
											move_record[2*i,2*i]=bot_type
											strategized=True
										elif move_record[i,1-i]==move_record[i+1,2-i] and move_record[i,1-i]==user_type:
											move_record[2*i,2-2*i]=bot_type
											strategized=True
							#if user along diagnols and bot is on corner, for player movement. 
							else:
								if move_record[0,0]==move_record[1,1]:
									move_record[1,2]==bot_type
									strategized=True
							#No more strategic moves to make
							difficulty='hard'


					##Bot goes first
					if user_first==False:
						#Bot's first corner, the bottom right, C3
						if turn==1:
							move_record[2,2]=bot_type
							strategized=True
						#Bot's second  corner
						elif turn==3:
							#If user in middle, B2, place piece on opposing corner, A1.
							if move_record[1,1]==user_type:
								move_record[0,0]=bot_type
								strategized=True
							#Otherwise, place piece in nearby corner.
							#Pick the corner such that the user is at a disadvatnage
							else:
								#Bottom left corner, A3
								for i in ([0,0],[1,0],[0,2],[1,2]):
									if move_record[i[0],i[1]]==user_type:
										move_record[2,0]=bot_type 
										strategized=True
										break
								#upper right corner, C1
								if strategized==False:
									move_record[0,2]=bot_type 
									strategized=True
						#Bot's third and final move
						elif turn==5:
							#If user at center, B2
							if move_record[1,1]==user_type:
								#If user at upper right, C1; or at lower left, A3.
								#Then, place piece on opposing corner
								#Win Gauranteed
								for i in [[0,2],[2,0]]:
									if move_record[i[0],i[1]]==user_type:
										move_record[i[1],i[0]]==bot_type
										strategized=True
										break
									#Otherwise, Tie Game as strategized is kept at False
							#Center is empty, hence the user is at disadvantage from before.
							#Win gauranteed
							else:
								if move_record[2,0]==bot_type:
									move_record[0,2]=bot_type
								else:
									move_record[2,0]=bot_type
								strategized=True
							#No more strategic moves to make
							difficulty="hard"


				
				#Hard Bot 
				#Secures win in any 3-way sequence.
				if (difficulty in ['hard','impossible']) and strategized==False:
					for s,sequence in enumerate(sequence_list):
						for i,seq3 in enumerate(sequence):
							#Checks if there is an empty spot in 3 element sequence
							seq3_empty=np.where(seq3==' ')
							if len(seq3_empty[0])==1:
								#Checks if there are two bot_type pieces in 3 element sequence
								seq3_bot=np.where(seq3==bot_type)
								#Will prevent loss or secure win. 
								if len(seq3_bot[0])==2:
									strategized=True
									#Sequence is original move_record; For row analysis.
									if s==0:
										move_record[i,seq3_empty[0]]=bot_type
									#Sequence is transposed move_record; For column analysis.
									elif s==1:
										move_record[seq3_empty[0],i]=bot_type
									#Sequence is a diagonol of move_record; For diagonal analysis.
									elif s==2:
										move_record[seq3_empty[0],seq3_empty[0]]=bot_type
									elif s==3:
										move_record[2-seq3_empty[0],seq3_empty[0]]=bot_type

				#Hard & Medium Bot
				#Prevent loss in any 3-way sequence.
				if strategized==False:
					for s,sequence in enumerate(sequence_list):
						for i,seq3 in enumerate(sequence):
							#Checks if there is an empty spot in 3 element sequence
							seq3_empty=np.where(seq3==' ')
							if len(seq3_empty[0])==1:
								#Checks if there are two other user_type pieces in 3 element sequence
								seq3_user=np.where(seq3==user_type)
								#Will prevent loss or secure win. 
								if len(seq3_user[0])==2:
									strategized=True
									#Sequence is original move_record; For row analysis.
									if s==0:
										move_record[i,seq3_empty[0]]=bot_type
									#Sequence is transposed move_record; For column analysis.
									elif s==1:
										move_record[seq3_empty[0],i]=bot_type
									#Sequence is a diagonol of move_record; For diagonal analysis.
									elif s==2:
										move_record[seq3_empty[0],seq3_empty[0]]=bot_type
									elif s==3:
										move_record[2-seq3_empty[0],seq3_empty[0]]=bot_type
			#All Bots
			#Randomly selects valid space
			if strategized==False:
				print('Random selection!')
				move_options=permissibleMoves()
				choice=random.choice(move_options)
				move_record[choice[0],choice[1]]=bot_type
			
			#Next turn, values edited and board is displayed
			boardDisplay()
			print("")
		turn+=1
		
		#Checks if game is won
		if turn>4:
			game_won=gameWon()
		#Breaks on an even match
		if (turn==9 and user_first==True) or (turn==10 and user_first==False):
			break

	#Game over. 
	if game_won==True:
		print("")
		print("The Game is Now Complete.")
		if turn%2==1:
			print('The User Wins!')
		else:
			print('The Bot Wins!')
	else:
		print("Tie Game!")
		return

###TESTING###
#print("****TEST INITIALIZING****")
#move_record=np.array([['x',' ','o'],['x','x','o'],['o','o','x']])
#boardDisplay()
#print(gameWon())
#print("****TEST COMPLETE****")
ticTacToe()









