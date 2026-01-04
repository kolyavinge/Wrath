from game.engine.GameState import GameState


class PersonBreathUpdater:

    def __init__(self, gameState: GameState):
        self.gameState = gameState

    def update(self):
        for person in self.gameState.allPerson:
            if not person.hasMoved and not self.gameState.allPersonItems[person].currentWeapon.isFiring:
                person.breathTime += 1.0
            else:
                person.breathTime = 0
