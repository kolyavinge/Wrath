import numpy
from openal.al import *

from game.vox.lib.AudioSource import AudioSource


class AudioSourceLoader:

    def load(self, audioBuffer):
        sourceId = ctypes.c_uint()
        alGenSources(1, sourceId)
        alSourcef(sourceId, AL_PITCH, numpy.float32(1))
        alSourcef(sourceId, AL_GAIN, numpy.float32(1))
        alSource3f(sourceId, AL_POSITION, numpy.float32(0), numpy.float32(0), numpy.float32(0))
        alSource3f(sourceId, AL_VELOCITY, numpy.float32(0), numpy.float32(0), numpy.float32(0))
        alSourcei(sourceId, AL_LOOPING, numpy.int32(0))
        alSourceQueueBuffers(sourceId, 1, audioBuffer.id)

        return AudioSource(sourceId)
