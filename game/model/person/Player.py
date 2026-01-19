from game.lib.DecrementCounter import DecrementCounter
from game.model.person.AimState import DefaultAimState
from game.model.person.Person import Person


class Player(Person):

    def __init__(self):
        super().__init__()
        self.aimState = DefaultAimState()
        self.swingValue = 0
        self.noActionTime = 0
        self.cowboyRemain = DecrementCounter()
