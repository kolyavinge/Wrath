from game.engine.GameState import GameState


class PersonUpdater:

    def __init__(self, gameData: GameState):
        self.gameData = gameData

    def commitZState(self):
        for person in self.gameData.allPerson:
            person.prevZState = person.zState

    def updateDelays(self):
        for person in self.gameData.allPerson:
            person.paralyzeDelay.decrease()
