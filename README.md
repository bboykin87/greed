# Greed

Discord implementation of the dice game


## Rules

Play begins by the first player rolling all five dice, attempting to score 350 or more on their initial roll to “come in” to the game. If a score of 350 or more isn’t achieved in the player’s turn, they score no points for that turn. Once a player has scored their initial “come in” of 350 points, they add all points accumulated on subsequent turns to their score, even if they score less than 350 points in a turn.

If a player does not roll a scoring combination on their turn, their turn is over and play continues clockwise. If a player rolls a scoring combination, they can elect to take that score and add it to their running total, or they can get greedy and reroll to attempt gaining a higher score.


## Scoring

* Each 1	100
* Each 5	50
* Three 1s	1000
* Three 2s	200
* Three 3s	300
* Three 4s	400
* Three 5s	500
* Three 6s	600

* A straight (1–2–3–4–5) is scored as 1000
