from game.engine.CameraUpdater import CameraUpdater
from game.engine.cm.PlayerWallCollisionProcessor import PlayerWallCollisionProcessor
from game.engine.LevelSegmentVisibilityUpdater import LevelSegmentVisibilityUpdater
from game.engine.PlayerLevelSegmentsUpdater import PlayerLevelSegmentsUpdater
from game.engine.PlayerMoveLogic import PlayerMoveLogic
from game.engine.PlayerPositionUpdater import PlayerPositionUpdater
from game.engine.PlayerTurnLogic import PlayerTurnLogic
from game.engine.PlayerZUpdater import PlayerZUpdater


class GameUpdater:

    def __init__(
        self,
        playerMoveLogic,
        playerTurnLogic,
        playerZUpdater,
        playerWallCollisionProcessor,
        playerLevelSegmentsUpdater,
        playerPositionUpdater,
        levelSegmentVisibilityUpdater,
        cameraUpdater,
    ):
        self.playerMoveLogic = playerMoveLogic
        self.playerTurnLogic = playerTurnLogic
        self.playerZUpdater = playerZUpdater
        self.playerWallCollisionProcessor = playerWallCollisionProcessor
        self.playerLevelSegmentsUpdater = playerLevelSegmentsUpdater
        self.playerPositionUpdater = playerPositionUpdater
        self.levelSegmentVisibilityUpdater = levelSegmentVisibilityUpdater
        self.cameraUpdater = cameraUpdater

    def update(self):
        self.playerMoveLogic.process()
        self.playerTurnLogic.process()
        self.playerWallCollisionProcessor.processCollisions()
        self.playerZUpdater.updateIfPlayerMoved()
        self.playerLevelSegmentsUpdater.updateIfPlayerMoved()
        self.cameraUpdater.update()
        self.levelSegmentVisibilityUpdater.updateIfPlayerMovedOrTurned()
        self.playerPositionUpdater.update()


def makeGameUpdater(resolver):
    return GameUpdater(
        resolver.resolve(PlayerMoveLogic),
        resolver.resolve(PlayerTurnLogic),
        resolver.resolve(PlayerZUpdater),
        resolver.resolve(PlayerWallCollisionProcessor),
        resolver.resolve(PlayerLevelSegmentsUpdater),
        resolver.resolve(PlayerPositionUpdater),
        resolver.resolve(LevelSegmentVisibilityUpdater),
        resolver.resolve(CameraUpdater),
    )
