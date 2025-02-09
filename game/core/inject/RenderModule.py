from game.gl.AdjacencyFormatConverter import *
from game.gl.AsyncModel3dLoader import *
from game.gl.Model3dLoader import *
from game.gl.RenderModel3dLoader import *
from game.gl.ScreenQuadVBO import *
from game.gl.ShaderCompiler import *
from game.gl.TextureLoader import *
from game.gl.VBOBuilderFactory import *
from game.gl.VBORenderer import *
from game.gl.VBOUpdaterFactory import *
from game.render.anx.BackgroundRenderer import *
from game.render.anx.RayRenderer import *
from game.render.anx.ShineCircleRenderer import *
from game.render.common.MaterialTextureCollection import *
from game.render.common.Model3dCollection import *
from game.render.common.Model3dDirectory import *
from game.render.common.ShaderCollection import *
from game.render.common.ShaderProgramCollection import *
from game.render.common.TextureCollection import *
from game.render.debug.DebugRenderer import *
from game.render.level.ConstructionVBOBuilder import *
from game.render.level.LampVBOBuilder import *
from game.render.level.LevelItemRenderCollection import *
from game.render.level.LevelItemRenderer import *
from game.render.level.LevelItemRenderModel3dBuilder import *
from game.render.level.LevelSegmentRenderer import *
from game.render.level.ShadowCasterBuilder import *
from game.render.level.ShadowCasterRenderCollection import *
from game.render.level.ShadowCasterRenderer import *
from game.render.level.StairVBOBuilder import *
from game.render.level.WallVBOBuilder import *
from game.render.main.MainSceneRenderer import *
from game.render.main.ShadowedObjectFramebuffer import *
from game.render.main.ShadowedObjectRenderer import *
from game.render.person.EnemyModel3dFactory import *
from game.render.person.EnemyRenderCollection import *
from game.render.person.EnemyRenderer import *
from game.render.powerup.PowerupModel3dFactory import *
from game.render.powerup.PowerupRenderCollection import *
from game.render.powerup.PowerupRenderer import *
from game.render.ui.GameScreenInitializer import *
from game.render.ui.GameScreenRenderer import *
from game.render.weapon.BulletHoleRenderCollection import *
from game.render.weapon.BulletHoleRenderer import *
from game.render.weapon.BulletModel3dFactory import *
from game.render.weapon.BulletRenderCollection import *
from game.render.weapon.BulletRenderer import *
from game.render.weapon.BulletTraceRenderer import *
from game.render.weapon.CrosshairRenderer import *
from game.render.weapon.PlayerWeaponRenderer import *
from game.render.weapon.shine.PlasmaShineBulletRenderer import *
from game.render.weapon.ShineBulletRenderer import *
from game.render.weapon.SniperCrosshairRenderer import *
from game.render.weapon.trace.RailgunBulletTraceRenderer import *
from game.render.weapon.WeaponFlashRenderCollection import *
from game.render.weapon.WeaponFlashRenderer import *
from game.render.weapon.WeaponFlashRenderMeshFactory import *
from game.render.weapon.WeaponModel3dFactory import *
from game.render.weapon.WeaponRenderCollection import *


