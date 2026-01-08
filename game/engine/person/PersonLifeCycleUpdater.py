from game.anx.PersonConstants import PersonConstants
from game.engine.GameState import GameState
from game.model.person.PersonStates import LifeCycle


class PersonLifeCycleUpdater:

    def __init__(self, gameState: GameState):
        self.gameState = gameState

    def update(self):
        for person in self.gameState.allPerson:
            self.processPerson(person)

    def processPerson(self, person):
        if person.lifeCycle == LifeCycle.alive:
            if person.health == 0:
                person.lifeCycle = LifeCycle.dead
                person.lifeCycleDelay.set(50)
        else:
            person.lifeCycleDelay.decrease()
            if person.lifeCycleDelay.isExpired():
                if person.lifeCycle == LifeCycle.dead:
                    person.lifeCycle = LifeCycle.respawnDelay
                    person.lifeCycleDelay.set(200)
                elif person.lifeCycle == LifeCycle.respawnDelay:
                    person.lifeCycle = LifeCycle.respawn
                    person.lifeCycleDelay.set(50)
                    person.addHealth(PersonConstants.maxPersonHealth)
                    self.gameState.respawnRequests.append(person)
                elif person.lifeCycle == LifeCycle.respawn:
                    person.lifeCycle = LifeCycle.alive
