import time

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
        playerTurnLogic,
        playerMovingTimeCalculator,
        playerVelocityCalculator,
        playerMoveLogic,
        playerZUpdater,
        playerWallCollisionProcessor,
        playerLevelSegmentsUpdater,
        playerPositionUpdater,
        levelSegmentVisibilityUpdater,
        cameraUpdater,
        cameraSwingLogic,
    ):
        self.playerTurnLogic = playerTurnLogic
        self.playerMovingTimeCalculator = playerMovingTimeCalculator
        self.playerVelocityCalculator = playerVelocityCalculator
        self.playerMoveLogic = playerMoveLogic
        self.playerZUpdater = playerZUpdater
        self.playerWallCollisionProcessor = playerWallCollisionProcessor
        self.playerLevelSegmentsUpdater = playerLevelSegmentsUpdater
        self.playerPositionUpdater = playerPositionUpdater
        self.levelSegmentVisibilityUpdater = levelSegmentVisibilityUpdater
        self.cameraUpdater = cameraUpdater
        self.cameraSwingLogic = cameraSwingLogic

    def update(self):
        start = time.time()

        self.playerTurnLogic.process()
        self.playerMovingTimeCalculator.calculate()
        self.playerVelocityCalculator.calculate()
        self.playerMoveLogic.process()
        self.playerWallCollisionProcessor.processCollisions()
        self.playerZUpdater.updateIfPlayerMoved()
        self.playerLevelSegmentsUpdater.updateIfPlayerMoved()
        self.cameraUpdater.updatePositionIfPlayerMoved()
        self.cameraSwingLogic.updateSwing()
        self.cameraUpdater.calculateViewMatrixIfPlayerMoved()
        self.levelSegmentVisibilityUpdater.updateIfPlayerMovedOrTurned()
        self.playerPositionUpdater.update()

        end = time.time()
        # print(f"Game updated {end-start:.8f}")


def makeGameUpdater(resolver):
    return GameUpdater(
        resolver.resolve(PlayerTurnLogic),
        resolver.resolve(PlayerMovingTimeCalculator),
        resolver.resolve(PlayerVelocityCalculator),
        resolver.resolve(PlayerMoveLogic),
        resolver.resolve(PlayerZUpdater),
        resolver.resolve(PlayerWallCollisionProcessor),
        resolver.resolve(PlayerLevelSegmentsUpdater),
        resolver.resolve(PlayerPositionUpdater),
        resolver.resolve(LevelSegmentVisibilityUpdater),
        resolver.resolve(CameraUpdater),
        resolver.resolve(CameraSwingLogic),
    )
