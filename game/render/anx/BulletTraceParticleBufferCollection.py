class BulletTraceParticleBufferCollection:

    def __init__(self, bufferInitializer):
        self.bufferInitializer = bufferInitializer
        self.buffers = {}

    def getBufferForTrace(self, trace):
        if trace in self.buffers:
            return self.buffers[trace]
        else:
            buffer = self.findFreeBufferOrNone()
            if buffer is None:
                buffer = self.bufferInitializer.makeEmpty(trace)
            self.bufferInitializer.init(buffer, trace)
            self.buffers[trace] = buffer

            return buffer

    def findFreeBufferOrNone(self):
        oldTraceToRemove = None
        freeBuffer = None
        for trace, buffer in self.buffers.items():
            if not trace.isVisible:
                oldTraceToRemove = trace
                freeBuffer = buffer
                break

        if oldTraceToRemove is not None:
            self.buffers.pop(oldTraceToRemove)

        return freeBuffer
