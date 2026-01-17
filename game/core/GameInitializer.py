from game.audio.AudioPlayer import AudioPlayer
from game.gl.TextRenderer import TextRenderer
from game.network.NetworkConnectionInitializer import NetworkConnectionInitializer
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
        textRenderer: TextRenderer,
        audioPlayer: AudioPlayer,
        audioBufferCollection: AudioBufferCollection,
        networkConnectionInitializer: NetworkConnectionInitializer,
    ):
        self.textureCollection = textureCollection
        self.materialTextureCollection = materialTextureCollection
        self.shaderCollection = shaderCollection
        self.shaderProgramCollection = shaderProgramCollection
        self.textRenderer = textRenderer
        self.audioPlayer = audioPlayer
        self.audioBufferCollection = audioBufferCollection
        self.networkConnectionInitializer = networkConnectionInitializer

    def init(self, client, server):
        self.textureCollection.init()
        self.materialTextureCollection.init()
        self.shaderCollection.init()
        self.shaderProgramCollection.init()
        self.textRenderer.init()
        self.audioPlayer.init()
        self.audioBufferCollection.init()
        self.networkConnectionInitializer.init(client, server)
