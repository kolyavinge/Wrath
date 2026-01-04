from game.engine.GameState import GameState


class WeaponFlashUpdater:

    def __init__(self, gameData: GameState):
        self.gameData = gameData

    def init(self):
        self.allVisibilityLevelSegments = self.gameData.visibilityTree.getAllLevelSegments()

    def update(self):
        for levelSegment in self.allVisibilityLevelSegments:
            for flash in levelSegment.weaponFlashes:
                flash.update()
                if not flash.isVisible:
                    levelSegment.weaponFlashes.remove(flash)
