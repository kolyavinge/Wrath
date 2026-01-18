from game.model.person.PersonStates import LifeCycle


class PersonLifeCycleUpdater:

    def update(self, gameState):
        for person in gameState.allPerson:
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
