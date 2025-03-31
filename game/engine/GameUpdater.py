import time

from game.engine.ai.EnemyAILogic import EnemyAILogic
from game.engine.BackgroundVisibilityDetector import BackgroundVisibilityDetector
from game.engine.BulletPositionUpdater import BulletPositionUpdater
from game.engine.BulletTraceUpdater import BulletTraceUpdater
from game.engine.BulletUpdater import BulletUpdater
from game.engine.CameraUpdater import CameraUpdater
from game.engine.cm.BulletCollisionProcessor import BulletCollisionProcessor
from game.engine.cm.PersonCollisionProcessor import PersonCollisionProcessor
from game.engine.cm.PersonWallCollisionProcessor import PersonWallCollisionProcessor
from game.engine.cm.PowerupCollisionProcessor import PowerupCollisionProcessor
from game.engine.EnemyLevelSegmentsUpdater import EnemyLevelSegmentsUpdater
from game.engine.LevelSegmentVisibilityUpdater import LevelSegmentVisibilityUpdater
from game.engine.PersonDoStepLogic import PersonDoStepLogic
from game.engine.PersonMovingTimeCalculator import PersonMovingTimeCalculator
from game.engine.PersonPositionUpdater import PersonPositionUpdater
from game.engine.PersonTurnLogic import PersonTurnLogic
from game.engine.PersonVelocityCalculator import PersonVelocityCalculator
from game.engine.PersonZUpdater import PersonZUpdater
from game.engine.PlayerLevelSegmentsUpdater import PlayerLevelSegmentsUpdater
from game.engine.PlayerMovingSwingLogic import PlayerMovingSwingLogic
from game.engine.PlayerWeaponPositionSwingLogic import PlayerWeaponPositionSwingLogic
from game.engine.PlayerWeaponPositionUpdater import PlayerWeaponPositionUpdater
from game.engine.PowerupUpdater import PowerupUpdater
from game.engine.TorchUpdater import TorchUpdater
from game.engine.WeaponDelayUpdater import WeaponDelayUpdater
from game.engine.WeaponFireLogic import WeaponFireLogic
from game.engine.WeaponFlashUpdater import WeaponFlashUpdater
from game.engine.WeaponSelector import WeaponSelector


