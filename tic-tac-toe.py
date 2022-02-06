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



#Determines if the game is complete. Returns True if so, False otherwise.  
def gameComplete():
	x_o=['x','o']
	for t in x_o:
		for n in range(3):
			#Row win
			if all(move==t for move in move_record[n]):
				return True,t
			#Column win
			if all(move==t for move in move_record[:,n]):
				return True,t
		#Diagonal win
		if all(move==t for move in np.diag(move_record)) or all(move==t for move in np.diag(np.flipud(move_record))):
			return True,t
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
	tutorial=validResponse('Would you like a tutorial on how to use this program?',{'y','yes','n','no'})
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
	else:
		turn=1
	#Esablish piece type for each player
	user_type=validResponse("Which piece would you like to be? (x/o)",['x','o'])
	if user_type=='o':
		bot_type='x'
	else:
		bot_type='o'


	##Begin Game
	game_complete=False
	while game_complete==False:
		#Player's Turn
		if turn%2==0:
			#Player's Decision
			print("User's Turn!")
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

		#Bot's Turn
		else:
			print(difficulty.capitalize()+" Bot's turn!")
			print("Calculating...")
			#3-way sequence strategization
			strategized=False
			if difficulty in ['medium','hard']:
				#Iterates through different versions of move_record.
				sequence_list=[move_record,np.transpose(move_record),[np.diag(move_record)],[np.diag(np.flipud(move_record))]]
				#Secures win in any 3-way sequence.
				if difficulty=='hard':
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
			
			#Randomly selects valid space
			if strategized==False:
				move_options=permissibleMoves()
				choice=random.choice(move_options)
				move_record[choice[0],choice[1]]=bot_type
		turn+=1

		#Displays Game Board. 
		print("Here is the current state of the board:")
		boardDisplay()
		#Checks if game is complete
		if turn>4:
			game_complete=gameComplete(move_record)








