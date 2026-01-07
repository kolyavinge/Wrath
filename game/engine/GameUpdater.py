from game.engine.ai.EnemyAIUpdater import EnemyAIUpdater
from game.engine.CameraUpdater import CameraUpdater
from game.engine.cm.BulletCollisionUpdater import BulletCollisionUpdater
from game.engine.cm.ExplosionCollisionUpdater import ExplosionCollisionUpdater
from game.engine.cm.PersonCeilingCollisionUpdater import PersonCeilingCollisionUpdater
from game.engine.cm.PersonCollisionUpdater import PersonCollisionUpdater
from game.engine.cm.PersonWallCollisionUpdater import PersonWallCollisionUpdater
from game.engine.cm.PowerupCollisionUpdater import PowerupCollisionUpdater
from game.engine.cm.RayCollisionUpdater import RayCollisionUpdater
from game.engine.GameState import GameState
from game.engine.level.BackgroundVisibilityUpdater import BackgroundVisibilityUpdater
from game.engine.person.CowboyEasterEggUpdater import CowboyEasterEggUpdater
from game.engine.person.EnemyLevelSegmentsUpdater import EnemyLevelSegmentsUpdater
from game.engine.person.EnemyLifeBarUpdater import EnemyLifeBarUpdater
from game.engine.person.EnemyVisibilityUpdater import EnemyVisibilityUpdater
from game.engine.person.FragStatisticUpdater import FragStatisticUpdater
from game.engine.person.LevelSegmentVisibilityUpdater import *
from game.engine.person.PersonBreathUpdater import PersonBreathUpdater
from game.engine.person.PersonFloorUpdater import PersonFloorUpdater
from game.engine.person.PersonJumpUpdater import PersonJumpUpdater
from game.engine.person.PersonLifeCycleUpdater import PersonLifeCycleUpdater
from game.engine.person.PersonMovingTimeUpdater import PersonMovingTimeUpdater
from game.engine.person.PersonPositionUpdater import PersonPositionUpdater
from game.engine.person.PersonRespawnUpdater import PersonRespawnUpdater
from game.engine.person.PersonSelectedWeaponPositionUpdater import *
from game.engine.person.PersonStepUpdater import PersonStepUpdater
from game.engine.person.PersonTurnUpdater import PersonTurnUpdater
from game.engine.person.PersonUpdater import PersonUpdater
from game.engine.person.PersonVelocityUpdater import PersonVelocityUpdater
from game.engine.person.PersonWeaponPositionUpdater import PersonWeaponPositionUpdater
from game.engine.person.PersonZUpdater import PersonZUpdater
from game.engine.person.PlayerBloodStainUpdater import PlayerBloodStainUpdater
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
from game.tools.CpuProfiler import cpuProfile
from game.tools.timeProfile import timeProfile


