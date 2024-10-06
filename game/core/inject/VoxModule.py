from game.audio.AudioBufferLoader import *
from game.audio.AudioPlayer import *
from game.audio.AudioSourceLoader import *
from game.vox.common.AudioBufferCollection import *
from game.vox.common.PersonVox import *
from game.vox.ui.GameScreenVox import *


class VoxModule:

    def init(self, binder):
        binder.bindSingleton(AudioBufferLoader, makeAudioBufferLoader)
        binder.bindSingleton(AudioPlayer, makeAudioPlayer)
        binder.bindSingleton(AudioSourceLoader, makeAudioSourceLoader)
        binder.bindSingleton(AudioBufferCollection, makeAudioBufferCollection)
        binder.bindSingleton(PersonVox, makePersonVox)
        binder.bindSingleton(GameScreenVox, makeGameScreenVox)
