from game.anx.PersonConstants import PersonConstants
from game.engine.GameData import GameData
from game.engine.person.PersonTurnLogic import PersonTurnLogic
from game.lib.Random import Random
from game.model.person.PersonStates import LifeCycle


class PersonLifeCycleUpdater:

    def __init__(
        self,
        gameData: GameData,
        personTurnLogic: PersonTurnLogic,
    ):
        self.gameData = gameData
        self.personTurnLogic = personTurnLogic

    def update(self):
        for person in self.gameData.allPerson:
            self.processPerson(person)

    def processPerson(self, person):
        if person.lifeCycle == LifeCycle.alive:
            if person.health == 0:
                person.lifeCycle = LifeCycle.dead
                person.lifeCycleDelay.set(100)
        else:
            person.lifeCycleDelay.decrease()
            if person.lifeCycleDelay.isExpired():
                if person.lifeCycle == LifeCycle.dead:
                    person.lifeCycle = LifeCycle.respawnDelay
                    person.lifeCycleDelay.set(500)
                elif person.lifeCycle == LifeCycle.respawnDelay:
                    person.lifeCycle = LifeCycle.respawn
                    person.lifeCycleDelay.set(100)
                    self.generateRespawnPosition(person)
                    person.addHealth(PersonConstants.maxPersonHealth)
                elif person.lifeCycle == LifeCycle.respawn:
                    person.lifeCycle = LifeCycle.alive

    def generateRespawnPosition(self, person):
        respawnArea = Random.getListItem(self.gameData.level.respawnAreas)
        position = respawnArea.getRandomPoint()
        person.moveNextPositionTo(position)
        self.personTurnLogic.orientToFrontNormal(person, respawnArea.frontNormal)
        person.hasMoved = True
        person.hasTurned = True
