from game.anx.PersonConstants import PersonConstants
from game.model.level.Stair import Stair
from game.model.person.PersonStates import PersonZState


class PersonStepUpdater:

    def update(self, gameState):
        for person, personItems in gameState.allPersonItems.items():
            self.updateForPerson(person, personItems, gameState.updateStatistic)

    def updateForPerson(self, person, personItems, updateStatistic):
        doStep = False
        if person.zState == PersonZState.onFloor:
            person.stepTime += 1.0 * personItems.currentWeapon.slowdownCoeff
            if isinstance(person.nextFloor, Stair):
                doStep = person.currentCenterPoint.z != person.nextCenterPoint.z
            else:
                doStep = person.stepTime > PersonConstants.stepTimeLimit

        if doStep:
            person.stepTime = 0
            updateStatistic.stepedPerson.append(person)