class GameUpdater:

    def __init__(
        self,
        personTurnLogic,
        personMovingTimeCalculator,
        personVelocityCalculator,
        personZUpdater,
        personWallCollisionProcessor,
        personCollisionProcessor,
        personDoStepLogic,
        playerLevelSegmentsUpdater,
        enemyLevelSegmentsUpdater,
        playerMovingSwingLogic,
        backgroundVisibilityDetector,
        personPositionUpdater,
        levelSegmentVisibilityUpdater,
        cameraUpdater,
        playerWeaponPositionUpdater,
        weaponDelayUpdater,
        weaponFireLogic,
        playerWeaponPositionSwingLogic,
        bulletUpdater,
        bulletPositionUpdater,
        bulletCollisionProcessor,
        powerupCollisionProcessor,
        torchUpdater,
        powerupUpdater,
        weaponFlashUpdater,
        bulletTraceUpdater,
        enemyAILogic,
        # event listeners
        weaponSelector,
    ):
        self.personTurnLogic = personTurnLogic
        self.personMovingTimeCalculator = personMovingTimeCalculator
        self.personVelocityCalculator = personVelocityCalculator
        self.personZUpdater = personZUpdater
        self.personWallCollisionProcessor = personWallCollisionProcessor
        self.personCollisionProcessor = personCollisionProcessor
        self.personDoStepLogic = personDoStepLogic
        self.playerLevelSegmentsUpdater = playerLevelSegmentsUpdater
        self.enemyLevelSegmentsUpdater = enemyLevelSegmentsUpdater
        self.playerMovingSwingLogic = playerMovingSwingLogic
        self.backgroundVisibilityDetector = backgroundVisibilityDetector
        self.personPositionUpdater = personPositionUpdater
        self.levelSegmentVisibilityUpdater = levelSegmentVisibilityUpdater
        self.cameraUpdater = cameraUpdater
        self.playerWeaponPositionUpdater = playerWeaponPositionUpdater
        self.weaponDelayUpdater = weaponDelayUpdater
        self.weaponFireLogic = weaponFireLogic
        self.playerWeaponPositionSwingLogic = playerWeaponPositionSwingLogic
        self.bulletUpdater = bulletUpdater
        self.bulletPositionUpdater = bulletPositionUpdater
        self.bulletCollisionProcessor = bulletCollisionProcessor
        self.powerupCollisionProcessor = powerupCollisionProcessor
        self.torchUpdater = torchUpdater
        self.powerupUpdater = powerupUpdater
        self.weaponFlashUpdater = weaponFlashUpdater
        self.bulletTraceUpdater = bulletTraceUpdater
        self.enemyAILogic = enemyAILogic

    def update(self):
        # start = time.time()

        self.personTurnLogic.process()
        self.personMovingTimeCalculator.calculate()
        self.personVelocityCalculator.calculate()
        self.personPositionUpdater.moveNextPosition()
        self.personWallCollisionProcessor.process()
        self.personCollisionProcessor.process()
        self.personZUpdater.updateIfMoved()
        self.personDoStepLogic.updateDoStep()
        self.playerLevelSegmentsUpdater.updateIfMoved()
        self.enemyLevelSegmentsUpdater.updateIfMoved()
        self.levelSegmentVisibilityUpdater.updateIfPlayerMovedOrTurned()
        self.personPositionUpdater.commitNextPosition()
        self.playerMovingSwingLogic.updateSwing()
        self.cameraUpdater.update()
        self.backgroundVisibilityDetector.updateIfPlayerMovedOrTurned()
        self.playerWeaponPositionUpdater.update()
        self.weaponDelayUpdater.update()
        self.weaponFireLogic.process()
        self.playerWeaponPositionSwingLogic.updateSwing()
        self.bulletUpdater.update()
        self.bulletPositionUpdater.moveNextPosition()
        self.bulletCollisionProcessor.process()
        self.bulletPositionUpdater.commitNextPosition()
        self.powerupCollisionProcessor.process()
        self.torchUpdater.update()
        self.powerupUpdater.update()
        self.powerupUpdater.generateNew()
        self.weaponFlashUpdater.update()
        self.bulletTraceUpdater.update()
        self.enemyAILogic.apply()
        self.personPositionUpdater.resetMovedAndTurned()
        self.personPositionUpdater.commitPersonState()

        # end = time.time()
        # print(f"Game updated {end-start:.8f}")


def makeGameUpdater(resolver):
    return GameUpdater(
        resolver.resolve(PersonTurnLogic),
        resolver.resolve(PersonMovingTimeCalculator),
        resolver.resolve(PersonVelocityCalculator),
        resolver.resolve(PersonZUpdater),
        resolver.resolve(PersonWallCollisionProcessor),
        resolver.resolve(PersonCollisionProcessor),
        resolver.resolve(PersonDoStepLogic),
        resolver.resolve(PlayerLevelSegmentsUpdater),
        resolver.resolve(EnemyLevelSegmentsUpdater),
        resolver.resolve(PlayerMovingSwingLogic),
        resolver.resolve(BackgroundVisibilityDetector),
        resolver.resolve(PersonPositionUpdater),
        resolver.resolve(LevelSegmentVisibilityUpdater),
        resolver.resolve(CameraUpdater),
        resolver.resolve(PlayerWeaponPositionUpdater),
        resolver.resolve(WeaponDelayUpdater),
        resolver.resolve(WeaponFireLogic),
        resolver.resolve(PlayerWeaponPositionSwingLogic),
        resolver.resolve(BulletUpdater),
        resolver.resolve(BulletPositionUpdater),
        resolver.resolve(BulletCollisionProcessor),
        resolver.resolve(PowerupCollisionProcessor),
        resolver.resolve(TorchUpdater),
        resolver.resolve(PowerupUpdater),
        resolver.resolve(WeaponFlashUpdater),
        resolver.resolve(BulletTraceUpdater),
        resolver.resolve(EnemyAILogic),
        resolver.resolve(WeaponSelector),
    )
