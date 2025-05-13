from game.engine.GameData import GameData


class PersonUpdater:

    def __init__(self, gameData: GameData):
        self.gameData = gameData

    def commitState(self):
        for person in self.gameData.allPerson:
            person.prevState = person.state

    def resetWounded(self):
        self.gameData.woundedPerson.clear()
        for person in self.gameData.allPerson:
            person.isWounded = False
