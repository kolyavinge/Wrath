import unittest

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


class SnapshotDiffSerializationIntegration(unittest.TestCase):

    def test(self):
        diff = SnapshotDiff()
        diff.player = SnapshotPerson(1, Vector3(0, 0, 0), 1.5, -1.5, 10)
        diff.players = [SnapshotPlayer(12, 85)]
        diff.enemies = [SnapshotPerson(10, Vector3(0, 0, 0), 2.5, -2.5, 50), SnapshotPerson(20, Vector3(0, 0, 0), 2.0, -2.0, 60)]
        diff.addedBullets = [SnapshotBullet(12, 1, 2, Vector3(0, 0, 0), Vector3(0, 0, 0))]
        diff.addedDebris = [SnapshotDebris(5, 2, Vector3(0, 0, 0), Vector3(0, 0, 0))]
        diff.addedRays = [SnapshotRay(1, 2)]
        diff.removedRayIds = [1, 2, 3]
        diff.addedPowerups = [SnapshotPowerup(2, 4, Vector3(0, 0, 0))]
        diff.removedPowerupIds = [4, 5, 6]
        diff.pickedupPowerupIds = [7, 8, 9]
        diff.addedPersonBulletCollisions = [SnapshotBulletCollision(2, 4, Vector3(0, 0, 0))]
        diff.addedPersonRayCollisions = [SnapshotRayCollision(4, 2, Vector3(0, 0, 0))]
        diff.addedPersonFrags = [SnapshotFragStatistic(4, 9)]
        diff.addedPersonDeaths = [SnapshotFragStatistic(5, 11)]

        writer = BinaryWriter(1024)
        writer.init()
        diff.toBytes(writer)
        bytes, writtenBytesCount = writer.getBytes()
        print("diff byte size =", writtenBytesCount)

        reader = BinaryReader()
        reader.init(bytes)
        diffDeser = SnapshotDiff.fromBytes(reader)
        self.assertEqual(writtenBytesCount, reader.readedBytesCount)

        self.assertEqual(diffDeser.player, diff.player)
        self.assertEqual(diffDeser.players, diff.players)
        self.assertEqual(diffDeser.enemies, diff.enemies)
        self.assertEqual(diffDeser.addedBullets, diff.addedBullets)
        self.assertEqual(diffDeser.addedDebris, diff.addedDebris)
        self.assertEqual(diffDeser.addedRays, diff.addedRays)
        self.assertEqual(diffDeser.removedRayIds, diff.removedRayIds)
        self.assertEqual(diffDeser.addedPowerups, diff.addedPowerups)
        self.assertEqual(diffDeser.removedPowerupIds, diff.removedPowerupIds)
        self.assertEqual(diffDeser.pickedupPowerupIds, diff.pickedupPowerupIds)
        self.assertEqual(diffDeser.addedPersonBulletCollisions, diff.addedPersonBulletCollisions)
        self.assertEqual(diffDeser.addedPersonRayCollisions, diff.addedPersonRayCollisions)
        self.assertEqual(diffDeser.addedPersonFrags, diff.addedPersonFrags)
        self.assertEqual(diffDeser.addedPersonDeaths, diff.addedPersonDeaths)
