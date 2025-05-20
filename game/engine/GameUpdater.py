from game.engine.ai.EnemyAIUpdater import EnemyAIUpdater
from game.engine.CameraUpdater import CameraUpdater
from game.engine.cm.BulletCollisionUpdater import BulletCollisionUpdater
from game.engine.cm.PersonCollisionUpdater import PersonCollisionUpdater
from game.engine.cm.PersonWallCollisionUpdater import PersonWallCollisionUpdater
from game.engine.cm.PowerupCollisionUpdater import PowerupCollisionUpdater
from game.engine.person.BackgroundVisibilityUpdater import BackgroundVisibilityUpdater
from game.engine.person.EnemyLevelSegmentsUpdater import EnemyLevelSegmentsUpdater
from game.engine.person.LevelSegmentVisibilityUpdater import *
from game.engine.person.PersonBreathUpdater import PersonBreathUpdater
from game.engine.person.PersonMovingTimeUpdater import PersonMovingTimeUpdater
from game.engine.person.PersonPositionUpdater import PersonPositionUpdater
from game.engine.person.PersonStepUpdater import PersonStepUpdater
from game.engine.person.PersonTurnUpdater import PersonTurnUpdater
from game.engine.person.PersonUpdater import PersonUpdater
from game.engine.person.PersonVelocityUpdater import PersonVelocityUpdater
from game.engine.person.PersonWeaponPositionUpdater import PersonWeaponPositionUpdater
from game.engine.person.PersonZUpdater import PersonZUpdater
from game.engine.person.PlayerLevelSegmentsUpdater import PlayerLevelSegmentsUpdater
from game.engine.person.PlayerMovingSwingUpdater import PlayerMovingSwingUpdater
from game.engine.person.PlayerWeaponSwingUpdater import PlayerWeaponSwingUpdater
from game.engine.person.TorchUpdater import TorchUpdater
from game.engine.powerup.PowerupUpdater import PowerupUpdater
from game.engine.weapon.BulletPositionUpdater import BulletPositionUpdater
from game.engine.weapon.BulletTraceUpdater import BulletTraceUpdater
from game.engine.weapon.BulletUpdater import BulletUpdater
from game.engine.weapon.NonStandardBulletMovingUpdater import *
from game.engine.weapon.SelectWeaponRequestListener import SelectWeaponRequestListener
from game.engine.weapon.WeaponDelayUpdater import WeaponDelayUpdater
from game.engine.weapon.WeaponFireUpdater import WeaponFireUpdater
from game.engine.weapon.WeaponFlashUpdater import WeaponFlashUpdater
from game.lib.Stopwatch import Stopwatch


class GameUpdater:

    gameData: GameData
    personTurnUpdater: PersonTurnUpdater
    personMovingTimeUpdater: PersonMovingTimeUpdater
    personVelocityUpdater: PersonVelocityUpdater
    personZUpdater: PersonZUpdater
    personWallCollisionUpdater: PersonWallCollisionUpdater
    personCollisionUpdater: PersonCollisionUpdater
    personStepUpdater: PersonStepUpdater
    playerLevelSegmentsUpdater: PlayerLevelSegmentsUpdater
    enemyLevelSegmentsUpdater: EnemyLevelSegmentsUpdater
    playerMovingSwingUpdater: PlayerMovingSwingUpdater
    backgroundVisibilityUpdater: BackgroundVisibilityUpdater
    personPositionUpdater: PersonPositionUpdater
    personUpdater: PersonUpdater
    levelSegmentVisibilityUpdater: LevelSegmentVisibilityUpdater
    cameraUpdater: CameraUpdater
    personBreathUpdater: PersonBreathUpdater
    personWeaponPositionUpdater: PersonWeaponPositionUpdater
    weaponDelayUpdater: WeaponDelayUpdater
    weaponFireUpdater: WeaponFireUpdater
    playerWeaponSwingUpdater: PlayerWeaponSwingUpdater
    bulletUpdater: BulletUpdater
    nonStandardBulletMovingUpdater: NonStandardBulletMovingUpdater
    bulletPositionUpdater: BulletPositionUpdater
    bulletCollisionUpdater: BulletCollisionUpdater
    powerupCollisionUpdater: PowerupCollisionUpdater
    torchUpdater: TorchUpdater
    powerupUpdater: PowerupUpdater
    weaponFlashUpdater: WeaponFlashUpdater
    bulletTraceUpdater: BulletTraceUpdater
    enemyAIUpdater: EnemyAIUpdater
    # event listeners
    selectWeaponRequestListener: SelectWeaponRequestListener

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
        self.personBreathUpdater.update()
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
        self.gameData.collisionData.clear()

        # sw.stop()
        # sw.printElapsed()
