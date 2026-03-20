import struct


class BinaryWriter:

    def __init__(self, bufferSizeBytes):
        self.byteBuffer = bytearray(bufferSizeBytes)

    def init(self):
        self.writtenBytesCount = 0

    def write(self, formatMask, *values):
        formatMask = "=" + formatMask
        struct.pack_into(formatMask, self.byteBuffer, self.writtenBytesCount, *values)
        self.writtenBytesCount += struct.calcsize(formatMask)

    def getBytes(self):
        return (self.byteBuffer, self.writtenBytesCount)
