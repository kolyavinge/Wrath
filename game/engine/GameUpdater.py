from game.engine.CameraSwingLogic import CameraSwingLogic
from game.engine.CameraUpdater import CameraUpdater
from game.engine.cm.PlayerWallCollisionProcessor import PlayerWallCollisionProcessor
from game.engine.LevelSegmentVisibilityUpdater import LevelSegmentVisibilityUpdater
from game.engine.PlayerLevelSegmentsUpdater import PlayerLevelSegmentsUpdater
from game.engine.PlayerMoveLogic import PlayerMoveLogic
from game.engine.PlayerMovingTimeCalculator import PlayerMovingTimeCalculator
from game.engine.PlayerPositionUpdater import PlayerPositionUpdater
from game.engine.PlayerTurnLogic import PlayerTurnLogic
from game.engine.PlayerVelocityCalculator import PlayerVelocityCalculator
from game.engine.PlayerZUpdater import PlayerZUpdater


class GameUpdater:

    def __init__(
        self,
        playerMovingTimeCalculator,
        playerVelocityCalculator,
        playerMoveLogic,
        playerTurnLogic,
        playerZUpdater,
        playerWallCollisionProcessor,
        playerLevelSegmentsUpdater,
        playerPositionUpdater,
        levelSegmentVisibilityUpdater,
        cameraUpdater,
        cameraSwingLogic,
    ):
        self.playerMovingTimeCalculator = playerMovingTimeCalculator
        self.playerVelocityCalculator = playerVelocityCalculator
        self.playerMoveLogic = playerMoveLogic
        self.playerTurnLogic = playerTurnLogic
        self.playerZUpdater = playerZUpdater
        self.playerWallCollisionProcessor = playerWallCollisionProcessor
        self.playerLevelSegmentsUpdater = playerLevelSegmentsUpdater
        self.playerPositionUpdater = playerPositionUpdater
        self.levelSegmentVisibilityUpdater = levelSegmentVisibilityUpdater
        self.cameraUpdater = cameraUpdater
        self.cameraSwingLogic = cameraSwingLogic

    def update(self):
        self.playerMovingTimeCalculator.calculate()
        self.playerVelocityCalculator.calculate()
        self.playerMoveLogic.process()
        self.playerTurnLogic.process()
        self.playerWallCollisionProcessor.processCollisions()
        self.playerZUpdater.updateIfPlayerMoved()
        self.playerLevelSegmentsUpdater.updateIfPlayerMoved()
        self.cameraUpdater.update()
        self.cameraSwingLogic.updateSwing()
        self.levelSegmentVisibilityUpdater.updateIfPlayerMovedOrTurned()
        self.playerPositionUpdater.update()


def makeGameUpdater(resolver):
    return GameUpdater(
        resolver.resolve(PlayerMovingTimeCalculator),
        resolver.resolve(PlayerVelocityCalculator),
        resolver.resolve(PlayerMoveLogic),
        resolver.resolve(PlayerTurnLogic),
        resolver.resolve(PlayerZUpdater),
        resolver.resolve(PlayerWallCollisionProcessor),
        resolver.resolve(PlayerLevelSegmentsUpdater),
        resolver.resolve(PlayerPositionUpdater),
        resolver.resolve(LevelSegmentVisibilityUpdater),
        resolver.resolve(CameraUpdater),
        resolver.resolve(CameraSwingLogic),
    )
