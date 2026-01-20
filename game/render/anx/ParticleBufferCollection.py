class ParticleBufferCollection:

    def __init__(self, bufferInitializer, extraInitData=None):
        self.bufferInitializer = bufferInitializer
        self.extraInitData = extraInitData
        self.buffers = {}

    def getBufferFor(self, item):
        if item in self.buffers:
            return self.buffers[item]
        else:
            buffer = self.findFreeBufferOrNone()
            if buffer is None:
                buffer = self.bufferInitializer.makeEmpty(item)
            self.bufferInitializer.init(buffer, item, self.extraInitData)
            self.buffers[item] = buffer

            return buffer

    def findFreeBufferOrNone(self):
        oldItemToRemove = None
        freeBuffer = None
        for item, buffer in self.buffers.items():
            if not item.isVisible:
                oldItemToRemove = item
                freeBuffer = buffer
                break

        if oldItemToRemove is not None:
            self.buffers.pop(oldItemToRemove)

        return freeBuffer
