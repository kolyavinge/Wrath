import numpy
from openal.al import *


class AudioSource:

    def __init__(self, id):
        self.id = id

    def isPlaying(self):
        state = ctypes.c_long()
        alGetSourcei(self.id, AL_SOURCE_STATE, state)

        return state == AL_PLAYING

    def setPosition(self, position):
        alSource3f(self.id, AL_POSITION, numpy.float32(position.x), numpy.float32(position.y), numpy.float32(position.z))

    def setGain(self, gainValue):
        alSourcef(self.id, AL_GAIN, gainValue)

    def setPitch(self, pitchValue):
        alSourcef(self.id, AL_PITCH, pitchValue)

    def setVelocity(self, velocity):
        alSource3f(self.id, AL_VELOCITY, numpy.float32(velocity.x), numpy.float32(velocity.y), numpy.float32(velocity.z))

    def release(self):
        alDeleteSources(1, self.id)
