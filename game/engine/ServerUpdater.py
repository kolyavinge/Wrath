from game.engine.ai.EnemyAIUpdater import EnemyAIUpdater
from game.engine.cm.BulletCollisionUpdater import BulletCollisionUpdater
from game.engine.cm.ExplosionCollisionUpdater import ExplosionCollisionUpdater
from game.engine.cm.PersonCeilingCollisionUpdater import PersonCeilingCollisionUpdater
from game.engine.cm.PersonCollisionUpdater import PersonCollisionUpdater
from game.engine.cm.PersonWallCollisionUpdater import PersonWallCollisionUpdater
from game.engine.cm.PowerupCollisionUpdater import PowerupCollisionUpdater
from game.engine.cm.RayCollisionUpdater import RayCollisionUpdater
from game.engine.person.EnemyLevelSegmentsUpdater import EnemyLevelSegmentsUpdater
from game.engine.person.FragStatisticUpdater import FragStatisticUpdater
from game.engine.person.LevelSegmentVisibilityUpdater import *
from game.engine.person.PersonFloorUpdater import PersonFloorUpdater
from game.engine.person.PersonJumpUpdater import PersonJumpUpdater
from game.engine.person.PersonLifeCycleUpdater import PersonLifeCycleUpdater
from game.engine.person.PersonMovingTimeUpdater import PersonMovingTimeUpdater
from game.engine.person.PersonPositionUpdater import PersonPositionUpdater
from game.engine.person.PersonRespawnUpdater import PersonRespawnUpdater
from game.engine.person.PersonSelectedWeaponPositionUpdater import *
from game.engine.person.PersonTurnUpdater import PersonTurnUpdater
from game.engine.person.PersonUpdater import PersonUpdater
from game.engine.person.PersonVelocityUpdater import PersonVelocityUpdater
from game.engine.person.PersonWeaponPositionUpdater import PersonWeaponPositionUpdater
from game.engine.person.PersonZUpdater import PersonZUpdater
from game.engine.powerup.PowerupUpdater import PowerupUpdater
from game.engine.weapon.BulletPositionUpdater import BulletPositionUpdater
from game.engine.weapon.BulletUpdater import BulletUpdater
from game.engine.weapon.ExplosionUpdater import ExplosionUpdater
from game.engine.weapon.NonStandardBulletMovingUpdater import *
from game.engine.weapon.RayPositionUpdater import RayPositionUpdater
from game.engine.weapon.SelectWeaponRequestListener import SelectWeaponRequestListener
from game.engine.weapon.WeaponAltFireUpdater import WeaponAltFireUpdater
from game.engine.weapon.WeaponDelayUpdater import WeaponDelayUpdater
from game.engine.weapon.WeaponFireUpdater import WeaponFireUpdater


class ServerUpdater:

    enemyAIUpdater: EnemyAIUpdater
    bulletCollisionUpdater: BulletCollisionUpdater
    explosionCollisionUpdater: ExplosionCollisionUpdater
    personCeilingCollisionUpdater: PersonCeilingCollisionUpdater
    personCollisionUpdater: PersonCollisionUpdater
    personWallCollisionUpdater: PersonWallCollisionUpdater
    powerupCollisionUpdater: PowerupCollisionUpdater
    rayCollisionUpdater: RayCollisionUpdater
    enemyLevelSegmentsUpdater: EnemyLevelSegmentsUpdater
    fragStatisticUpdater: FragStatisticUpdater
    personFloorUpdater: PersonFloorUpdater
    personJumpUpdater: PersonJumpUpdater
    personLifeCycleUpdater: PersonLifeCycleUpdater
    personMovingTimeUpdater: PersonMovingTimeUpdater
    personPositionUpdater: PersonPositionUpdater
    personRespawnUpdater: PersonRespawnUpdater
    personTurnUpdater: PersonTurnUpdater
    personUpdater: PersonUpdater
    personVelocityUpdater: PersonVelocityUpdater
    personWeaponPositionUpdater: PersonWeaponPositionUpdater
    personZUpdater: PersonZUpdater
    powerupUpdater: PowerupUpdater
    bulletPositionUpdater: BulletPositionUpdater
    bulletUpdater: BulletUpdater
    explosionUpdater: ExplosionUpdater
    nonStandardBulletMovingUpdater: NonStandardBulletMovingUpdater
    rayPositionUpdater: RayPositionUpdater
    weaponAltFireUpdater: WeaponAltFireUpdater
    weaponDelayUpdater: WeaponDelayUpdater
    weaponFireUpdater: WeaponFireUpdater
    # event listeners
    selectWeaponRequestListener: SelectWeaponRequestListener

    def update(self, gameState):
        self.personTurnUpdater.updateForEnemies(gameState)
        self.personMovingTimeUpdater.updateForEnemies(gameState)
        self.personVelocityUpdater.updateForEnemies(gameState)
        self.personPositionUpdater.moveEnemiesNextPosition(gameState)
        self.personRespawnUpdater.update(gameState)
        self.personFloorUpdater.updateEnemiesNextFloor(gameState)
        self.personJumpUpdater.updateForEnemies(gameState)
        self.personWallCollisionUpdater.updateForEnemies(gameState)
        self.personCollisionUpdater.update(gameState)
        self.personZUpdater.updateIfMovedForEnemies(gameState)
        self.personCeilingCollisionUpdater.updateForEnemies(gameState)
        self.personPositionUpdater.commitEnemiesNextPosition(gameState)
        self.personFloorUpdater.commitEnemiesNextFloor(gameState)
        self.enemyLevelSegmentsUpdater.updateIfMoved(gameState)
        self.personWeaponPositionUpdater.update(gameState)
        self.weaponDelayUpdater.updateForEnemies(gameState)
        self.weaponFireUpdater.updateForEnemies(gameState)
        self.weaponAltFireUpdater.updateForEnemies(gameState)
        self.personLifeCycleUpdater.update(gameState)
        self.nonStandardBulletMovingUpdater.update(gameState)
        self.bulletPositionUpdater.moveNextPosition(gameState)
        self.bulletCollisionUpdater.update(gameState)
        self.bulletPositionUpdater.commitNextPosition(gameState)
        self.rayPositionUpdater.update(gameState)
        self.rayCollisionUpdater.update(gameState)
        self.powerupCollisionUpdater.updateForEnemies(gameState)
        self.explosionCollisionUpdater.update(gameState)
        self.explosionUpdater.update(gameState)
        self.powerupUpdater.generateNew(gameState)
        self.enemyAIUpdater.update(gameState)
        self.personPositionUpdater.resetMovedAndTurned(gameState)
        self.personUpdater.commitZStateForEnemies(gameState)
        self.personUpdater.updateDelaysForEnemies(gameState)
        self.fragStatisticUpdater.update(gameState)
        gameState.reservedCollisionData.update(gameState.collisionData)
        gameState.collisionData.clear()
        gameState.updateGlobalTime()
