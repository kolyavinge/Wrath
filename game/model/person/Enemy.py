from game.calc.Geometry import Geometry
from game.model.person.Person import Person


class AIData:

    def __init__(self):
        self.horizontalFieldViewRadians = Geometry.degreesToRadians(45.0)
        self.checkCollisionLength = 3.0
        self.checkCollisionDirectionsCount = 8
        self.checkCollisionRadianStep = self.horizontalFieldViewRadians / self.checkCollisionDirectionsCount


class Enemy(Person):

    def __init__(self):
        super().__init__()
        self.currentCenterPointLevelSegment = None
        self.aiData = AIData()
