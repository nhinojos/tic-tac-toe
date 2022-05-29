# Tic-Tac-Toe
### Goal
To recreate the classic game of Tic-Tac-Toe.

### Criteria
- Includes a tutorial.
- User plays against an automated opponent with ranging in difficulties. The easiest opponent randomly guesses while the hardest should be impossible to beat.
- The user has agency over piece type, who goes first, optional pre-game tutorial, and bot difficulty.

### Method & Results
I created tic-tac-toe through mere functional programming instead of object-oriented. NumPy arrays acted as a framework to manipulate x's and o's in a 3x3 matrix. As for difficulty, there are four tiers: 'easy' is a random guessing bot with no strategy, 'medium' is the same as 'easy' yet it will prevent loss where obvious, 'hard' is the same as 'medium' yet it will secure win where obvious, and 'impossible' which is the same as 'hard' yet it makes strategically optimum choices within the first couple turns to ensure it will never lose, and even likely win. As you may guess, each bot inherits the properties of the previous bot and then some. Hence, the code of each bot is not necessarilly unique nor individualized. 
