import random


class Die(object):
    """[summary]

    Args:
        object ([type]): [description]
    """

    def __init__(self):
        self.diceA = 1
        self.diceB = 1
        self.diceC = 1
        self.diceD = 1
        self.diceE = 1

    def roll(self):
        try:
            rState = random.getstate()
            _dice = [self.diceA, self.diceB, self.diceC, self.diceD, self.diceE]
            print(len(_dice))
            for count, _ in enumerate(_dice):
                print(count)
                rResult = random.randint(1,6)
                _dice[count] = rResult
            random.setstate(rState)
        except Exception as e:
            print(e)
        finally:
            print(_dice)

    def hold(self, holdDice):
        A = 0
        B = 1
        C = 2
        D = 3
        E = 4
        _dice = [self.diceA, self.diceB, self.diceC, self.diceD, self.diceE]
        sDice = []
        try:
            for count, _ in enumerate(holdDice):
                sDice.append(_dice[_])
        except Exception as e:
            pass
        
                

die = Die()
die.roll()

