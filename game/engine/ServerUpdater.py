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

    gameState: GameState
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

    def update(self):
        # читаем и применяем текущие сообщения от всех клиентов
        self.personTurnUpdater.updateForEnemies()
        self.personMovingTimeUpdater.updateForEnemies()
        self.personVelocityUpdater.updateForEnemies()
        self.personPositionUpdater.moveEnemyNextPosition()
        self.personRespawnUpdater.update()
        self.personFloorUpdater.updateEnemyNextFloor()
        self.personJumpUpdater.updateForEnemies()
        self.personWallCollisionUpdater.updateForEnemies()
        self.personCollisionUpdater.update()
        self.personZUpdater.updateIfMovedForEnemies()
        self.personCeilingCollisionUpdater.updateForEnemies()
        self.personPositionUpdater.commitEnemyNextPosition()
        self.personFloorUpdater.commitEnemyNextFloor()
        self.enemyLevelSegmentsUpdater.updateIfMoved()
        self.weaponDelayUpdater.updateForEnemies()
        self.weaponFireUpdater.updateForEnemies()
        self.weaponAltFireUpdater.updateForEnemies()
        self.personLifeCycleUpdater.update()
        self.nonStandardBulletMovingUpdater.update()
        self.bulletPositionUpdater.moveNextPosition()
        self.bulletCollisionUpdater.update()
        self.bulletPositionUpdater.commitNextPosition()
        self.rayPositionUpdater.update()
        self.rayCollisionUpdater.update()
        self.powerupCollisionUpdater.updateForEnemies()
        self.explosionCollisionUpdater.update()
        self.explosionUpdater.update()
        self.powerupUpdater.generateNew()
        self.enemyAIUpdater.update()
        self.personPositionUpdater.resetMovedAndTurned()
        self.personUpdater.commitZStateForEnemies()
        self.personUpdater.updateDelaysForEnemies()
        self.bulletUpdater.removeNotAlive()
        self.fragStatisticUpdater.update()
        self.gameState.collisionData.clear()
        self.gameState.updateGlobalTime()
        # формируем и отправляем новый сообщения клиентам
