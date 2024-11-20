import time

from game.engine.BulletMoveLogic import BulletMoveLogic
from game.engine.CameraUpdater import CameraUpdater
from game.engine.cm.BulletCollisionProcessor import BulletCollisionProcessor
from game.engine.cm.PlayerWallCollisionDetector import PlayerWallCollisionDetector
from game.engine.cm.PlayerWallCollisionProcessor import PlayerWallCollisionProcessor
from game.engine.cm.PowerupCollisionProcessor import PowerupCollisionProcessor
from game.engine.LevelSegmentVisibilityUpdater import LevelSegmentVisibilityUpdater
from game.engine.PersonDoStepLogic import PersonDoStepLogic
from game.engine.PlayerLevelSegmentsUpdater import PlayerLevelSegmentsUpdater
from game.engine.PlayerMoveLogic import PlayerMoveLogic
from game.engine.PlayerMovingSwingLogic import PlayerMovingSwingLogic
from game.engine.PlayerMovingTimeCalculator import PlayerMovingTimeCalculator
from game.engine.PlayerPositionUpdater import PlayerPositionUpdater
from game.engine.PlayerTurnLogic import PlayerTurnLogic
from game.engine.PlayerVelocityCalculator import PlayerVelocityCalculator
from game.engine.PlayerWeaponPositionSwingLogic import PlayerWeaponPositionSwingLogic
from game.engine.PlayerWeaponPositionUpdater import PlayerWeaponPositionUpdater
from game.engine.PlayerZUpdater import PlayerZUpdater
from game.engine.PowerupUpdater import PowerupUpdater
from game.engine.TorchUpdater import TorchUpdater
from game.engine.WeaponDelayUpdater import WeaponDelayUpdater
from game.engine.WeaponFireLogic import WeaponFireLogic
from game.engine.WeaponFlashUpdater import WeaponFlashUpdater
from game.engine.WeaponSelector import WeaponSelector


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
        weaponDelayUpdater,
        weaponFireLogic,
        playerWeaponPositionSwingLogic,
        bulletMoveLogic,
        bulletCollisionProcessor,
        powerupCollisionProcessor,
        torchUpdater,
        powerupUpdater,
        weaponFlashUpdater,
        # event listeners
        weaponSelector,
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
        self.weaponDelayUpdater = weaponDelayUpdater
        self.weaponFireLogic = weaponFireLogic
        self.playerWeaponPositionSwingLogic = playerWeaponPositionSwingLogic
        self.bulletMoveLogic = bulletMoveLogic
        self.bulletCollisionProcessor = bulletCollisionProcessor
        self.powerupCollisionProcessor = powerupCollisionProcessor
        self.torchUpdater = torchUpdater
        self.powerupUpdater = powerupUpdater
        self.weaponFlashUpdater = weaponFlashUpdater

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
        self.weaponDelayUpdater.update()
        self.weaponFireLogic.process()
        self.playerWeaponPositionSwingLogic.updateSwing()
        self.bulletMoveLogic.process()
        self.bulletCollisionProcessor.process()
        self.powerupCollisionProcessor.process()
        self.torchUpdater.update()
        self.powerupUpdater.update()
        self.powerupUpdater.generateNew()
        self.weaponFlashUpdater.update()

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
        resolver.resolve(WeaponDelayUpdater),
        resolver.resolve(WeaponFireLogic),
        resolver.resolve(PlayerWeaponPositionSwingLogic),
        resolver.resolve(BulletMoveLogic),
        resolver.resolve(BulletCollisionProcessor),
        resolver.resolve(PowerupCollisionProcessor),
        resolver.resolve(TorchUpdater),
        resolver.resolve(PowerupUpdater),
        resolver.resolve(WeaponFlashUpdater),
        resolver.resolve(WeaponSelector),
    )
