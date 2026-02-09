import unittest

from game.lib.BinaryReader import BinaryReader
from game.lib.BinaryWriter import BinaryWriter


class BinaryReaderWriterIntegration(unittest.TestCase):

    def testOneByte(self):
        writer = BinaryWriter(1)
        writer.init()
        writer.write("b", 123)
        bytes, count = writer.getBytes()
        self.assertEqual(count, 1)

        reader = BinaryReader()
        reader.init(bytes)
        v = reader.read("b")
        self.assertEqual(v, 123)

    def testTwoBytes(self):
        writer = BinaryWriter(2)
        writer.init()
        writer.write("bb", 123, 124)
        bytes, count = writer.getBytes()
        self.assertEqual(count, 2)

        reader = BinaryReader()
        reader.init(bytes)
        (v1, v2) = reader.read("bb")
        self.assertEqual(v1, 123)
        self.assertEqual(v2, 124)

    def testOneInt(self):
        writer = BinaryWriter(4)
        writer.init()
        writer.write("i", 1000000)
        bytes, count = writer.getBytes()
        self.assertEqual(count, 4)

        reader = BinaryReader()
        reader.init(bytes)
        v = reader.read("i")
        self.assertEqual(v, 1000000)

    def testOneFloat(self):
        writer = BinaryWriter(4)
        writer.init()
        writer.write("f", 12.5)
        bytes, count = writer.getBytes()
        self.assertEqual(count, 4)

        reader = BinaryReader()
        reader.init(bytes)
        v = reader.read("f")
        self.assertEqual(v, 12.5)

    def testManyValues(self):
        writer = BinaryWriter(17)
        writer.init()
        writer.write("Bifif", 128, 12345678, 12.5, 55, 3.5)
        bytes, count = writer.getBytes()
        self.assertEqual(count, 17)

        reader = BinaryReader()
        reader.init(bytes)
        (v1, v2, v3, v4, v5) = reader.read("Bifif")
        self.assertEqual(v1, 128)
        self.assertEqual(v2, 12345678)
        self.assertEqual(v3, 12.5)
        self.assertEqual(v4, 55)
        self.assertEqual(v5, 3.5)

    def testManyValuesReadByOne(self):
        writer = BinaryWriter(17)
        writer.init()
        writer.write("Bifif", 128, 12345678, 12.5, 55, 3.5)
        bytes, count = writer.getBytes()
        self.assertEqual(count, 17)

        reader = BinaryReader()
        reader.init(bytes)
        v1 = reader.read("B")
        self.assertEqual(v1, 128)
        self.assertEqual(reader.readedBytesCount, 1)

        v2 = reader.read("i")
        self.assertEqual(v2, 12345678)
        self.assertEqual(reader.readedBytesCount, 5)

        v3 = reader.read("f")
        self.assertEqual(v3, 12.5)
        self.assertEqual(reader.readedBytesCount, 9)

        v4 = reader.read("i")
        self.assertEqual(v4, 55)
        self.assertEqual(reader.readedBytesCount, 13)

        v5 = reader.read("f")
        self.assertEqual(v5, 3.5)
        self.assertEqual(reader.readedBytesCount, 17)
