from game.model.person.Enemy import Enemy
from game.model.person.Player import Player
from game.model.snapshot.ClientSnapshot import ClientSnapshot
from game.model.snapshot.ServerSnapshot import ServerSnapshot
from game.model.snapshot.SnapshotBullet import SnapshotBullet
from game.model.snapshot.SnapshotBulletCollision import SnapshotBulletCollision
from game.model.snapshot.SnapshotDebris import SnapshotDebris
from game.model.snapshot.SnapshotPerson import SnapshotPerson
from game.model.snapshot.SnapshotPowerup import SnapshotPowerup
from game.model.snapshot.SnapshotRay import SnapshotRay
from game.model.snapshot.SnapshotRayCollision import SnapshotRayCollision
from game.model.weapon.Debris import Debris
from game.model.weapon.WeaponCollection import WeaponCollection


class SnapshotFactory:

    def makeClientSnapshot(self, clientGameState):
        snapshot = ClientSnapshot()
        snapshot.player = self.makeSnapshotPerson(clientGameState.player)
        snapshot.bullets = {
            bullet.id: self.makeSnapshotBullet(bullet)
            for bullet in clientGameState.bullets
            if bullet.weapon is not None and type(bullet.ownerPerson) == Player
        }
        snapshot.debris = {
            debris.id: self.makeSnapshotDebris(debris)
            for debris in clientGameState.bullets
            if isinstance(debris, Debris) and type(debris.ownerPerson) == Player
        }
        snapshot.rays = {ray.id: self.makeSnapshotRay(ray) for ray in clientGameState.rays if type(ray.ownerPerson) == Player}
        snapshot.notPickedupPowerupIds = set([powerup.id for powerup in clientGameState.powerups])

        return snapshot

    def makeServerSnapshot(self, serverGameState):
        snapshot = ServerSnapshot()
        snapshot.enemies = [self.makeSnapshotPerson(enemy) for enemy in serverGameState.enemies]
        snapshot.bullets = {bullet.id: self.makeSnapshotBullet(bullet) for bullet in serverGameState.bullets if type(bullet.ownerPerson) == Enemy}
        snapshot.debris = {
            debris.id: self.makeSnapshotDebris(debris)
            for debris in serverGameState.bullets
            if isinstance(debris, Debris) and type(debris.ownerPerson) == Enemy
        }
        snapshot.rays = {ray.id: self.makeSnapshotRay(ray) for ray in serverGameState.rays if type(ray.ownerPerson) == Enemy}
        snapshot.powerups = {powerup.id: self.makeSnapshotPowerup(powerup) for powerup in serverGameState.powerups}
        snapshot.personBulletCollisions = {
            collisionId: self.makeSnapshotBulletCollision(damagedPerson, bullet)
            for collisionId, damagedPerson, bullet in serverGameState.reservedCollisionData.personBullet
        }
        snapshot.personRayCollisions = {
            collisionId: self.makeSnapshotRayCollision(damagedPerson, ray)
            for collisionId, damagedPerson, ray in serverGameState.reservedCollisionData.personRay
        }

        return snapshot

    def makeSnapshotPerson(self, person):
        snapshotPerson = SnapshotPerson()
        snapshotPerson.id = person.id
        snapshotPerson.centerPoint = person.currentCenterPoint.copy()
        snapshotPerson.yawRadians = person.yawRadians
        snapshotPerson.pitchRadians = person.pitchRadians
        snapshotPerson.health = person.health

        return snapshotPerson

    def makeSnapshotBullet(self, bullet):
        snapshotBullet = SnapshotBullet()
        snapshotBullet.id = bullet.id
        snapshotBullet.personId = bullet.ownerPerson.id
        snapshotBullet.weaponNumber = WeaponCollection.getWeaponNumberByType(type(bullet.weapon))
        snapshotBullet.position = bullet.prevCurrentPosition.copy()
        snapshotBullet.direction = bullet.direction.copy()
        # snapshotBullet.velocityValue = bullet.velocityValue

        return snapshotBullet

    def makeSnapshotDebris(self, debris):
        snapshotDebris = SnapshotDebris()
        snapshotDebris.id = debris.id
        snapshotDebris.personId = debris.ownerPerson.id
        snapshotDebris.position = debris.currentPosition.copy()
        snapshotDebris.direction = debris.direction.copy()

        return snapshotDebris

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
