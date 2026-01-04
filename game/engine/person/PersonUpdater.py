from game.engine.GameState import GameState


class PersonUpdater:

    def __init__(self, gameState: GameState):
        self.gameState = gameState

    def commitZState(self):
        for person in self.gameState.allPerson:
            person.prevZState = person.zState

    def updateDelays(self):
        for person in self.gameState.allPerson:
            person.paralyzeDelay.decrease()
