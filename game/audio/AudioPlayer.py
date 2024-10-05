import atexit

import numpy
from openal.al import *
from openal.alc import *


class AudioPlayer:

    def init(self):
        self.device = alcOpenDevice(None)
        assert self.device is not None
        self.context = alcCreateContext(self.device, None)
        assert self.context is not None
        alcMakeContextCurrent(self.context)
        atexit.register(self.release)

    def play(self, audioSource):
        alSourcePlay(audioSource.id)

    def setListenerPosition(self, position):
        alListener3f(AL_POSITION, numpy.float32(position.x), numpy.float32(position.y), numpy.float32(position.z))

    def release(self):
        alcDestroyContext(self.context)
        alcCloseDevice(self.device)


def makeAudioPlayer(resolver):
    return AudioPlayer()
