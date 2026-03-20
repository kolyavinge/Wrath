class AudioSourcePool:

    def __init__(self, makeAudioSourceFunc):
        self.makeAudioSourceFunc = makeAudioSourceFunc
        self.sources = []

    def getAudioSource(self):
        source = self.findFreeSourceOrNone()
        if source is None:
            source = self.makeAudioSourceFunc()
            self.sources.append(source)

        return source

    def findFreeSourceOrNone(self):
        for source in self.sources:
            if not source.isPlaying():
                return source

        return None

    def release(self):
        for source in self.sources:
            source.release()
