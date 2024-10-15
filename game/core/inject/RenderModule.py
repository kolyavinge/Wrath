from game.gl.AdjancencyFormatConverter import *
from game.gl.Model3dLoader import *
from game.gl.ScreenQuadVBO import *
from game.gl.ShaderCompiler import *
from game.gl.TextureLoader import *
from game.gl.VBOBuilderFactory import *
from game.gl.VBORenderer import *
from game.render.common.MaterialTextureCollection import *
from game.render.common.ShaderCollection import *
from game.render.common.ShaderProgramCollection import *
from game.render.common.TextureCollection import *
from game.render.debug.DebugRenderer import *
from game.render.level.ConstructionVBOBuilder import *
from game.render.level.LevelItemGroupBuilder import *
from game.render.level.LevelItemGroupCollection import *
from game.render.level.LevelRenderer import *
from game.render.level.ShadowCastLevelItemBuilder import *
from game.render.level.ShadowCastLevelItemCollection import *
from game.render.level.StairVBOBuilder import *
from game.render.level.WallVBOBuilder import *
from game.render.main.MainSceneFramebuffer import *
from game.render.main.MainSceneRenderer import *
from game.render.ui.GameScreenRenderer import *
from game.render.weapon.PlayerWeaponRenderer import *
from game.render.weapon.WeaponModel3dFactory import *
from game.render.weapon.WeaponRenderModel3dCollection import *


class RenderModule:

    def init(self, binder):
        binder.bindSingleton(AdjacencyFormatConverter, makeAdjacencyFormatConverter)
        binder.bindSingleton(Model3dLoader, makeModel3dLoader)
        binder.bindSingleton(ScreenQuadVBO, makeScreenQuadVBO)
        binder.bindSingleton(ShaderCompiler, makeShaderCompiler)
        binder.bindSingleton(TextureLoader, makeTextureLoader)
        binder.bindSingleton(VBOBuilderFactory, makeVBOBuilderFactory)
        binder.bindSingleton(VBORenderer, makeVBORenderer)
        binder.bindSingleton(MaterialTextureCollection, makeMaterialTextureCollection)
        binder.bindSingleton(ShaderCollection, makeShaderCollection)
        binder.bindSingleton(ShaderProgramCollection, makeShaderProgramCollection)
        binder.bindSingleton(TextureCollection, makeTextureCollection)
        binder.bindSingleton(DebugRenderer, makeDebugRenderer)
        binder.bindSingleton(ConstructionVBOBuilder, makeConstructionVBOBuilder)
        binder.bindSingleton(LevelItemGroupBuilder, makeLevelItemGroupBuilder)
        binder.bindSingleton(LevelItemGroupCollection, makeLevelItemGroupCollection)
        binder.bindSingleton(LevelRenderer, makeLevelRenderer)
        binder.bindSingleton(ShadowCastLevelItemBuilder, makeShadowCastLevelItemBuilder)
        binder.bindSingleton(ShadowCastLevelItemCollection, makeShadowCastLevelItemCollection)
        binder.bindSingleton(StairVBOBuilder, makeStairVBOBuilder)
        binder.bindSingleton(WallVBOBuilder, makeWallVBOBuilder)
        binder.bindSingleton(MainSceneFramebuffer, makeMainSceneFramebuffer)
        binder.bindSingleton(MainSceneRenderer, makeMainSceneRenderer)
        binder.bindSingleton(GameScreenRenderer, makeGameScreenRenderer)
        binder.bindSingleton(PlayerWeaponRenderer, makePlayerWeaponRenderer)
        binder.bindSingleton(WeaponModel3dFactory, makeWeaponModel3dFactory)
        binder.bindSingleton(WeaponRenderModel3dCollection, makeWeaponRenderModel3dCollection)
