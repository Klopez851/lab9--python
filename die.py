import random

class Die:
    # sets up the attributes of the class
    def __init__(self):
        self.value = 0

    # sets and gets the value of self.value
    def Roll(self):
        self.value = random.randint(1, 6)
        return self.value