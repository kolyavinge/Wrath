from game.engine.ai.EnemyAILogic import EnemyAILogic
from game.engine.BackgroundVisibilityUpdater import BackgroundVisibilityUpdater
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
from game.engine.NonStandardBulletMovingLogic import NonStandardBulletMovingLogic
from game.engine.PersonMovingTimeUpdater import PersonMovingTimeUpdater
from game.engine.PersonPositionUpdater import PersonPositionUpdater
from game.engine.PersonStepUpdater import PersonStepUpdater
from game.engine.PersonTurnUpdater import PersonTurnUpdater
from game.engine.PersonUpdater import PersonUpdater
from game.engine.PersonVelocityUpdater import PersonVelocityUpdater
from game.engine.PersonWeaponPositionUpdater import PersonWeaponPositionUpdater
from game.engine.PersonZUpdater import PersonZUpdater
from game.engine.PlayerLevelSegmentsUpdater import PlayerLevelSegmentsUpdater
from game.engine.PlayerMovingSwingUpdater import PlayerMovingSwingUpdater
from game.engine.PlayerWeaponSwingUpdater import PlayerWeaponSwingUpdater
from game.engine.PowerupUpdater import PowerupUpdater
from game.engine.TorchUpdater import TorchUpdater
from game.engine.WeaponDelayUpdater import WeaponDelayUpdater
from game.engine.WeaponFireUpdater import WeaponFireUpdater
from game.engine.WeaponFlashUpdater import WeaponFlashUpdater
from game.engine.WeaponSelector import WeaponSelector
from game.lib.Stopwatch import Stopwatch


class GameUpdater:

    def __init__(
        self,
        personTurnUpdater,
        personMovingTimeUpdater,
        personVelocityUpdater,
        personZUpdater,
        personWallCollisionProcessor,
        personCollisionProcessor,
        personStepUpdater,
        playerLevelSegmentsUpdater,
        enemyLevelSegmentsUpdater,
        playerMovingSwingUpdater,
        backgroundVisibilityUpdater,
        personPositionUpdater,
        personUpdater,
        levelSegmentVisibilityUpdater,
        cameraUpdater,
        personWeaponPositionUpdater,
        weaponDelayUpdater,
        weaponFireUpdater,
        playerWeaponSwingUpdater,
        bulletUpdater,
        nonStandardBulletMovingLogic,
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
        self.personTurnUpdater = personTurnUpdater
        self.personMovingTimeUpdater = personMovingTimeUpdater
        self.personVelocityUpdater = personVelocityUpdater
        self.personZUpdater = personZUpdater
        self.personWallCollisionProcessor = personWallCollisionProcessor
        self.personCollisionProcessor = personCollisionProcessor
        self.personStepUpdater = personStepUpdater
        self.playerLevelSegmentsUpdater = playerLevelSegmentsUpdater
        self.enemyLevelSegmentsUpdater = enemyLevelSegmentsUpdater
        self.playerMovingSwingUpdater = playerMovingSwingUpdater
        self.backgroundVisibilityUpdater = backgroundVisibilityUpdater
        self.personPositionUpdater = personPositionUpdater
        self.personUpdater = personUpdater
        self.levelSegmentVisibilityUpdater = levelSegmentVisibilityUpdater
        self.cameraUpdater = cameraUpdater
        self.personWeaponPositionUpdater = personWeaponPositionUpdater
        self.weaponDelayUpdater = weaponDelayUpdater
        self.weaponFireUpdater = weaponFireUpdater
        self.playerWeaponSwingUpdater = playerWeaponSwingUpdater
        self.bulletUpdater = bulletUpdater
        self.nonStandardBulletMovingLogic = nonStandardBulletMovingLogic
        self.bulletPositionUpdater = bulletPositionUpdater
        self.bulletCollisionProcessor = bulletCollisionProcessor
        self.powerupCollisionProcessor = powerupCollisionProcessor
        self.torchUpdater = torchUpdater
        self.powerupUpdater = powerupUpdater
        self.weaponFlashUpdater = weaponFlashUpdater
        self.bulletTraceUpdater = bulletTraceUpdater
        self.enemyAILogic = enemyAILogic

    def update(self):
        # sw = Stopwatch()
        # sw.start()

        self.personTurnUpdater.update()
        self.personMovingTimeUpdater.update()
        self.personVelocityUpdater.update()
        self.personPositionUpdater.moveNextPosition()
        self.personWallCollisionProcessor.process()
        self.personCollisionProcessor.process()
        self.personZUpdater.updateIfMoved()
        self.personStepUpdater.update()
        self.playerLevelSegmentsUpdater.updateIfMoved()
        self.enemyLevelSegmentsUpdater.updateIfMoved()
        self.levelSegmentVisibilityUpdater.updateIfPlayerMovedOrTurned()
        self.personPositionUpdater.commitNextPosition()
        self.playerMovingSwingUpdater.update()
        self.cameraUpdater.update()
        self.backgroundVisibilityUpdater.updateIfPlayerMovedOrTurned()
        self.personWeaponPositionUpdater.update()
        self.weaponDelayUpdater.update()
        self.weaponFireUpdater.update()
        self.playerWeaponSwingUpdater.update()
        self.bulletUpdater.update()
        self.nonStandardBulletMovingLogic.apply()
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
        self.personUpdater.commitState()
        self.personUpdater.resetWounded()

        # sw.stop()
        # sw.printElapsed()


def makeGameUpdater(resolver):
    return GameUpdater(
        resolver.resolve(PersonTurnUpdater),
        resolver.resolve(PersonMovingTimeUpdater),
        resolver.resolve(PersonVelocityUpdater),
        resolver.resolve(PersonZUpdater),
        resolver.resolve(PersonWallCollisionProcessor),
        resolver.resolve(PersonCollisionProcessor),
        resolver.resolve(PersonStepUpdater),
        resolver.resolve(PlayerLevelSegmentsUpdater),
        resolver.resolve(EnemyLevelSegmentsUpdater),
        resolver.resolve(PlayerMovingSwingUpdater),
        resolver.resolve(BackgroundVisibilityUpdater),
        resolver.resolve(PersonPositionUpdater),
        resolver.resolve(PersonUpdater),
        resolver.resolve(LevelSegmentVisibilityUpdater),
        resolver.resolve(CameraUpdater),
        resolver.resolve(PersonWeaponPositionUpdater),
        resolver.resolve(WeaponDelayUpdater),
        resolver.resolve(WeaponFireUpdater),
        resolver.resolve(PlayerWeaponSwingUpdater),
        resolver.resolve(BulletUpdater),
        resolver.resolve(NonStandardBulletMovingLogic),
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
