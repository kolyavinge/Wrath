from game.gl.ShaderCompiler import *
from game.gl.TextureLoader import *
from game.gl.VBOBuilderFactory import *
from game.gl.VBORenderer import *
from game.render.common.ShaderCollection import *
from game.render.common.ShaderProgramCollection import *
from game.render.common.TextureCollection import *
from game.render.debug.DebugRenderer import *
from game.render.level.CeilingVBOBuilder import *
from game.render.level.FloorVBOBuilder import *
from game.render.level.LevelRenderer import *
from game.render.level.LevelSegmentVBOBuilder import *
from game.render.level.LevelSegmentVBOCollection import *
from game.render.level.StairVBOBuilder import *
from game.render.level.WallVBOBuilder import *
from game.render.ui.GameScreenRenderer import *


class RenderModule:

    def init(self, binder):
        binder.bindSingleton(ShaderCompiler, makeShaderCompiler)
        binder.bindSingleton(TextureLoader, makeTextureLoader)
        binder.bindSingleton(VBOBuilderFactory, makeVBOBuilderFactory)
        binder.bindSingleton(VBORenderer, makeVBORenderer)
        binder.bindSingleton(ShaderCollection, makeShaderCollection)
        binder.bindSingleton(ShaderProgramCollection, makeShaderProgramCollection)
        binder.bindSingleton(TextureCollection, makeTextureCollection)
        binder.bindSingleton(DebugRenderer, makeDebugRenderer)
        binder.bindSingleton(CeilingVBOBuilder, makeCeilingVBOBuilder)
        binder.bindSingleton(FloorVBOBuilder, makeFloorVBOBuilder)
        binder.bindSingleton(LevelRenderer, makeLevelRenderer)
        binder.bindSingleton(LevelSegmentVBOBuilder, makeLevelSegmentVBOBuilder)
        binder.bindSingleton(LevelSegmentVBOCollection, makeLevelSegmentVBOCollection)
        binder.bindSingleton(StairVBOBuilder, makeStairVBOBuilder)
        binder.bindSingleton(WallVBOBuilder, makeWallVBOBuilder)
        binder.bindSingleton(GameScreenRenderer, makeGameScreenRenderer)
