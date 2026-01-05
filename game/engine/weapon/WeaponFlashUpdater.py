from game.engine.GameState import GameState


class WeaponFlashUpdater:

    def __init__(self, gameState: GameState):
        self.gameState = gameState

    def update(self):
        for levelSegment in self.gameState.visibilityTree.allLevelSegments:
            for flash in levelSegment.weaponFlashes:
                flash.update()
                if not flash.isVisible:
                    levelSegment.weaponFlashes.remove(flash)
