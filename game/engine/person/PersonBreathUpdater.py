from game.engine.GameData import GameData


class PersonBreathUpdater:

    def __init__(self, gameData: GameData):
        self.gameData = gameData

    def update(self):
        for person in self.gameData.allPerson:
            if not person.hasMoved and not self.gameData.allPersonItems[person].currentWeapon.isFiring:
                person.breathTime += 1.0
            else:
                person.breathTime = 0
