import numpy as np
import random

for i in range(2):
	print("")

##Initial Variable
move_type=np.array([['a1','a2','a3'],['b1','b2','b3'],['c1','c2','c3']])
move_record=np.full((3,3),' ')


##Secondary functions for the Tic-Tac-Toe game. 
#Displays the board given a list of moves. 
def boardDisplay(move_record):
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
def gameComplete(move_record):
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

#Defines list of permissible moves in Row x Column format
def permissibleMoves(move_record):
	options=np.where(move_record==' ')
	move_options=[]
	for i in range(len(options[0])):
		move_options.append([options[0][i],options[1][i]])
	return move_options
	

#Bot's change to game board.
def botDecision(move_record,bot_type,difficulty):
	#List of valid move options 
	move_options=permissibleMoves(move_record)
	#Easy Bot (0) chooses random option to play.
	#Medium Bot (1) passively prevents loss. Otherwise, Medium Bot also chooses randomly.
	#Hard Bot (2) passively prevents loss AND will win when opportunity is readily available.
	#Impossible Bot (3) uses the ultimate strategy to ultimately win and never lose. 
	if difficulty in [0,1]:
		#Medium Bot Prevents Loss
		if difficulty==1:
			#List of seqences for the below for-loop to iterate through
			sequence_list=[move_record,np.transpose(move_record),[np.diag(move_record)],[np.diag(np.flipud(move_record))]]
			#Determines user piece type
			if bot_type=='x':
				user_type='o'
			else:
				user_type='x'
			#Prevent loss in  any three-way sequence
				#ERROR Iterator i changes depending on the sequence, perhaps create another enumerator?
				#Or, mark where the move should be made...
			for sequence in sequence_list:
				for i,seq3 in enumerate(sequence):
					seq3_empty=np.where(seq3==' ')
					if len(seq3_empty[0])!=0:
						seq3_user=np.where(seq3==user_type)
						if len(seq3_user[0])==2:
							print("LOSS PREVENTED")
							print("sequence:")
							print(sequence)
							print("seq3:",seq3)
							#Second index may need to utilize seq3_empty
							move_record[i,[0]]=bot_type
							return move_record
		
		#Randomly selects valid space
		choice=random.choice(move_options)
		move_record[choice[0],choice[1]]=bot_type
		return move_record


#User's change to game board.
def userDecision(move_record,user_type):
	#Determining allowed moves.
	move_options=permissibleMoves(move_record)
	
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
	return move_record



####TESTING
move_made1=np.array([['x',' ','x'],[' ',' ',' '],['x',' ','o']])
boardDisplay(move_made1)
print("")
userDecision(move_made1,'x')
boardDisplay(move_made1)


##Primary Game Function
def ticTacToe():
	#Intiallization
	made_moves=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
	print("Welcome to Tic-Tac-Toe!")
	print("")

	#Asks if user would like a tutorial.
	tutorial=validResponse('Would you like a tutorial?',{'y','yes','n','no'})
	if tutorial in {'y','yes'}:
		print("You can make moves based on column labels ABC and row labels 123")
		print("For example, the center position would be labeled B2")
		print("Here is an example of what the board will look like:")
		print("")
		boardDisplay(made_moves)
	print("Let's Begin.")

	#Asks user which piece they would prefer.
	user_type=validResponse("Which piece would you like to be?(x/o)",{'x','o'})
	if user_type=='x':
		bot_type='o'
	else:
		bot_type='x'

	#Asks user if they would like to go first.
	user_first=validResponse("Would you like to go first?(y/n)",{'y','n'})


	#Game start.
	game_complete=False
	n=0
	while game_complete==False:
		if n==0 and user_first=='y':
			return








