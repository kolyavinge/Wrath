from game.audio.AudioPlayer import AudioPlayer
from game.render.common.MaterialTextureCollection import MaterialTextureCollection
from game.render.common.ShaderCollection import ShaderCollection
from game.render.common.ShaderProgramCollection import ShaderProgramCollection
from game.render.common.TextureCollection import TextureCollection
from game.vox.common.AudioBufferCollection import AudioBufferCollection


class GameInitializer:

    def __init__(
        self,
        textureCollection: TextureCollection,
        materialTextureCollection: MaterialTextureCollection,
        shaderCollection: ShaderCollection,
        shaderProgramCollection: ShaderProgramCollection,
        audioPlayer: AudioPlayer,
        audioBufferCollection: AudioBufferCollection,
    ):
        self.textureCollection = textureCollection
        self.materialTextureCollection = materialTextureCollection
        self.shaderCollection = shaderCollection
        self.shaderProgramCollection = shaderProgramCollection
        self.audioPlayer = audioPlayer
        self.audioBufferCollection = audioBufferCollection

    def init(self):
        self.textureCollection.init()
        self.materialTextureCollection.init()
        self.shaderCollection.init()
        self.shaderProgramCollection.init()
        self.audioPlayer.init()
        self.audioBufferCollection.init()
