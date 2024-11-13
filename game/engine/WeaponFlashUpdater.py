from game.engine.GameData import GameData


class WeaponFlashUpdater:

    def __init__(self, gameData):
        self.gameData = gameData

    def init(self):
        self.allVisibilityLevelSegments = self.gameData.level.visibilityTree.getAllLevelSegments()

    def update(self):
        for levelSegment in self.allVisibilityLevelSegments:
            for flash in levelSegment.weaponFlashes:
                flash.update()
                if not flash.isVisible:
                    levelSegment.weaponFlashes.remove(flash)


def makeWeaponFlashUpdater(resolver):
    return WeaponFlashUpdater(resolver.resolve(GameData))
