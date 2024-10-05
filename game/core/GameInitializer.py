from game.audio.AudioPlayer import AudioPlayer
from game.render.common.MaterialTextureCollection import MaterialTextureCollection
from game.render.common.ShaderCollection import ShaderCollection
from game.render.common.ShaderProgramCollection import ShaderProgramCollection
from game.render.common.TextureCollection import TextureCollection
from game.vox.common.AudioBufferCollection import AudioBufferCollection
from game.vox.common.AudioSourceCollection import AudioSourceCollection


class GameInitializer:

    def __init__(
        self,
        textureCollection,
        materialTextureCollection,
        shaderCollection,
        shaderProgramCollection,
        audioPlayer,
        audioBufferCollection,
        audioSourceCollection,
    ):
        self.textureCollection = textureCollection
        self.materialTextureCollection = materialTextureCollection
        self.shaderCollection = shaderCollection
        self.shaderProgramCollection = shaderProgramCollection
        self.audioPlayer = audioPlayer
        self.audioBufferCollection = audioBufferCollection
        self.audioSourceCollection = audioSourceCollection

    def init(self):
        self.textureCollection.init()
        self.materialTextureCollection.init()
        self.shaderCollection.init()
        self.shaderProgramCollection.init()
        self.audioPlayer.init()
        self.audioBufferCollection.init()
        self.audioSourceCollection.init()


def makeGameInitializer(resolver):
    return GameInitializer(
        resolver.resolve(TextureCollection),
        resolver.resolve(MaterialTextureCollection),
        resolver.resolve(ShaderCollection),
        resolver.resolve(ShaderProgramCollection),
        resolver.resolve(AudioPlayer),
        resolver.resolve(AudioBufferCollection),
        resolver.resolve(AudioSourceCollection),
    )
