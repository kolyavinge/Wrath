from game.engine.LevelSegmentVisibilityUpdater import LevelSegmentVisibilityUpdater
from game.engine.PlayerPositionUpdater import PlayerPositionUpdater
from game.engine.CameraUpdater import CameraUpdater


class GameUpdater:

    def __init__(self, playerPositionUpdater, levelSegmentVisibilityUpdater, cameraUpdater):
        self.playerPositionUpdater = playerPositionUpdater
        self.levelSegmentVisibilityUpdater = levelSegmentVisibilityUpdater
        self.cameraUpdater = cameraUpdater

    def update(self):
        self.playerPositionUpdater.update()
        self.cameraUpdater.update()
        self.levelSegmentVisibilityUpdater.update()


def makeGameUpdater(resolver):
    return GameUpdater(resolver.resolve(PlayerPositionUpdater), resolver.resolve(LevelSegmentVisibilityUpdater), resolver.resolve(CameraUpdater))
