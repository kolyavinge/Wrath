from game.gl.ShaderCompiler import *
from game.render.debug.DebugRenderer import *
from game.render.ShaderCollection import *
from game.render.ShaderProgramCollection import *
from game.render.TextureCollection import *


class RenderModule:

    def init(self, binder):
        binder.bindSingleton(ShaderCompiler, makeShaderCompiler)
        binder.bindSingleton(DebugRenderer, makeDebugRenderer)
        binder.bindSingleton(ShaderCollection, makeShaderCollection)
        binder.bindSingleton(ShaderProgramCollection, makeShaderProgramCollection)
        binder.bindSingleton(TextureCollection, makeTextureCollection)
