from game.engine.GameState import GameState


class PersonBreathUpdater:

    def __init__(self, gameData: GameState):
        self.gameData = gameData

    def update(self):
        for person in self.gameData.allPerson:
            if not person.hasMoved and not self.gameData.allPersonItems[person].currentWeapon.isFiring:
                person.breathTime += 1.0
            else:
                person.breathTime = 0
