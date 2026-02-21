from game.model.person.PersonStates import LifeCycle
from game.model.person.Player import Player
from game.model.snapshot.ClientSnapshot import ClientSnapshot
from game.model.snapshot.ServerSnapshot import ServerSnapshot
from game.model.snapshot.SnapshotBullet import SnapshotBullet, WeaponInfoExtraBit
from game.model.snapshot.SnapshotBulletCollision import SnapshotBulletCollision
from game.model.snapshot.SnapshotFragStatistic import SnapshotFragStatistic
from game.model.snapshot.SnapshotPerson import SnapshotPerson
from game.model.snapshot.SnapshotPlayer import SnapshotPlayer
from game.model.snapshot.SnapshotPowerup import SnapshotPowerup
from game.model.snapshot.SnapshotRay import SnapshotRay
from game.model.snapshot.SnapshotRayCollision import SnapshotRayCollision
from game.model.snapshot.SnapshotRespawnedPerson import SnapshotRespawnedPerson
from game.model.weapon.WeaponCollection import WeaponCollection


class SnapshotFactory:

    def makeClientSnapshot(self, clientGameState):
        snapshot = ClientSnapshot()
        snapshot.person = self.makeSnapshotPerson(clientGameState.player)
        snapshot.bullets = {
            bullet.id: self.makeSnapshotBullet(bullet, clientGameState.allPersonItems)
            for bullet in clientGameState.bullets
            if bullet.weapon is not None and type(bullet.ownerPerson) == Player
        }
        snapshot.rays = {ray.id: self.makeSnapshotRay(ray) for ray in clientGameState.rays if type(ray.ownerPerson) == Player}
        snapshot.notPickedupPowerupIds = set([powerup.id for powerup in clientGameState.powerups])

        return snapshot

    def makeServerSnapshot(self, serverGameState):
        snapshot = ServerSnapshot()
        snapshot.players = {player.id: self.makeSnapshotPlayer(player) for player in serverGameState.players}
        snapshot.allPerson = {person.id: self.makeSnapshotPerson(person) for person in serverGameState.allPerson}
        snapshot.respawnedPerson = set(
            [self.makeSnapshotRespawnedPerson(person) for person in serverGameState.allPerson if person.lifeCycle == LifeCycle.respawned]
        )
        snapshot.bullets = {
            bullet.id: self.makeSnapshotBullet(bullet, serverGameState.allPersonItems)
            for bullet in serverGameState.bullets
            if bullet.weapon is not None
        }
        snapshot.rays = {ray.id: self.makeSnapshotRay(ray) for ray in serverGameState.rays}
        snapshot.powerups = {powerup.id: self.makeSnapshotPowerup(powerup) for powerup in serverGameState.powerups}
        snapshot.personBulletCollisions = {
            collisionId: self.makeSnapshotBulletCollision(damagedPerson, bullet)
            for collisionId, damagedPerson, bullet in serverGameState.reservedCollisionData.personBullet
        }
        snapshot.personRayCollisions = {
            collisionId: self.makeSnapshotRayCollision(damagedPerson, ray)
            for collisionId, damagedPerson, ray in serverGameState.reservedCollisionData.personRay
        }
        snapshot.personFrags = set([self.makeSnapshotFragStatistic(person, stat) for person, stat in serverGameState.personFragStatistic.items()])
        snapshot.personDeaths = set([self.makeSnapshotDeathStatistic(person, stat) for person, stat in serverGameState.personFragStatistic.items()])

        return snapshot

    def makeSnapshotPerson(self, person):
        snapshotPerson = SnapshotPerson()
        snapshotPerson.id = person.id
        snapshotPerson.centerPoint = person.currentCenterPoint.copy()
        snapshotPerson.yawRadians = person.yawRadians
        snapshotPerson.pitchRadians = person.pitchRadians
        snapshotPerson.health = person.health

        return snapshotPerson

    def makeSnapshotPlayer(self, player):
        snapshotPlayer = SnapshotPlayer()
        snapshotPlayer.id = player.id
        snapshotPlayer.health = player.health

        return snapshotPlayer

    def makeSnapshotRespawnedPerson(self, person):
        snapshotRespawnedPerson = SnapshotRespawnedPerson()
        snapshotRespawnedPerson.id = person.id
        snapshotRespawnedPerson.centerPoint = person.currentCenterPoint.copy()

        return snapshotRespawnedPerson

    def makeSnapshotBullet(self, bullet, allPersonItems):
        snapshotBullet = SnapshotBullet()
        snapshotBullet.id = bullet.id
        snapshotBullet.personId = bullet.ownerPerson.id
        snapshotBullet.weaponInfo = WeaponCollection.getWeaponNumberByType(type(bullet.weapon))
        if bullet.weapon.defaultCount == 2:
            personItems = allPersonItems[bullet.ownerPerson]
            if bullet.weapon == personItems.leftHandWeapon:
                snapshotBullet.weaponInfo |= WeaponInfoExtraBit.leftHandWeapon
        snapshotBullet.position = bullet.prevCurrentPosition.copy()
        snapshotBullet.direction = bullet.direction.copy()
        snapshotBullet.randomSeed = bullet.randomSeed
        # snapshotBullet.velocityValue = bullet.velocityValue

        return snapshotBullet

    def makeSnapshotRay(self, ray):
        snapshotRay = SnapshotRay()
        snapshotRay.id = ray.id
        snapshotRay.personId = ray.ownerPerson.id

        return snapshotRay

    def makeSnapshotPowerup(self, powerup):
        snapshotPowerup = SnapshotPowerup()
        snapshotPowerup.id = powerup.id
        snapshotPowerup.kind = powerup.kind
        snapshotPowerup.position = powerup.pickupPosition.copy()

        return snapshotPowerup

    def makeSnapshotBulletCollision(self, damagedPerson, bullet):
        snapshotBulletCollision = SnapshotBulletCollision()
        snapshotBulletCollision.damagedPersonId = damagedPerson.id
        snapshotBulletCollision.bulletId = bullet.id
        snapshotBulletCollision.collisionPoint = bullet.currentPosition.copy()

        return snapshotBulletCollision

    def makeSnapshotRayCollision(self, damagedPerson, ray):
        snapshotRayCollision = SnapshotRayCollision()
        snapshotRayCollision.damagedPersonId = damagedPerson.id
        snapshotRayCollision.rayId = ray.id
        snapshotRayCollision.collisionPoint = ray.currentPosition.copy()

        return snapshotRayCollision

    def makeSnapshotFragStatistic(self, person, stat):
        snapshotFragStatistic = SnapshotFragStatistic()
        snapshotFragStatistic.personId = person.id
        snapshotFragStatistic.value = stat.frags

        return snapshotFragStatistic

    def makeSnapshotDeathStatistic(self, person, stat):
        snapshotFragStatistic = SnapshotFragStatistic()
        snapshotFragStatistic.personId = person.id
        snapshotFragStatistic.value = stat.deaths

        return snapshotFragStatistic
