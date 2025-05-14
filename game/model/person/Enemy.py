from game.model.ai.AIData import AIData
from game.model.person.Person import Person


class Enemy(Person):

    def __init__(self):
        super().__init__()
        self.currentCenterPointLevelSegment = None
        self.aiData = AIData()
