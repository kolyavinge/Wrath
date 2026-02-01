from game.engine.cm.BulletCollisionUpdater import BulletCollisionUpdater
from game.engine.cm.PersonCeilingCollisionUpdater import PersonCeilingCollisionUpdater
from game.engine.cm.PersonWallCollisionUpdater import PersonWallCollisionUpdater
from game.engine.cm.PowerupCollisionUpdater import PowerupCollisionUpdater
from game.engine.cm.RayCollisionUpdater import RayCollisionUpdater
from game.engine.level.BackgroundVisibilityUpdater import BackgroundVisibilityUpdater
from game.engine.person.CameraUpdater import CameraUpdater
from game.engine.person.CowboyEasterEggUpdater import CowboyEasterEggUpdater
from game.engine.person.EnemyLevelSegmentsUpdater import EnemyLevelSegmentsUpdater
from game.engine.person.EnemyLifeBarUpdater import EnemyLifeBarUpdater
from game.engine.person.EnemyVisibilityUpdater import EnemyVisibilityUpdater
from game.engine.person.LevelSegmentVisibilityUpdater import *
from game.engine.person.PersonFloorUpdater import PersonFloorUpdater
from game.engine.person.PersonJumpUpdater import PersonJumpUpdater
from game.engine.person.PersonLifeCycleUpdater import PersonLifeCycleUpdater
from game.engine.person.PersonMovingTimeUpdater import PersonMovingTimeUpdater
from game.engine.person.PersonPositionUpdater import PersonPositionUpdater
from game.engine.person.PersonSelectedWeaponPositionUpdater import *
from game.engine.person.PersonStepUpdater import PersonStepUpdater
from game.engine.person.PersonTurnUpdater import PersonTurnUpdater
from game.engine.person.PersonUpdater import PersonUpdater
from game.engine.person.PersonVelocityUpdater import PersonVelocityUpdater
from game.engine.person.PersonWeaponPositionUpdater import PersonWeaponPositionUpdater
from game.engine.person.PersonZUpdater import PersonZUpdater
from game.engine.person.PlayerBloodStainUpdater import PlayerBloodStainUpdater
from game.engine.person.PlayerBreathUpdater import PlayerBreathUpdater
from game.engine.person.PlayerLevelSegmentsUpdater import PlayerLevelSegmentsUpdater
from game.engine.person.PlayerMovingSwingUpdater import PlayerMovingSwingUpdater
from game.engine.person.PlayerWeaponSwingUpdater import PlayerWeaponSwingUpdater
from game.engine.person.TorchUpdater import TorchUpdater
from game.engine.powerup.PowerupUpdater import PowerupUpdater
from game.engine.weapon.BulletPositionUpdater import BulletPositionUpdater
from game.engine.weapon.BulletTraceUpdater import BulletTraceUpdater
from game.engine.weapon.BulletUpdater import BulletUpdater
from game.engine.weapon.ExplosionUpdater import ExplosionUpdater
from game.engine.weapon.NonStandardBulletMovingUpdater import *
from game.engine.weapon.RayPositionUpdater import RayPositionUpdater
from game.engine.weapon.SelectWeaponRequestListener import SelectWeaponRequestListener
from game.engine.weapon.SniperAimFloatingUpdater import SniperAimFloatingUpdater
from game.engine.weapon.WeaponAltFireUpdater import WeaponAltFireUpdater
from game.engine.weapon.WeaponDelayUpdater import WeaponDelayUpdater
from game.engine.weapon.WeaponFireUpdater import WeaponFireUpdater
from game.engine.weapon.WeaponFlashUpdater import WeaponFlashUpdater


