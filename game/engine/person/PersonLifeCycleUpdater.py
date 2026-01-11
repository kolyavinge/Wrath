from game.engine.GameState import GameState
from game.model.person.PersonStates import LifeCycle


class PersonLifeCycleUpdater:

    def __init__(self, gameState: GameState):
        self.gameState = gameState

    def update(self):
        for person in self.gameState.allPerson:
            self.updatePerson(person)

    def updatePerson(self, person):
        if person.lifeCycle == LifeCycle.alive:
            if person.health == 0:
                person.lifeCycle = LifeCycle.dead
                person.lifeCycleDelay.set(50)
        else:
            person.lifeCycleDelay.decrease()
            if person.lifeCycleDelay.isExpired():
                if person.lifeCycle == LifeCycle.dead:
                    person.lifeCycle = LifeCycle.respawn
                elif person.lifeCycle == LifeCycle.respawn:
                    person.lifeCycle = LifeCycle.respawnDelay
                    person.lifeCycleDelay.set(50)
                elif person.lifeCycle == LifeCycle.respawnDelay:
                    person.lifeCycle = LifeCycle.alive
