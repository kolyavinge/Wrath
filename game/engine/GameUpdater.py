from game.engine.CameraUpdater import CameraUpdater
from game.engine.cm.PlayerWallCollisionProcessor import PlayerWallCollisionProcessor
from game.engine.LevelSegmentVisibilityUpdater import LevelSegmentVisibilityUpdater
from game.engine.PlayerLevelSegmentsUpdater import PlayerLevelSegmentsUpdater
from game.engine.PlayerPositionUpdater import PlayerPositionUpdater
from game.engine.PlayerZUpdater import PlayerZUpdater


class GameUpdater:

    def __init__(
        self,
        playerZUpdater,
        playerWallCollisionProcessor,
        playerLevelSegmentsUpdater,
        playerPositionUpdater,
        levelSegmentVisibilityUpdater,
        cameraUpdater,
    ):
        self.playerZUpdater = playerZUpdater
        self.playerWallCollisionProcessor = playerWallCollisionProcessor
        self.playerLevelSegmentsUpdater = playerLevelSegmentsUpdater
        self.playerPositionUpdater = playerPositionUpdater
        self.levelSegmentVisibilityUpdater = levelSegmentVisibilityUpdater
        self.cameraUpdater = cameraUpdater

    def update(self):
        self.playerZUpdater.update()
        self.playerWallCollisionProcessor.processCollisions()
        if self.playerWallCollisionProcessor.hasCollisions:
            self.playerZUpdater.update()
        self.playerLevelSegmentsUpdater.update()
        self.playerPositionUpdater.update()
        self.cameraUpdater.update()
        self.levelSegmentVisibilityUpdater.update()


def makeGameUpdater(resolver):
    return GameUpdater(
        resolver.resolve(PlayerZUpdater),
        resolver.resolve(PlayerWallCollisionProcessor),
        resolver.resolve(PlayerLevelSegmentsUpdater),
        resolver.resolve(PlayerPositionUpdater),
        resolver.resolve(LevelSegmentVisibilityUpdater),
        resolver.resolve(CameraUpdater),
    )
