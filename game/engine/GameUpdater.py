import time

from game.engine.CameraUpdater import CameraUpdater
from game.engine.cm.PlayerWallCollisionDetector import PlayerWallCollisionDetector
from game.engine.cm.PlayerWallCollisionProcessor import PlayerWallCollisionProcessor
from game.engine.LevelSegmentVisibilityUpdater import LevelSegmentVisibilityUpdater
from game.engine.PersonDoStepLogic import PersonDoStepLogic
from game.engine.PlayerLevelSegmentsUpdater import PlayerLevelSegmentsUpdater
from game.engine.PlayerMoveLogic import PlayerMoveLogic
from game.engine.PlayerMovingSwingLogic import PlayerMovingSwingLogic
from game.engine.PlayerMovingTimeCalculator import PlayerMovingTimeCalculator
from game.engine.PlayerPositionUpdater import PlayerPositionUpdater
from game.engine.PlayerTurnLogic import PlayerTurnLogic
from game.engine.PlayerVelocityCalculator import PlayerVelocityCalculator
from game.engine.PlayerWeaponPositionUpdater import PlayerWeaponPositionUpdater
from game.engine.PlayerZUpdater import PlayerZUpdater
from game.engine.TorchSwitcher import TorchSwitcher


class GameUpdater:

    def __init__(
        self,
        playerTurnLogic,
        playerMovingTimeCalculator,
        playerVelocityCalculator,
        playerMoveLogic,
        playerZUpdater,
        playerWallCollisionDetector,
        playerWallCollisionProcessor,
        personDoStepLogic,
        playerLevelSegmentsUpdater,
        playerMovingSwingLogic,
        playerPositionUpdater,
        levelSegmentVisibilityUpdater,
        cameraUpdater,
        playerWeaponPositionUpdater,
        torchSwitcher,
    ):
        self.playerTurnLogic = playerTurnLogic
        self.playerMovingTimeCalculator = playerMovingTimeCalculator
        self.playerVelocityCalculator = playerVelocityCalculator
        self.playerMoveLogic = playerMoveLogic
        self.playerZUpdater = playerZUpdater
        self.playerWallCollisionDetector = playerWallCollisionDetector
        self.playerWallCollisionProcessor = playerWallCollisionProcessor
        self.personDoStepLogic = personDoStepLogic
        self.playerLevelSegmentsUpdater = playerLevelSegmentsUpdater
        self.playerMovingSwingLogic = playerMovingSwingLogic
        self.playerPositionUpdater = playerPositionUpdater
        self.levelSegmentVisibilityUpdater = levelSegmentVisibilityUpdater
        self.cameraUpdater = cameraUpdater
        self.playerWeaponPositionUpdater = playerWeaponPositionUpdater
        self.torchSwitcher = torchSwitcher

    def update(self):
        # start = time.time()

        self.playerTurnLogic.process()
        self.playerMovingTimeCalculator.calculate()
        self.playerVelocityCalculator.calculate()
        self.playerMoveLogic.process()
        self.playerWallCollisionDetector.detectCollisions()
        self.playerWallCollisionProcessor.processCollisions()
        self.playerZUpdater.updateIfPlayerMoved()
        self.personDoStepLogic.updateDoStep()
        self.playerLevelSegmentsUpdater.updateIfPlayerMoved()
        self.levelSegmentVisibilityUpdater.updateIfPlayerMovedOrTurned()
        self.playerPositionUpdater.update()
        self.playerMovingSwingLogic.updateSwing()
        self.cameraUpdater.update()
        self.playerWeaponPositionUpdater.update()
        self.torchSwitcher.update()

        # end = time.time()
        # print(f"Game updated {end-start:.8f}")


def makeGameUpdater(resolver):
    return GameUpdater(
        resolver.resolve(PlayerTurnLogic),
        resolver.resolve(PlayerMovingTimeCalculator),
        resolver.resolve(PlayerVelocityCalculator),
        resolver.resolve(PlayerMoveLogic),
        resolver.resolve(PlayerZUpdater),
        resolver.resolve(PlayerWallCollisionDetector),
        resolver.resolve(PlayerWallCollisionProcessor),
        resolver.resolve(PersonDoStepLogic),
        resolver.resolve(PlayerLevelSegmentsUpdater),
        resolver.resolve(PlayerMovingSwingLogic),
        resolver.resolve(PlayerPositionUpdater),
        resolver.resolve(LevelSegmentVisibilityUpdater),
        resolver.resolve(CameraUpdater),
        resolver.resolve(PlayerWeaponPositionUpdater),
        resolver.resolve(TorchSwitcher),
    )
