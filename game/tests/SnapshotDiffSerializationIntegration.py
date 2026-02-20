import unittest

from numpy import float32

from game.calc.Vector3 import Vector3
from game.lib.BinaryReader import BinaryReader
from game.lib.BinaryWriter import BinaryWriter
from game.model.snapshot.SnapshotBullet import SnapshotBullet
from game.model.snapshot.SnapshotBulletCollision import SnapshotBulletCollision
from game.model.snapshot.SnapshotDebris import SnapshotDebris
from game.model.snapshot.SnapshotDiff import SnapshotDiff
from game.model.snapshot.SnapshotFragStatistic import SnapshotFragStatistic
from game.model.snapshot.SnapshotPerson import SnapshotPerson
from game.model.snapshot.SnapshotPlayer import SnapshotPlayer
from game.model.snapshot.SnapshotPowerup import SnapshotPowerup
from game.model.snapshot.SnapshotRay import SnapshotRay
from game.model.snapshot.SnapshotRayCollision import SnapshotRayCollision
from game.model.snapshot.SnapshotRespawnedPerson import SnapshotRespawnedPerson


class SnapshotDiffSerializationIntegration(unittest.TestCase):

    def test(self):
        diff = SnapshotDiff()
        diff.addedPersonIds = [1, 2, 3, 4, 5]
        diff.person = SnapshotPerson.make(1, Vector3(float32(3.2), float32(-6.9), float32(44.2)), 1.5, -1.5, 10)
        diff.player = SnapshotPlayer.make(12, 85)
        diff.respawnedPerson = [SnapshotRespawnedPerson.make(10, Vector3(float32(3.2), float32(-6.9), float32(44.2)))]
        diff.enemies = [
            SnapshotPerson.make(10, Vector3(float32(3.2), float32(-6.9), float32(44.2)), 2.5, -2.5, 50),
            SnapshotPerson.make(20, Vector3(float32(3.2), float32(-6.9), float32(44.2)), 2.0, -2.0, 60),
        ]
        diff.addedBullets = [
            SnapshotBullet.make(
                12, 1, 2, Vector3(float32(3.2), float32(-6.9), float32(44.2)), Vector3(float32(3.2), float32(-6.9), float32(44.2)), None
            ),
            SnapshotBullet.make(
                12, 1, 4, Vector3(float32(3.2), float32(-6.9), float32(44.2)), Vector3(float32(3.2), float32(-6.9), float32(44.2)), 42789
            ),
        ]
        diff.addedRays = [SnapshotRay.make(1, 2)]
        diff.removedRayIds = [1, 2, 3]
        diff.addedPowerups = [SnapshotPowerup.make(2, 4, Vector3(float32(3.2), float32(-6.9), 0.15487157943974397845))]
        diff.removedPowerupIds = [4, 5, 6]
        diff.pickedupPowerupIds = [7, 8, 9]
        diff.addedPersonBulletCollisions = [SnapshotBulletCollision.make(2, 4, Vector3(float32(3.2), float32(-6.9), float32(44.2)))]
        diff.addedPersonRayCollisions = [SnapshotRayCollision.make(4, 2, Vector3(float32(3.2), float32(-6.9), float32(44.2)))]
        diff.addedPersonFrags = [SnapshotFragStatistic.make(4, 9)]
        diff.addedPersonDeaths = [SnapshotFragStatistic.make(5, 11)]

        writer = BinaryWriter(1024)
        writer.init()
        diff.toBytes(writer)
        bytes, writtenBytesCount = writer.getBytes()
        print("diff byte size =", writtenBytesCount)

        reader = BinaryReader()
        reader.init(bytes)
        diffDeser = SnapshotDiff.fromBytes(reader)
        self.assertEqual(writtenBytesCount, reader.readedBytesCount)

        self.assertEqual(diffDeser.addedPersonIds, diff.addedPersonIds)
        self.assertEqual(diffDeser.person, diff.person)
        self.assertEqual(diffDeser.player, diff.player)
        self.assertEqual(diffDeser.enemies, diff.enemies)
        self.assertEqual(diffDeser.respawnedPerson, diff.respawnedPerson)
        self.assertEqual(diffDeser.addedBullets, diff.addedBullets)
        self.assertEqual(diffDeser.addedRays, diff.addedRays)
        self.assertEqual(diffDeser.removedRayIds, diff.removedRayIds)
        self.assertEqual(diffDeser.addedPowerups, diff.addedPowerups)
        self.assertEqual(diffDeser.removedPowerupIds, diff.removedPowerupIds)
        self.assertEqual(diffDeser.pickedupPowerupIds, diff.pickedupPowerupIds)
        self.assertEqual(diffDeser.addedPersonBulletCollisions, diff.addedPersonBulletCollisions)
        self.assertEqual(diffDeser.addedPersonRayCollisions, diff.addedPersonRayCollisions)
        self.assertEqual(diffDeser.addedPersonFrags, diff.addedPersonFrags)
        self.assertEqual(diffDeser.addedPersonDeaths, diff.addedPersonDeaths)