class ClientUpdater:

    bulletCollisionUpdater: BulletCollisionUpdater
    personCeilingCollisionUpdater: PersonCeilingCollisionUpdater
    personWallCollisionUpdater: PersonWallCollisionUpdater
    powerupCollisionUpdater: PowerupCollisionUpdater
    rayCollisionUpdater: RayCollisionUpdater
    backgroundVisibilityUpdater: BackgroundVisibilityUpdater
    cameraUpdater: CameraUpdater
    cowboyEasterEggUpdater: CowboyEasterEggUpdater
    enemyLevelSegmentsUpdater: EnemyLevelSegmentsUpdater
    enemyLifeBarUpdater: EnemyLifeBarUpdater
    enemyVisibilityUpdater: EnemyVisibilityUpdater
    levelSegmentVisibilityUpdater: LevelSegmentVisibilityUpdater
    personFloorUpdater: PersonFloorUpdater
    personJumpUpdater: PersonJumpUpdater
    personLifeCycleUpdater: PersonLifeCycleUpdater
    personMovingTimeUpdater: PersonMovingTimeUpdater
    personPositionUpdater: PersonPositionUpdater
    personSelectedWeaponPositionUpdater: PersonSelectedWeaponPositionUpdater
    personStepUpdater: PersonStepUpdater
    personTurnUpdater: PersonTurnUpdater
    personUpdater: PersonUpdater
    personVelocityUpdater: PersonVelocityUpdater
    personWeaponPositionUpdater: PersonWeaponPositionUpdater
    personZUpdater: PersonZUpdater
    playerBloodStainUpdater: PlayerBloodStainUpdater
    playerBreathUpdater: PlayerBreathUpdater
    playerLevelSegmentsUpdater: PlayerLevelSegmentsUpdater
    playerMovingSwingUpdater: PlayerMovingSwingUpdater
    playerWeaponSwingUpdater: PlayerWeaponSwingUpdater
    torchUpdater: TorchUpdater
    powerupUpdater: PowerupUpdater
    bulletPositionUpdater: BulletPositionUpdater
    bulletTraceUpdater: BulletTraceUpdater
    bulletUpdater: BulletUpdater
    explosionUpdater: ExplosionUpdater
    sniperAimFloatingUpdater: SniperAimFloatingUpdater
    rayPositionUpdater: RayPositionUpdater
    weaponAltFireUpdater: WeaponAltFireUpdater
    weaponDelayUpdater: WeaponDelayUpdater
    weaponFireUpdater: WeaponFireUpdater
    weaponFlashUpdater: WeaponFlashUpdater
    # event listeners
    selectWeaponRequestListener: SelectWeaponRequestListener

    def update(self, gameState):
        self.personTurnUpdater.updateForPlayer(gameState)
        self.personMovingTimeUpdater.updateForPlayer(gameState)
        self.personVelocityUpdater.updateForPlayer(gameState)
        self.personPositionUpdater.movePlayerNextPosition(gameState)
        self.personFloorUpdater.updatePlayerNextFloor(gameState)
        self.personJumpUpdater.updateForPlayer(gameState)
        self.personWallCollisionUpdater.updateForPlayer(gameState)
        self.personZUpdater.updateIfMovedForPlayer(gameState)
        self.personCeilingCollisionUpdater.updateForPlayer(gameState)
        self.personStepUpdater.update(gameState)
        self.personPositionUpdater.commitPlayerNextPosition(gameState)
        self.personFloorUpdater.commitPlayerNextFloor(gameState)
        self.playerLevelSegmentsUpdater.updateIfMoved(gameState)
        self.enemyLevelSegmentsUpdater.updateIfMoved(gameState)
        self.personWeaponPositionUpdater.update(gameState)
        self.personSelectedWeaponPositionUpdater.update(gameState)
        self.weaponDelayUpdater.updateForPlayer(gameState)
        self.weaponFireUpdater.updateForPlayer(gameState)
        self.weaponAltFireUpdater.updateForPlayer(gameState)
        self.personLifeCycleUpdater.update(gameState)
        self.bulletPositionUpdater.moveNextPosition(gameState)
        self.bulletCollisionUpdater.updateForConstructions(gameState)
        self.bulletPositionUpdater.commitNextPosition(gameState)
        self.rayPositionUpdater.update(gameState)
        self.rayCollisionUpdater.updateForConstructions(gameState)
        self.powerupCollisionUpdater.updateForPlayer(gameState)
        self.bulletUpdater.update(gameState)
        self.explosionUpdater.update(gameState)
        self.powerupUpdater.update(gameState)
        self.weaponFlashUpdater.update(gameState)
        self.bulletTraceUpdater.update(gameState)
        self.torchUpdater.update(gameState)
        self.cameraUpdater.update(gameState)
        self.levelSegmentVisibilityUpdater.updateIfPlayerMovedOrTurned(gameState)
        self.enemyVisibilityUpdater.updateEnemiesVisibility(gameState)
        self.backgroundVisibilityUpdater.updateIfNeeded(gameState)
        self.playerMovingSwingUpdater.update(gameState)
        self.playerBreathUpdater.update(gameState)
        self.playerWeaponSwingUpdater.update(gameState)
        self.playerBloodStainUpdater.update(gameState)
        self.enemyLifeBarUpdater.update(gameState)
        self.sniperAimFloatingUpdater.update()
        self.cowboyEasterEggUpdater.update(gameState)
        self.personPositionUpdater.resetMovedAndTurnedForPlayer(gameState)
        self.personUpdater.commitZStateForPlayer(gameState)
        self.personUpdater.updateDelaysForPlayer(gameState)
        self.bulletUpdater.removeNotAlive(gameState)
        gameState.collisionData.clear()
        gameState.updateGlobalTime()
