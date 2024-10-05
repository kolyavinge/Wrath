from openal.al import *

from game.audio.AudioBuffer import AudioBuffer
from game.audio.AudioFile import AudioFile


class AudioBufferLoader:

    def load(self, filePath):
        audioFile = AudioFile()
        audioFile.load(filePath)
        bufferId = ctypes.c_uint()
        alGenBuffers(1, bufferId)
        format = self.getFormat(audioFile)
        alBufferData(bufferId, format, audioFile.soundData, audioFile.soundDataSizeInBytes, audioFile.sampleRate)

        return AudioBuffer(bufferId)

    def getFormat(self, audioFile):
        formats = {
            (1, 8): AL_FORMAT_MONO8,
            (2, 8): AL_FORMAT_STEREO8,
            (1, 16): AL_FORMAT_MONO16,
            (2, 16): AL_FORMAT_STEREO16,
        }

        return formats[(audioFile.channelsCount, audioFile.bitsPerSample)]


def makeAudioBufferLoader(resolver):
    return AudioBufferLoader()
