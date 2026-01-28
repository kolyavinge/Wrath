from game.model.person.Player import Player
from game.model.snapshot.Bullet import Bullet
from game.model.snapshot.Person import Person
from game.model.weapon.WeaponCollection import WeaponCollection
from game.network.Snapshot import Snapshot


class SnapshotFactory:

    def makeClientSnapshot(self, clientGameState):
        # TODO сделать разделение на ClientSnapshot и ServerSnapshot
        snapshot = Snapshot()
        snapshot.player = self.makeSnapshotPersonFor(clientGameState.player)
        snapshot.bullets = [self.makeSnapshotBulletFor(bullet) for bullet in clientGameState.bullets if type(bullet.ownerPerson) == Player]

        return snapshot

    def makeServerSnapshot(self, serverGameState):
        snapshot = Snapshot()
        snapshot.enemies = [self.makeSnapshotPersonFor(enemy) for enemy in serverGameState.enemies]

        return snapshot

    def makeSnapshotPersonFor(self, person):
        snapshotPerson = Person()
        snapshotPerson.id = person.id
        snapshotPerson.centerPoint = person.currentCenterPoint.copy()
        snapshotPerson.yawRadians = person.yawRadians
        snapshotPerson.pitchRadians = person.pitchRadians

        return snapshotPerson

    def makeSnapshotBulletFor(self, bullet):
        snapshotBullet = Bullet()
        snapshotBullet.id = bullet.id
        if bullet.ownerPerson is not None:  # if bullet is debris -> ownerPerson is None
            snapshotBullet.personId = bullet.ownerPerson.id
        if bullet.weapon is not None:  # if bullet is debris -> weapon is None
            snapshotBullet.weaponNumber = WeaponCollection.getWeaponNumberByType(type(bullet.weapon))
        snapshotBullet.position = bullet.prevCurrentPosition.copy()
        snapshotBullet.direction = bullet.direction.copy()
        # snapshotBullet.velocityValue = bullet.velocityValue

        return snapshotBullet
