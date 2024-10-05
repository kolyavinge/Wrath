import wave


class AudioFile:

    def load(self, filePath):
        file = wave.open(filePath, "r")
        self.channelsCount = file.getnchannels()
        self.bitsPerSample = 8 * file.getsampwidth()
        self.sampleRate = file.getframerate()
        self.soundData = file.readframes(file.getnframes())
        self.soundDataSizeInBytes = len(self.soundData)
        file.close()
