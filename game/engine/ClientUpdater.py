from game.engine.cm.BulletCollisionUpdater import BulletCollisionUpdater
from game.engine.cm.PersonCeilingCollisionUpdater import PersonCeilingCollisionUpdater
from game.engine.cm.PersonWallCollisionUpdater import PersonWallCollisionUpdater
from game.engine.cm.PowerupCollisionUpdater import PowerupCollisionUpdater
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
from game.engine.weapon.SelectWeaponRequestListener import SelectWeaponRequestListener
from game.engine.weapon.SniperAimFloatingUpdater import SniperAimFloatingUpdater
from game.engine.weapon.WeaponAltFireUpdater import WeaponAltFireUpdater
from game.engine.weapon.WeaponDelayUpdater import WeaponDelayUpdater
from game.engine.weapon.WeaponFireUpdater import WeaponFireUpdater
from game.engine.weapon.WeaponFlashUpdater import WeaponFlashUpdater


class ClientUpdater:

    gameState: GameState
    bulletCollisionUpdater: BulletCollisionUpdater
    personCeilingCollisionUpdater: PersonCeilingCollisionUpdater
    personWallCollisionUpdater: PersonWallCollisionUpdater
    powerupCollisionUpdater: PowerupCollisionUpdater
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
    weaponAltFireUpdater: WeaponAltFireUpdater
    weaponDelayUpdater: WeaponDelayUpdater
    weaponFireUpdater: WeaponFireUpdater
    weaponFlashUpdater: WeaponFlashUpdater
    # event listeners
    selectWeaponRequestListener: SelectWeaponRequestListener

    def update(self):
        # читаем и применяем текущие сообщения от сервера
        self.personTurnUpdater.updateForPlayer()
        self.personMovingTimeUpdater.updateForPlayer()
        self.personVelocityUpdater.updateForPlayer()
        self.personPositionUpdater.movePlayerNextPosition()
        self.personFloorUpdater.updatePlayerNextFloor()
        self.personJumpUpdater.updateForPlayer()
        self.personWallCollisionUpdater.updateForPlayer()
        self.personZUpdater.updateIfMovedForPlayer()
        self.personCeilingCollisionUpdater.updateForPlayer()
        self.personPositionUpdater.commitPlayerNextPosition()
        self.personFloorUpdater.commitPlayerNextFloor()
        # асинхронно отправляем на сервер позицию игрока и направление взгляда
        self.playerLevelSegmentsUpdater.updateIfMoved()
        self.enemyLevelSegmentsUpdater.updateIfMoved()
        self.personStepUpdater.update()
        self.personWeaponPositionUpdater.update()
        self.personSelectedWeaponPositionUpdater.update()
        self.weaponDelayUpdater.updateForPlayer()
        self.weaponFireUpdater.updateForPlayer()
        self.weaponAltFireUpdater.updateForPlayer()
        # отправляем инфу о выстреле
        self.personLifeCycleUpdater.update()
        self.bulletPositionUpdater.moveNextPosition()
        self.bulletCollisionUpdater.updateForConstructions()
        self.bulletPositionUpdater.commitNextPosition()
        self.powerupCollisionUpdater.updateForPlayer()
        # отправляем если взяли поверап
        self.bulletUpdater.update()
        self.explosionUpdater.update()
        self.powerupUpdater.update()
        self.weaponFlashUpdater.update()
        self.bulletTraceUpdater.update()
        self.torchUpdater.update()
        self.cameraUpdater.update()
        self.levelSegmentVisibilityUpdater.updateIfPlayerMovedOrTurned()
        self.enemyVisibilityUpdater.updateEnemiesVisibility()
        self.backgroundVisibilityUpdater.updateIfNeeded()
        self.playerMovingSwingUpdater.update()
        self.playerBreathUpdater.update()
        self.playerWeaponSwingUpdater.update()
        self.playerBloodStainUpdater.update()
        self.enemyLifeBarUpdater.update()
        self.sniperAimFloatingUpdater.update()
        self.cowboyEasterEggUpdater.update()
        self.personPositionUpdater.resetMovedAndTurnedForPlayer()
        self.personUpdater.commitZStateForPlayer()
        self.personUpdater.updateDelaysForPlayer()
        self.bulletUpdater.removeNotAlive()
        self.gameState.collisionData.clear()
        self.gameState.updateGlobalTime()
