from game.model.person.Enemy import Enemy
from game.model.person.Player import Player
from game.model.snapshot.ClientSnapshot import ClientSnapshot
from game.model.snapshot.ServerSnapshot import ServerSnapshot
from game.model.snapshot.SnapshotBullet import SnapshotBullet
from game.model.snapshot.SnapshotPerson import SnapshotPerson
from game.model.snapshot.SnapshotPowerup import SnapshotPowerup
from game.model.weapon.WeaponCollection import WeaponCollection


class SnapshotFactory:

    def makeClientSnapshot(self, clientGameState):
        snapshot = ClientSnapshot()
        snapshot.player = self.makeSnapshotPerson(clientGameState.player)
        snapshot.bullets = [self.makeSnapshotBullet(bullet) for bullet in clientGameState.bullets if type(bullet.ownerPerson) == Player]
        snapshot.notPickedupPowerupIds = set([powerup.id for powerup in clientGameState.powerups])

        return snapshot

    def makeServerSnapshot(self, serverGameState):
        snapshot = ServerSnapshot()
        snapshot.enemies = [self.makeSnapshotPerson(enemy) for enemy in serverGameState.enemies]
        snapshot.bullets = [self.makeSnapshotBullet(bullet) for bullet in serverGameState.bullets if type(bullet.ownerPerson) == Enemy]
        snapshot.powerups = {powerup.id: self.makeSnapshotPowerup(powerup) for powerup in serverGameState.powerups}

        return snapshot

    def makeSnapshotPerson(self, person):
        snapshotPerson = SnapshotPerson()
        snapshotPerson.id = person.id
        snapshotPerson.centerPoint = person.currentCenterPoint.copy()
        snapshotPerson.yawRadians = person.yawRadians
        snapshotPerson.pitchRadians = person.pitchRadians

        return snapshotPerson

    def makeSnapshotBullet(self, bullet):
        snapshotBullet = SnapshotBullet()
        snapshotBullet.id = bullet.id
        if bullet.ownerPerson is not None:  # if bullet is debris -> ownerPerson is None
            snapshotBullet.personId = bullet.ownerPerson.id
        if bullet.weapon is not None:  # if bullet is debris -> weapon is None
            snapshotBullet.weaponNumber = WeaponCollection.getWeaponNumberByType(type(bullet.weapon))
        snapshotBullet.position = bullet.prevCurrentPosition.copy()
        snapshotBullet.direction = bullet.direction.copy()
        # snapshotBullet.velocityValue = bullet.velocityValue

        return snapshotBullet

    def makeSnapshotPowerup(self, powerup):
        snapshotPowerup = SnapshotPowerup()
        snapshotPowerup.id = powerup.id
        snapshotPowerup.kind = powerup.kind
        snapshotPowerup.position = powerup.pickupPosition

        return snapshotPowerup
