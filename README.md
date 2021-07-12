# Greed

Discord implementation of the dice game


## Rules

Play begins by the first player rolling all five dice, attempting to score 350 or more on their initial roll to “come in” to the game. If a score of 350 or more isn’t achieved in the player’s turn, they score no points for that turn. Once a player has scored their initial “come in” of 350 points, they add all points accumulated on subsequent turns to their score, even if they score less than 350 points in a turn.

If a player does not roll a scoring combination on their turn, their turn is over and play continues clockwise. If a player rolls a scoring combination, they can elect to take that score and add it to their running total, or they can get greedy and reroll to attempt gaining a higher score.


## Scoring

* 1=100 points
* 5=50 points
* 3 of a kind= 100 x the number on the dice (100 points for three 1’s, 500 points for three 5’s, etc.)
* 4 of a kind= 1000 points
* three pairs (can only be achieved on a single roll)= 1500 points.
* A straight with all six dice (can only be achieved on a single roll)= 2000 points.
* 5 of a kind= 2000 points.

