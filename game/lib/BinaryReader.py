import struct


class BinaryReader:

    def init(self, bytes):
        self.bytes = bytes
        self.readedBytesCount = 0

    def read(self, formatMask):
        formatMask = "=" + formatMask
        value = struct.unpack_from(formatMask, self.bytes, self.readedBytesCount)
        self.readedBytesCount += struct.calcsize(formatMask)
        # unpack tuple if one argument in formatMask (two after concat)
        if len(formatMask) == 2:
            (value,) = value

        return value
