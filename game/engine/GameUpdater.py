from game.engine.ai.EnemyAIUpdater import EnemyAIUpdater
from game.engine.BackgroundVisibilityUpdater import BackgroundVisibilityUpdater
from game.engine.BulletPositionUpdater import BulletPositionUpdater
from game.engine.BulletTraceUpdater import BulletTraceUpdater
from game.engine.BulletUpdater import BulletUpdater
from game.engine.CameraUpdater import CameraUpdater
from game.engine.cm.BulletCollisionUpdater import BulletCollisionUpdater
from game.engine.cm.PersonCollisionUpdater import PersonCollisionUpdater
from game.engine.cm.PersonWallCollisionUpdater import PersonWallCollisionUpdater
from game.engine.cm.PowerupCollisionUpdater import PowerupCollisionUpdater
from game.engine.EnemyLevelSegmentsUpdater import EnemyLevelSegmentsUpdater
from game.engine.LevelSegmentVisibilityUpdater import LevelSegmentVisibilityUpdater
from game.engine.NonStandardBulletMovingUpdater import NonStandardBulletMovingUpdater
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
        personWallCollisionUpdater,
        personCollisionUpdater,
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
        nonStandardBulletMovingUpdater,
        bulletPositionUpdater,
        bulletCollisionUpdater,
        powerupCollisionUpdater,
        torchUpdater,
        powerupUpdater,
        weaponFlashUpdater,
        bulletTraceUpdater,
        enemyAIUpdater,
        # event listeners
        weaponSelector,
    ):
        self.personTurnUpdater = personTurnUpdater
        self.personMovingTimeUpdater = personMovingTimeUpdater
        self.personVelocityUpdater = personVelocityUpdater
        self.personZUpdater = personZUpdater
        self.personWallCollisionUpdater = personWallCollisionUpdater
        self.personCollisionUpdater = personCollisionUpdater
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
        self.nonStandardBulletMovingUpdater = nonStandardBulletMovingUpdater
        self.bulletPositionUpdater = bulletPositionUpdater
        self.bulletCollisionUpdater = bulletCollisionUpdater
        self.powerupCollisionUpdater = powerupCollisionUpdater
        self.torchUpdater = torchUpdater
        self.powerupUpdater = powerupUpdater
        self.weaponFlashUpdater = weaponFlashUpdater
        self.bulletTraceUpdater = bulletTraceUpdater
        self.enemyAIUpdater = enemyAIUpdater

    def update(self):
        # sw = Stopwatch()
        # sw.start()

        self.personTurnUpdater.update()
        self.personMovingTimeUpdater.update()
        self.personVelocityUpdater.update()
        self.personPositionUpdater.moveNextPosition()
        self.personWallCollisionUpdater.update()
        self.personCollisionUpdater.update()
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
        self.nonStandardBulletMovingUpdater.update()
        self.bulletPositionUpdater.moveNextPosition()
        self.bulletCollisionUpdater.update()
        self.bulletPositionUpdater.commitNextPosition()
        self.powerupCollisionUpdater.update()
        self.torchUpdater.update()
        self.powerupUpdater.update()
        self.powerupUpdater.generateNew()
        self.weaponFlashUpdater.update()
        self.bulletTraceUpdater.update()
        self.enemyAIUpdater.update()
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
        resolver.resolve(PersonWallCollisionUpdater),
        resolver.resolve(PersonCollisionUpdater),
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
        resolver.resolve(NonStandardBulletMovingUpdater),
        resolver.resolve(BulletPositionUpdater),
        resolver.resolve(BulletCollisionUpdater),
        resolver.resolve(PowerupCollisionUpdater),
        resolver.resolve(TorchUpdater),
        resolver.resolve(PowerupUpdater),
        resolver.resolve(WeaponFlashUpdater),
        resolver.resolve(BulletTraceUpdater),
        resolver.resolve(EnemyAIUpdater),
        resolver.resolve(WeaponSelector),
    )
