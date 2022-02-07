# Tic-Tac-Toe
### Goal
To recreate Tic-Tac-Toe in Python.

### Criteria
- Include tutorial
- Automated opponent, ranging in difficulties. Easiest should be a bot who randomly guesses, which hardest should be impossible to beat
- User agency over piece type, who goes first, optional pre-game tutorial, and bot difficulty.

### Method & Results
I created the tic-tac-toe game through mere functional programming instead of OOP. NumPy arrays acted as a frameowkr to manipulate x's and o's in a 3x3 matrix. As for difficulty, there are four tiers: 'easy' is a random guessing bot with no strategy, 'medium' is the same as 'easy' yet it will prevent loss where obvious, 'hard' is the same as 'medium' yet it will secure win where obvious, and 'impossible' which is the same as 'hard' yet it makes strategically optimumchoices within the first couple turns to ensure it will never lose, and even likely win. As you may guess, each bot inherits the properties of the previous bot and then some. Hence, the code of each bot is not necessarilly unique or individualized. 

All bots are fully constructed and no errors have been observed. Yet, further testing may be needed to ensure this program contains zero errors. 
