import numpy as np
import random

##Initial Variable
move_type=np.array([['a1','a2','a3'],['b1','b2','b3'],['c1','c2','c3']])
move_made=np.empty((3,3),dtype=str)



##Secondary functions for Tic-Tac-Toe
#Displays the board given a list of moves. 
def boardDisplay(move_made):
	print("   A|B|C")
	print("   —————")

	#Prints each row
	for i in range(3):
		row=[str(i+1),'|',' ',' ','|',' ','|',' ']
		for j in range(3):
			row[3+2*j]=move_made[i,j]
		print(''.join(row))
	return


#Ensures a user's response is valid. If not, ask again. 
def properResponse(prompt,valid_answers):
	answer=str(input(prompt)).lower()
	if answer not in valid_answers:
		print("That is not a valid repsonse.")
		properResponse(prompt,valid_answers)
	else:
		return answer



#Determines if the game is complete. Returns True if so, False otherwise.  
def gameComplete(move_made):
	x_o=['x','o']
	for t in x_o:
		for n in range(3):
			#Row win
			if all(move==t for move in move_made[n]):
				return True,t
			#Column win
			if all(move==t for move in move_made[:,n]):
				return True,t
		#Diagonal win
		if all(move==t for move in np.diag(move_made)) or all(move==t for move in np.diag(np.flipud(move_made))):
			return True,t
	return False



#The Decision a Bot Makes.
def botDecision(move_made,bot_type,difficulty):
	#List of valid move options 
	options=np.where(move_made==' ')
	move_options=[]
	for i in range(len(options[0])):
		move_options.append([options[0][i],options[1][i]])
	
	#Easy Bot (0) chooses random option to play
	#Medium Bot (1) passively prevents loss. Otherwise, Medium Bot also chooses randomly
	#****Hard Bot (2) passively prevents loss AND will win for_____
	if difficulty in [0,1]:
		#Medium Bot Prevents Loss
		if difficulty==1:
			#List of seqences for the below for-loop to iterate through
			sequence_list=[move_made,np.transpose(move_made),[np.diag(move_made)],[np.diag(np.flipud(move_made))]]
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
							move_made[i,options[0]]=bot_type
							return move_made
		
		#Randomly selects valid space
		choice=random.choice(move_options)
		move_made[choice[0],choice[1]]=bot_type
		return move_made


move_made1=np.array([['x',' ','x'],[' ',' ',' '],['x','o','o']])
print("**BEFORE**")
boardDisplay(move_made1)
print("")
print("**AFTER**")
botDecision(move_made1,'x',1)
boardDisplay(move_made1)

def userDecision(made_moves,user_type):
	#Determines every valid move that can be made. 
	options=[]
	for r,row in enumerate(made_moves):
		for c,move in enumerate(row):
			if move==' ':
				options.append([r,c])
	
	#Translates list of valid options to alpha-numerical format. 
	abc=['a','b','c']
	options_abc={}
	for o in options:
		print(abc[o[0]])
		options_abc.append(abc[o[0]]+str[o[1]])

	print(options_abc)
	choice=properResponse("What is your next move?",options_abc)





##Calls the game to begin
def ticTacToe():
	#Intiallization
	made_moves=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
	print("Welcome to Tic-Tac-Toe!")
	print("")


	#Asks if user would like a tutorial.
	tutorial=properResponse('Would you like a tutorial?',{'y','yes','n','no'})
	if tutorial in {'y','yes'}:
		print("You can make moves based on column labels ABC and row labels 123")
		print("For example, the center position would be labeled B2")
		print("Here is an example of what the board will look like:")
		print("")
		boardDisplay(made_moves)
	print("Let's Begin.")

	#Asks user which piece they would prefer.
	user_type=properResponse("Which piece would you like to be?(x/o)",{'x','o'})
	if user_type=='x':
		bot_type='o'
	else:
		bot_type='x'

	#Asks user if they would like to go first.
	user_first=properResponse("Would you like to go first?(y/n)",{'y','n'})


	#Game start.
	game_complete=False
	n=0
	while game_complete==False:
		if n==0 and user_first=='y':
			return








