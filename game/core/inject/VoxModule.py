from game.audio.AudioBufferLoader import *
from game.audio.AudioPlayer import *
from game.audio.AudioSourceLoader import *
from game.vox.common.AudioBufferCollection import *
from game.vox.common.AudioSourceFactory import *
from game.vox.common.PersonVox import *
from game.vox.common.PlayerItemsVox import *
from game.vox.common.PowerupVox import *
from game.vox.common.WeaponVox import *
from game.vox.ui.GameScreenVox import *


class VoxModule:

    def init(self, binder):
        binder.bindSingleton(AudioBufferLoader, makeAudioBufferLoader)
        binder.bindSingleton(AudioPlayer, makeAudioPlayer)
        binder.bindSingleton(AudioSourceLoader, makeAudioSourceLoader)
        binder.bindSingleton(AudioBufferCollection, makeAudioBufferCollection)
        binder.bindSingleton(AudioSourceFactory, makeAudioSourceFactory)
        binder.bindSingleton(PersonVox, makePersonVox)
        binder.bindSingleton(PlayerItemsVox, makePlayerItemsVox)
        binder.bindSingleton(PowerupVox, makePowerupVox)
        binder.bindSingleton(WeaponVox, makeWeaponVox)
        binder.bindSingleton(GameScreenVox, makeGameScreenVox)
