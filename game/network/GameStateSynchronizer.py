from game.core.ClientPersonInitializer import ClientPersonInitializer
from game.engine.person.PersonTurnLogic import PersonTurnLogic
from game.engine.person.PersonWeaponPositionUpdater import PersonWeaponPositionUpdater
from game.engine.powerup.PowerupLogic import PowerupLogic
from game.engine.weapon.BulletLogic import BulletLogic
from game.engine.weapon.BulletPositionUpdater import BulletPositionUpdater
from game.engine.weapon.ExplosionLogic import ExplosionLogic
from game.engine.weapon.RayLogic import RayLogic
from game.engine.weapon.WeaponSelector import WeaponSelector
from game.model.snapshot.SnapshotBullet import SnapshotBullet
from game.model.weapon.Plasma import Plasma
from game.model.weapon.WeaponCollection import WeaponCollection


class GameStateSynchronizer:

    def __init__(
        self,
        clientPersonInitializer: ClientPersonInitializer,
        personTurnLogic: PersonTurnLogic,
        bulletLogic: BulletLogic,
        rayLogic: RayLogic,
        explosionLogic: ExplosionLogic,
        bulletPositionUpdater: BulletPositionUpdater,
        weaponSelector: WeaponSelector,
        personWeaponPositionUpdater: PersonWeaponPositionUpdater,
        powerupLogic: PowerupLogic,
    ):
        self.clientPersonInitializer = clientPersonInitializer
        self.personTurnLogic = personTurnLogic
        self.bulletLogic = bulletLogic
        self.rayLogic = rayLogic
        self.explosionLogic = explosionLogic
        self.bulletPositionUpdater = bulletPositionUpdater
        self.weaponSelector = weaponSelector
        self.personWeaponPositionUpdater = personWeaponPositionUpdater
        self.powerupLogic = powerupLogic

    def applySnapshotDiff(self, gameState, diff):
        if hasattr(diff, "addedEnemyIds"):
            for addedEnemyId in diff.addedEnemyIds:
                self.clientPersonInitializer.addPerson(gameState, addedEnemyId)

        if hasattr(diff, "removedEnemyIds"):
            for removedEnemyId in diff.removedEnemyIds:
                self.clientPersonInitializer.removePerson(gameState, removedEnemyId)

        if hasattr(diff, "person"):
            self.synchPerson(gameState, diff.person)

        if hasattr(diff, "player"):
            self.synchPerson(gameState, diff.player)

        if hasattr(diff, "enemies"):
            for enemy in diff.enemies:
                self.synchPerson(gameState, enemy)

        if hasattr(diff, "respawnedPerson"):
            for person in diff.respawnedPerson:
                self.synchRespawnedPerson(gameState, person)

        if hasattr(diff, "addedBullets"):
            for bullet in diff.addedBullets:
                self.synchAddedBullet(gameState, bullet)

        if hasattr(diff, "addedRays"):
            for ray in diff.addedRays:
                self.synchAddedRay(gameState, ray)

        if hasattr(diff, "removedRayIds"):
            for rayId in diff.removedRayIds:
                self.synchRemovedRay(gameState, rayId)

        if hasattr(diff, "addedPowerups"):
            for powerup in diff.addedPowerups:
                self.synchAddedPowerup(gameState, powerup)

        if hasattr(diff, "removedPowerupIds"):
            for powerupId in diff.removedPowerupIds:
                self.synchRemovedPowerup(gameState, powerupId)

        if hasattr(diff, "addedPersonBulletCollisions"):
            for bulletCollision in diff.addedPersonBulletCollisions:
                self.synchAddedPersonBulletCollision(gameState, bulletCollision)

        if hasattr(diff, "addedPersonRayCollisions"):
            for rayCollision in diff.addedPersonRayCollisions:
                self.synchAddedPersonRayCollision(gameState, rayCollision)

        if hasattr(diff, "addedPersonFrags"):
            for frags in diff.addedPersonFrags:
                self.synchAddedPersonFrags(gameState, frags)

        if hasattr(diff, "addedPersonDeaths"):
            for deaths in diff.addedPersonDeaths:
                self.synchAddedPersonDeaths(gameState, deaths)

    def synchPerson(self, gameState, diffPerson):
        sychedPerson = gameState.allPerson.getById(diffPerson.id)
        personItems = gameState.allPersonItems[sychedPerson]
        if hasattr(diffPerson, "centerPoint"):
            sychedPerson.hasMoved = True
            sychedPerson.moveNextPositionTo(diffPerson.centerPoint)
            sychedPerson.commitNextPosition()
        if hasattr(diffPerson, "yawRadians"):
            sychedPerson.yawRadians = diffPerson.yawRadians
        if hasattr(diffPerson, "pitchRadians"):
            sychedPerson.pitchRadians = diffPerson.pitchRadians
        if hasattr(diffPerson, "yawRadians") or hasattr(diffPerson, "pitchRadians"):
            self.personTurnLogic.calculateDirectionVectors(sychedPerson)
        if hasattr(diffPerson, "health"):
            sychedPerson.health = diffPerson.health
        if hasattr(diffPerson, "vest"):
            personItems.vest = diffPerson.vest
        if hasattr(diffPerson, "jumpingValue"):
            sychedPerson.jumpingValue = diffPerson.jumpingValue
        if hasattr(diffPerson, "selectedWeaponNumber"):
            weaponType = WeaponCollection.getWeaponTypeByNumber(diffPerson.selectedWeaponNumber)
            if personItems.hasWeaponByType(weaponType):
                self.weaponSelector.selectWeaponByType(sychedPerson, personItems, weaponType)

    def synchRespawnedPerson(self, gameState, diffPerson):
        sychedPerson = gameState.allPerson.getById(diffPerson.id)
        sychedPerson.moveNextPositionTo(diffPerson.centerPoint)
        self.personTurnLogic.orientToFrontNormal(sychedPerson, diffPerson.frontNormal)
        sychedPerson.commitNextPosition()
        gameState.bloodStains.clear()

    def synchAddedBullet(self, gameState, diffBullet):
        # TODO подумать как при рассинхроне обработать на клиенте тот путь
        # который пуля пролетела на сервере до передачи клиенту
        person = gameState.allPerson.getById(diffBullet.personId)
        personItems = gameState.allPersonItems[person]
        weaponNumber, isLeftHandWeapon, isCharged, isAltBullet = SnapshotBullet.readWeaponInfo(diffBullet.weaponInfo)
        diffBulletWeaponType = WeaponCollection.getWeaponTypeByNumber(weaponNumber)
        if not personItems.hasWeaponByType(diffBulletWeaponType):
            return
        if personItems.getCurrentWeaponType() != diffBulletWeaponType:
            self.weaponSelector.setWeaponByType(personItems, diffBulletWeaponType)
            self.personWeaponPositionUpdater.updateForPerson(person, personItems)
        if diffBulletWeaponType.defaultCount == 2:
            if isLeftHandWeapon:
                personItems.setLeftHandWeaponAsCurrent()
            else:
                personItems.setRightHandWeaponAsCurrent()
        if isCharged:
            personItems.currentWeapon.isCharged = True
        if not isAltBullet:
            newBullet = self.bulletLogic.makeBullet(gameState, person, personItems.currentWeapon, diffBullet.id, diffBullet.randomSeed)
            personItems.currentWeapon.bulletsCount -= 1
        else:
            newBullet = self.bulletLogic.makeAltBullet(gameState, person, personItems.currentWeapon, diffBullet.id, diffBullet.randomSeed)
            personItems.currentWeapon.altBulletsCount -= 1
        newBullet.direction = diffBullet.direction.copy()
        self.bulletPositionUpdater.moveBulletNextPositionTo(gameState, newBullet, diffBullet.position)
        self.bulletPositionUpdater.commitBulletNextPosition(newBullet, gameState.visibilityTree)
        diffBulletWeapon = personItems.getWeaponByTypeOrNone(diffBulletWeaponType)
        gameState.updateStatistic.firedWeapons.append((person, diffBulletWeapon, newBullet))

    def synchAddedRay(self, gameState, diffRay):
        person = gameState.allPerson.getById(diffRay.personId)
        personItems = gameState.allPersonItems[person]
        weapon = personItems.getWeaponByTypeOrNone(Plasma)
        if weapon is None:
            return
        if personItems.currentWeapon != weapon:
            self.weaponSelector.setWeaponByType(personItems, type(weapon))
            self.personWeaponPositionUpdater.updateForPerson(person, personItems)
        self.rayLogic.makeRay(gameState, person, weapon, diffRay.id)
        personItems.currentWeapon.bulletsCount -= 1

    def synchRemovedRay(self, gameState, diffRayId):
        ray = gameState.rays.getByIdOrNone(diffRayId)
        if ray is not None:
            self.rayLogic.removeRay(gameState, ray)

    def synchAddedPowerup(self, gameState, diffPowerup):
        self.powerupLogic.makePowerupFromKind(gameState, diffPowerup.id, diffPowerup.kind, diffPowerup.position)

    def synchRemovedPowerup(self, gameState, diffPowerupId):
        powerup = gameState.powerups.getByIdOrNone(diffPowerupId)
        if powerup is not None:
            self.powerupLogic.removePowerup(gameState, powerup)

    def synchAddedPersonBulletCollision(self, gameState, diffBulletCollision):
        aliveOrRemovedBullet = gameState.removedBullets.getByIdOrNone(diffBulletCollision.bulletId) or gameState.bullets.getByIdOrNone(
            diffBulletCollision.bulletId
        )
        if aliveOrRemovedBullet is None:
            return
        damagedPerson = gameState.allPerson.getById(diffBulletCollision.damagedPersonId)
        gameState.collisionData.personBullet[damagedPerson] = aliveOrRemovedBullet
        aliveOrRemovedBullet.damagedObject = damagedPerson
        aliveOrRemovedBullet.currentPosition = diffBulletCollision.collisionPoint.copy()
        aliveOrRemovedBullet.nextPosition = aliveOrRemovedBullet.currentPosition
        if aliveOrRemovedBullet.isAlive:
            gameState.bullets.remove(aliveOrRemovedBullet)
            self.bulletLogic.removeFromVisibilityLevelSegment(aliveOrRemovedBullet)
        else:
            gameState.removedBullets.remove(aliveOrRemovedBullet)
        self.explosionLogic.makeExplosion(gameState, aliveOrRemovedBullet)

    def synchAddedPersonRayCollision(self, gameState, diffRayCollision):
        ray = gameState.rays.getByIdOrNone(diffRayCollision.rayId)
        if ray is None:
            return
        damagedPerson = gameState.allPerson.getById(diffRayCollision.damagedPersonId)
        gameState.collisionData.personRay[damagedPerson] = ray
        ray.damagedObject = damagedPerson
        ray.stopOnPosition(diffRayCollision.collisionPoint)

    def synchAddedPersonFrags(self, gameState, diffFrags):
        person = gameState.allPerson.getById(diffFrags.personId)
        gameState.personFragStatistic[person].frags = diffFrags.value

    def synchAddedPersonDeaths(self, gameState, diffDeaths):
        person = gameState.allPerson.getById(diffDeaths.personId)
        gameState.personFragStatistic[person].deaths = diffDeaths.value
