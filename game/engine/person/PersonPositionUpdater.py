class PersonPositionUpdater:

    def movePlayerNextPosition(self, gameState):
        self.movePersonNextPosition(gameState.player)

    def moveBotsNextPosition(self, gameState):
        for bot in gameState.bots:
            self.movePersonNextPosition(bot)

    def movePersonNextPosition(self, person):
        if person.velocityValue > 0:
            person.moveNextPositionBy(person.velocityVector)

    def commitPlayerNextPosition(self, gameState):
        gameState.player.commitNextPosition()

    def commitBotsNextPosition(self, gameState):
        for bot in gameState.bots:
            bot.commitNextPosition()
