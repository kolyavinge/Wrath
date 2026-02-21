from game.engine.ai.EnemyAIUpdater import EnemyAIUpdater
from game.engine.cm.BulletCollisionUpdater import BulletCollisionUpdater
from game.engine.cm.ExplosionCollisionUpdater import ExplosionCollisionUpdater
from game.engine.cm.PersonCeilingCollisionUpdater import PersonCeilingCollisionUpdater
from game.engine.cm.PersonCollisionUpdater import PersonCollisionUpdater
from game.engine.cm.PersonWallCollisionUpdater import PersonWallCollisionUpdater
from game.engine.cm.PowerupCollisionUpdater import PowerupCollisionUpdater
from game.engine.cm.RayCollisionUpdater import RayCollisionUpdater
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
from game.engine.person.PlayerLevelSegmentsUpdater import PlayerLevelSegmentsUpdater
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
    playerLevelSegmentsUpdater: PlayerLevelSegmentsUpdater
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
        self.personTurnUpdater.updateForBots(gameState)
        self.personMovingTimeUpdater.updateForBots(gameState)
        self.personVelocityUpdater.updateForBots(gameState)
        self.personPositionUpdater.moveBotsNextPosition(gameState)
        self.personRespawnUpdater.update(gameState)
        self.personFloorUpdater.updateBotsNextFloor(gameState)
        self.personJumpUpdater.updateForBots(gameState)
        self.personWallCollisionUpdater.updateForBots(gameState)
        self.personCollisionUpdater.update(gameState)
        self.personZUpdater.updateForBots(gameState)
        self.personCeilingCollisionUpdater.updateForBots(gameState)
        self.personPositionUpdater.commitBotsNextPosition(gameState)
        self.personFloorUpdater.commitBotsNextFloor(gameState)
        self.playerLevelSegmentsUpdater.updateForAllPerson(gameState)
        self.personWeaponPositionUpdater.update(gameState)
        self.weaponDelayUpdater.updateForBots(gameState)
        self.weaponFireUpdater.updateForEnemies(gameState)
        self.weaponAltFireUpdater.updateForBots(gameState)
        self.nonStandardBulletMovingUpdater.update(gameState)
        self.bulletPositionUpdater.moveNextPosition(gameState)
        self.bulletCollisionUpdater.update(gameState)
        self.bulletPositionUpdater.commitNextPosition(gameState)
        self.rayPositionUpdater.update(gameState)
        self.rayCollisionUpdater.update(gameState)
        self.powerupCollisionUpdater.updateForBots(gameState)
        self.explosionCollisionUpdater.update(gameState)
        self.explosionUpdater.update(gameState)
        self.powerupUpdater.generateNew(gameState)
        self.personLifeCycleUpdater.update(gameState)
        self.enemyAIUpdater.update(gameState)
        self.personUpdater.commitZStateForBots(gameState)
        self.personUpdater.updateDelaysForBots(gameState)
        self.fragStatisticUpdater.update(gameState)
        gameState.updateGlobalTime()

    def clear(self, gameState):
        gameState.updateStatistic.clear()
        gameState.reservedCollisionData.update(gameState.collisionData)
        gameState.collisionData.clear()
