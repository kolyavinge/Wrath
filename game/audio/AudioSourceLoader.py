from openal.al import *

from game.audio.AudioSource import AudioSource


class AudioSourceLoader:

    def load(self, audioBuffer):
        sourceId = ctypes.c_uint()
        alGenSources(1, sourceId)
        alSourcef(sourceId, AL_PITCH, 1)
        alSourcef(sourceId, AL_GAIN, 1)
        alSource3f(sourceId, AL_POSITION, 0, 0, 0)
        alSource3f(sourceId, AL_VELOCITY, 0, 0, 0)
        alSourcei(sourceId, AL_LOOPING, 0)
        alSourceQueueBuffers(sourceId, 1, audioBuffer.id)

        return AudioSource(sourceId)
