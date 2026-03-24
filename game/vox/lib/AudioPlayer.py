import numpy
from openal.al import *
from openal.alc import *

from game.anx.CommonConstants import CommonConstants
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

    def stop(self, audioSource):
        alSourceStop(audioSource.id)

    def setListenerPosition(self, position, lookDirection):
        alListener3f(AL_POSITION, numpy.float32(position.x), numpy.float32(position.y), numpy.float32(position.z))

        orientation = numpy.array(
            [
                lookDirection.x,
                lookDirection.y,
                lookDirection.z,
                CommonConstants.zAxis.x,
                CommonConstants.zAxis.y,
                CommonConstants.zAxis.z,
            ],
            dtype=numpy.float32,
        )
        alListenerfv(AL_ORIENTATION, orientation.ctypes.data_as(ctypes.POINTER(ctypes.c_float)))

    def release(self, _):
        alcDestroyContext(self.context)
        alcCloseDevice(self.device)