class RenderModule:

    def init(self, binder):
        binder.bindSingleton(AdjacencyFormatConverter, makeAdjacencyFormatConverter)
        # binder.bindSingleton(AsyncModel3dLoader, makeAsyncModel3dLoader)
        binder.bindSingleton(Model3dLoader, makeModel3dLoader)
        binder.bindSingleton(RenderModel3dLoader, makeRenderModel3dLoader)
        binder.bindSingleton(ScreenQuadVBO, makeScreenQuadVBO)
        binder.bindSingleton(ShaderCompiler, makeShaderCompiler)
        binder.bindSingleton(TextureLoader, makeTextureLoader)
        binder.bindSingleton(VBOBuilderFactory, makeVBOBuilderFactory)
        binder.bindSingleton(VBORenderer, makeVBORenderer)
        binder.bindSingleton(VBOUpdaterFactory, makeVBOUpdaterFactory)
        binder.bindSingleton(BackgroundRenderer, makeBackgroundRenderer)
        binder.bindSingleton(RayRenderer, makeRayRenderer)
        binder.bindSingleton(ShineCircleRenderer, makeShineCircleRenderer)
        binder.bindSingleton(MaterialTextureCollection, makeMaterialTextureCollection)
        # binder.bindSingleton(Model3dCollection, makeModel3dCollection)
        binder.bindSingleton(Model3dDirectory, makeModel3dDirectory)
        binder.bindSingleton(ShaderCollection, makeShaderCollection)
        binder.bindSingleton(ShaderProgramCollection, makeShaderProgramCollection)
        binder.bindSingleton(TextureCollection, makeTextureCollection)
        binder.bindSingleton(DebugRenderer, makeDebugRenderer)
        binder.bindSingleton(ConstructionVBOBuilder, makeConstructionVBOBuilder)
        binder.bindSingleton(LampVBOBuilder, makeLampVBOBuilder)
        binder.bindSingleton(LevelItemRenderCollection, makeLevelItemRenderCollection)
        binder.bindSingleton(LevelItemRenderer, makeLevelItemRenderer)
        binder.bindSingleton(LevelItemRenderModel3dBuilder, makeLevelItemRenderModel3dBuilder)
        binder.bindSingleton(LevelSegmentRenderer, makeLevelSegmentRenderer)
        binder.bindSingleton(ShadowCasterBuilder, makeShadowCasterBuilder)
        binder.bindSingleton(ShadowCasterRenderCollection, makeShadowCasterRenderCollection)
        binder.bindSingleton(ShadowCasterRenderer, makeShadowCasterRenderer)
        binder.bindSingleton(StairVBOBuilder, makeStairVBOBuilder)
        binder.bindSingleton(WallVBOBuilder, makeWallVBOBuilder)
        binder.bindSingleton(MainSceneRenderer, makeMainSceneRenderer)
        binder.bindSingleton(ShadowedObjectFramebuffer, makeShadowedObjectFramebuffer)
        binder.bindSingleton(ShadowedObjectRenderer, makeShadowedObjectRenderer)
        binder.bindSingleton(EnemyModel3dFactory, makeEnemyModel3dFactory)
        binder.bindSingleton(EnemyRenderCollection, makeEnemyRenderCollection)
        binder.bindSingleton(EnemyRenderer, makeEnemyRenderer)
        binder.bindSingleton(PowerupModel3dFactory, makePowerupModel3dFactory)
        binder.bindSingleton(PowerupRenderCollection, makePowerupRenderCollection)
        binder.bindSingleton(PowerupRenderer, makePowerupRenderer)
        binder.bindSingleton(GameScreenInitializer, makeGameScreenInitializer)
        binder.bindSingleton(GameScreenRenderer, makeGameScreenRenderer)
        binder.bindSingleton(BulletHoleRenderCollection, makeBulletHoleRenderCollection)
        binder.bindSingleton(BulletHoleRenderer, makeBulletHoleRenderer)
        binder.bindSingleton(BulletModel3dFactory, makeBulletModel3dFactory)
        binder.bindSingleton(BulletRenderCollection, makeBulletRenderCollection)
        binder.bindSingleton(BulletRenderer, makeBulletRenderer)
        binder.bindSingleton(BulletTraceRenderer, makeBulletTraceRenderer)
        binder.bindSingleton(CrosshairRenderer, makeCrosshairRenderer)
        binder.bindSingleton(PlayerWeaponRenderer, makePlayerWeaponRenderer)
        binder.bindSingleton(PlasmaShineBulletRenderer, makePlasmaShineBulletRenderer)
        binder.bindSingleton(ShineBulletRenderer, makeShineBulletRenderer)
        binder.bindSingleton(SniperCrosshairRenderer, makeSniperCrosshairRenderer)
        binder.bindSingleton(RailgunBulletTraceRenderer, makeRailgunBulletTraceRenderer)
        binder.bindSingleton(WeaponFlashRenderCollection, makeWeaponFlashRenderCollection)
        binder.bindSingleton(WeaponFlashRenderer, makeWeaponFlashRenderer)
        binder.bindSingleton(WeaponFlashRenderMeshFactory, makeWeaponFlashRenderMeshFactory)
        binder.bindSingleton(WeaponModel3dFactory, makeWeaponModel3dFactory)
        binder.bindSingleton(WeaponRenderCollection, makeWeaponRenderCollection)
