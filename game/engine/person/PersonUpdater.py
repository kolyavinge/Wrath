class PersonUpdater:

    def commitZState(self, gameState):
        for person in gameState.allPerson:
            person.prevZState = person.zState

    def commitZStateForBots(self, gameState):
        for bot in gameState.bots:
            bot.prevZState = bot.zState

    def updateDelaysForPlayer(self, gameState):
        gameState.player.paralyzeDelay.decrease()

    def updateDelaysForBots(self, gameState):
        for bot in gameState.bots:
            bot.paralyzeDelay.decrease()
