from game.engine.GameData import GameData


class PersonUpdater:

    def __init__(self, gameData: GameData):
        self.gameData = gameData

    def commitZState(self):
        for person in self.gameData.allPerson:
            person.prevZState = person.zState

    def updateDelays(self):
        for person in self.gameData.allPerson:
            person.selectWeaponDelay.decrease()
