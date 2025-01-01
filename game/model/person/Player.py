from game.anx.PersonConstants import PersonConstants
from game.calc.Vector3 import Vector3
from game.lib.Math import Math
from game.model.person.Person import Person


class Player(Person):

    maxPitchRadians = Math.piHalf - 0.1

    def __init__(self):
        super().__init__()
        self.eyePosition = Vector3()
        self.prevPrevSwingValue = 0
        self.prevSwingValue = 0
        self.currentSwingValue = 0

    def commitNextPosition(self):
        super().commitNextPosition()
        self.eyePosition = self.currentCenterPoint.copy()
        self.eyePosition.z += PersonConstants.eyeLength
