import numpy
from openal.al import *
from openal.alc import *

from game.lib.EventManager import EventManager, Events


class AudioPlayer:

    def __init__(
        self,
        eventManager: EventManager,
    ):
        eventManager.attachToEvent(Events.appExited, self.release)

    def init(self):
        self.device = alcOpenDevice(None)
        assert self.device is not None
        self.context = alcCreateContext(self.device, None)
        assert self.context is not None
        alcMakeContextCurrent(self.context)

    def play(self, audioSource):
        alSourcePlay(audioSource.id)

    def setListenerPosition(self, position):
        alListener3f(AL_POSITION, numpy.float32(position.x), numpy.float32(position.y), numpy.float32(position.z))

    def release(self, _):
        alcDestroyContext(self.context)
        alcCloseDevice(self.device)
