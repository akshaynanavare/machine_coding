
import random

class Dice:
    def __init__(self,no_of_dice) -> None:
        self.Dice = no_of_dice

    def getDiceNumber(self):
        return random.randint(self.Dice, 6*self.Dice)
        