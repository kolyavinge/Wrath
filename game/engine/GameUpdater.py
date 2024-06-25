from game.engine.CameraUpdater import CameraUpdater
from game.engine.cm.PlayerWallCollisionProcessor import PlayerWallCollisionProcessor
from game.engine.LevelSegmentVisibilityUpdater import LevelSegmentVisibilityUpdater
from game.engine.PlayerLevelSegmentsUpdater import PlayerLevelSegmentsUpdater
from game.engine.PlayerPositionUpdater import PlayerPositionUpdater


class GameUpdater:

    def __init__(self, playerWallCollisionProcessor, playerLevelSegmentsUpdater, playerPositionUpdater, levelSegmentVisibilityUpdater, cameraUpdater):
        self.playerWallCollisionProcessor = playerWallCollisionProcessor
        self.playerLevelSegmentsUpdater = playerLevelSegmentsUpdater
        self.playerPositionUpdater = playerPositionUpdater
        self.levelSegmentVisibilityUpdater = levelSegmentVisibilityUpdater
        self.cameraUpdater = cameraUpdater

    def update(self):
        self.playerWallCollisionProcessor.processCollisions()
        self.playerLevelSegmentsUpdater.update()
        self.playerPositionUpdater.update()
        self.cameraUpdater.update()
        self.levelSegmentVisibilityUpdater.update()


def makeGameUpdater(resolver):
    return GameUpdater(
        resolver.resolve(PlayerWallCollisionProcessor),
        resolver.resolve(PlayerLevelSegmentsUpdater),
        resolver.resolve(PlayerPositionUpdater),
        resolver.resolve(LevelSegmentVisibilityUpdater),
        resolver.resolve(CameraUpdater),
    )
