from game.model.person.PersonStates import PersonZState


class PersonJumpUpdater:

    def updateForPlayer(self, gameState):
        self.updateForPerson(gameState.player, gameState.playerInputData, gameState.updateStatistic)

    def updateForBots(self, gameState):
        for bot, inputData in gameState.botInputData.items():
            self.updateForPerson(bot, inputData, gameState.updateStatistic)

    def updateForPerson(self, person, inputData, updateStatistic):
        isJumpAvailable = inputData.jump and (person.zState == PersonZState.onFloor or person.zState == PersonZState.jumping)

        if not isJumpAvailable:
            person.jumpingTime = 0
            person.jumpingValue = 0
            return

        if person.jumpingTime <= 1.0:
            person.jumpingTime += 0.1
            if person.jumpingTime == 0.5:
                updateStatistic.jumpedPerson.append(person)
        else:
            person.jumpingTime = 0

        person.jumpingValue = person.jumpingFunc.getValue(person.jumpingTime)
