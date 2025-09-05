from game.model.ai.AIData import AIData
from game.model.person.Person import Person
from game.model.person.PersonStates import LifeCycle


class Enemy(Person):

    def __init__(self):
        super().__init__()
        self.isVisibleForPlayer = False
        self.currentCenterPointLevelSegment = None
        self.aiData = AIData()

    def getAlphaForLifeCycle(self):
        if self.lifeCycle == LifeCycle.alive:
            return 1.0
        if self.lifeCycle == LifeCycle.dead:
            return self.lifeCycleDelay.value / self.lifeCycleDelay.initValue
        if self.lifeCycle == LifeCycle.respawnDelay:
            return 0.0
        if self.lifeCycle == LifeCycle.respawn:
            return 1.0 - self.lifeCycleDelay.value / self.lifeCycleDelay.initValue

        raise Exception("Wrong LifeCycle value.")
