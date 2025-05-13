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
        binder.bindSingleton(AudioBufferLoader)
        binder.bindSingleton(AudioPlayer)
        binder.bindSingleton(AudioSourceLoader)
        binder.bindSingleton(AudioBufferCollection)
        binder.bindSingleton(AudioSourceFactory)
        binder.bindSingleton(PersonVox)
        binder.bindSingleton(PlayerItemsVox)
        binder.bindSingleton(PowerupVox)
        binder.bindSingleton(WeaponVox)
        binder.bindSingleton(GameScreenVox)