class GameUpdater:

    gameState: GameState
    enemyAIUpdater: EnemyAIUpdater
    cameraUpdater: CameraUpdater
    bulletCollisionUpdater: BulletCollisionUpdater
    explosionCollisionUpdater: ExplosionCollisionUpdater
    personCeilingCollisionUpdater: PersonCeilingCollisionUpdater
    personCollisionUpdater: PersonCollisionUpdater
    personWallCollisionUpdater: PersonWallCollisionUpdater
    powerupCollisionUpdater: PowerupCollisionUpdater
    rayCollisionUpdater: RayCollisionUpdater
    backgroundVisibilityUpdater: BackgroundVisibilityUpdater
    cowboyEasterEggUpdater: CowboyEasterEggUpdater
    enemyLevelSegmentsUpdater: EnemyLevelSegmentsUpdater
    enemyLifeBarUpdater: EnemyLifeBarUpdater
    enemyVisibilityUpdater: EnemyVisibilityUpdater
    fragStatisticUpdater: FragStatisticUpdater
    levelSegmentVisibilityUpdater: LevelSegmentVisibilityUpdater
    personBreathUpdater: PersonBreathUpdater
    personFloorUpdater: PersonFloorUpdater
    personJumpUpdater: PersonJumpUpdater
    personLifeCycleUpdater: PersonLifeCycleUpdater
    personMovingTimeUpdater: PersonMovingTimeUpdater
    personPositionUpdater: PersonPositionUpdater
    personRespawnUpdater: PersonRespawnUpdater
    personSelectedWeaponPositionUpdater: PersonSelectedWeaponPositionUpdater
    personStepUpdater: PersonStepUpdater
    personTurnUpdater: PersonTurnUpdater
    personUpdater: PersonUpdater
    personVelocityUpdater: PersonVelocityUpdater
    personWeaponPositionUpdater: PersonWeaponPositionUpdater
    personZUpdater: PersonZUpdater
    playerBloodStainUpdater: PlayerBloodStainUpdater
    playerLevelSegmentsUpdater: PlayerLevelSegmentsUpdater
    playerMovingSwingUpdater: PlayerMovingSwingUpdater
    playerWeaponSwingUpdater: PlayerWeaponSwingUpdater
    torchUpdater: TorchUpdater
    powerupUpdater: PowerupUpdater
    bulletPositionUpdater: BulletPositionUpdater
    bulletTraceUpdater: BulletTraceUpdater
    bulletUpdater: BulletUpdater
    explosionUpdater: ExplosionUpdater
    nonStandardBulletMovingUpdater: NonStandardBulletMovingUpdater
    rayPositionUpdater: RayPositionUpdater
    sniperAimFloatingUpdater: SniperAimFloatingUpdater
    weaponAltFireUpdater: WeaponAltFireUpdater
    weaponDelayUpdater: WeaponDelayUpdater
    weaponFireUpdater: WeaponFireUpdater
    weaponFlashUpdater: WeaponFlashUpdater
    # event listeners
    selectWeaponRequestListener: SelectWeaponRequestListener

    # @timeProfile("Game updated", CommonConstants.mainTimerMsec / 1000.0, showOnlyLimited=True)
    # @cpuProfile
    def update(self):
        # --- main game loop ---

        self.personTurnUpdater.update()
        self.personMovingTimeUpdater.update()
        self.personVelocityUpdater.update()
        self.personPositionUpdater.moveNextPosition()
        self.personRespawnUpdater.update()
        self.personFloorUpdater.updateNextFloor()
        self.personJumpUpdater.update()
        self.personWallCollisionUpdater.update()
        self.personCollisionUpdater.update()
        self.personZUpdater.updateIfMoved()
        self.personCeilingCollisionUpdater.update()
        self.personStepUpdater.update()  # можно делать для всех персонажей
        self.personPositionUpdater.commitNextPosition()
        self.personFloorUpdater.commitNextFloor()
        # асинхронно отправляем на сервер позицию игрока и направление взгляда
        self.personWeaponPositionUpdater.update()
        self.personSelectedWeaponPositionUpdater.update()
        self.playerLevelSegmentsUpdater.updateIfMoved()
        self.enemyLevelSegmentsUpdater.updateIfMoved()

        # для игрока на клиенте
        # для ботов на сервере
        self.weaponDelayUpdater.update()
        self.weaponFireUpdater.update()
        self.weaponAltFireUpdater.update()

        # на сервере
        self.nonStandardBulletMovingUpdater.update()
        self.bulletPositionUpdater.moveNextPosition()
        self.bulletCollisionUpdater.update()
        self.bulletPositionUpdater.commitNextPosition()
        self.rayPositionUpdater.update()
        self.rayCollisionUpdater.update()
        self.powerupCollisionUpdater.update()
        self.explosionCollisionUpdater.update()
        self.powerupUpdater.generateNew()
        self.enemyAIUpdater.update()
        # на сервере

        self.personLifeCycleUpdater.update()
        self.bulletUpdater.update()
        self.explosionUpdater.update()
        self.powerupUpdater.update()
        self.weaponFlashUpdater.update()
        self.bulletTraceUpdater.update()
        self.torchUpdater.update()
        self.personPositionUpdater.resetMovedAndTurned()
        self.personUpdater.commitZState()
        self.personUpdater.updateDelays()
        self.fragStatisticUpdater.update()
        self.bulletUpdater.removeNotAlive()

        # for player
        self.cameraUpdater.update()
        self.levelSegmentVisibilityUpdater.updateIfPlayerMovedOrTurned()
        self.enemyVisibilityUpdater.updateEnemiesVisibility()
        self.playerMovingSwingUpdater.update()
        self.personBreathUpdater.update()
        self.backgroundVisibilityUpdater.updateIfNeeded()
        self.playerWeaponSwingUpdater.update()
        self.playerBloodStainUpdater.update()
        self.enemyLifeBarUpdater.update()
        self.cowboyEasterEggUpdater.update()
        self.sniperAimFloatingUpdater.update()
        # for player

        self.gameState.collisionData.clear()
        self.gameState.updateGlobalTime()
