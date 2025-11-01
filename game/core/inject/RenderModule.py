from game.gl.AdjacencyFormatConverter import *
from game.gl.model3d.AnimationLoader import *
from game.gl.model3d.AnimationPlayer import *
from game.gl.model3d.FrameInterpolator import *
from game.gl.model3d.FrameLoader import *
from game.gl.model3d.Model3dLoader import *
from game.gl.model3d.Model3dRenderer import *
from game.gl.model3d.RenderModel3dLoader import *
from game.gl.ShaderCompiler import *
from game.gl.SpriteRendererFactory import *
from game.gl.TextRenderer import *
from game.gl.TextureLoader import *
from game.gl.vbo.ScreenQuadVBO import *
from game.gl.vbo.VBOBuilderFactory import *
from game.gl.vbo.VBORenderer import *
from game.gl.vbo.VBOUpdaterFactory import *
from game.render.anx.LauncherBulletTraceParticleBufferInitializer import *
from game.render.anx.RayRenderer import *
from game.render.anx.ShineCircleRenderer import *
from game.render.anx.VignetteRenderer import *
from game.render.common.MaterialTextureCollection import *
from game.render.common.Model3dDirectory import *
from game.render.common.ShaderCollection import *
from game.render.common.ShaderProgramCollection import *
from game.render.common.TextureCollection import *
from game.render.debug.PlayerSegmentItemsRenderer import *
from game.render.level.BackgroundRenderer import *
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
from game.render.menu.DashboardRenderer import *
from game.render.menu.DashboardSpriteRenderer import *
from game.render.menu.DashboardTextRenderer import *
from game.render.person.EnemyAnimationCollection import *
from game.render.person.EnemyLifeBarRenderer import *
from game.render.person.EnemyModel3dFactory import *
from game.render.person.EnemyRenderCollection import *
from game.render.person.EnemyRenderer import *
from game.render.person.PlayerBloodStainRenderCollection import *
from game.render.person.PlayerBloodStainRenderer import *
from game.render.person.PlayerBloodStainRenderMeshFactory import *
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
from game.render.weapon.shine.PlasmaShineBulletRenderer import *
from game.render.weapon.ShineBulletRenderer import *
from game.render.weapon.SniperCrosshairRenderer import *
from game.render.weapon.trace.LauncherBulletTraceRenderer import *
from game.render.weapon.trace.RailgunBulletTraceRenderer import *
from game.render.weapon.trace.RayBulletTraceRenderer import *
from game.render.weapon.trace.RifleBulletTraceRenderer import *
from game.render.weapon.trace.SniperBulletTraceRenderer import *
from game.render.weapon.WeaponFlashRenderCollection import *
from game.render.weapon.WeaponFlashRenderer import *
from game.render.weapon.WeaponFlashRenderMeshFactory import *
from game.render.weapon.WeaponModel3dFactory import *
from game.render.weapon.WeaponRenderCollection import *
from game.render.weapon.WeaponRenderer import *


class RenderModule:

    def init(self, binder):
        binder.bindSingleton(AdjacencyFormatConverter)
        binder.bindSingleton(AnimationLoader)
        binder.bindSingleton(AnimationPlayer)
        binder.bindSingleton(FrameInterpolator)
        binder.bindSingleton(FrameLoader)
        binder.bindSingleton(Model3dLoader)
        binder.bindSingleton(Model3dRenderer)
        binder.bindSingleton(RenderModel3dLoader)
        binder.bindSingleton(ShaderCompiler)
        binder.bindSingleton(SpriteRendererFactory)
        binder.bindSingleton(TextRenderer)
        binder.bindSingleton(TextureLoader)
        binder.bindSingleton(ScreenQuadVBO)
        binder.bindSingleton(VBOBuilderFactory)
        binder.bindSingleton(VBORenderer)
        binder.bindSingleton(VBOUpdaterFactory)
        binder.bindSingleton(LauncherBulletTraceParticleBufferInitializer)
        binder.bindSingleton(RayRenderer)
        binder.bindSingleton(ShineCircleRenderer)
        binder.bindSingleton(VignetteRenderer)
        binder.bindSingleton(MaterialTextureCollection)
        binder.bindSingleton(Model3dDirectory)
        binder.bindSingleton(ShaderCollection)
        binder.bindSingleton(ShaderProgramCollection)
        binder.bindSingleton(TextureCollection)
        binder.bindSingleton(PlayerSegmentItemsRenderer)
        binder.bindSingleton(BackgroundRenderer)
        binder.bindSingleton(ConstructionVBOBuilder)
        binder.bindSingleton(LampVBOBuilder)
        binder.bindSingleton(LevelItemRenderCollection)
        binder.bindSingleton(LevelItemRenderer)
        binder.bindSingleton(LevelItemRenderModel3dBuilder)
        binder.bindSingleton(LevelSegmentRenderer)
        binder.bindSingleton(ShadowCasterBuilder)
        binder.bindSingleton(ShadowCasterRenderCollection)
        binder.bindSingleton(ShadowCasterRenderer)
        binder.bindSingleton(StairVBOBuilder)
        binder.bindSingleton(WallVBOBuilder)
        binder.bindSingleton(MainSceneRenderer)
        binder.bindSingleton(ShadowedObjectFramebuffer)
        binder.bindSingleton(ShadowedObjectRenderer)
        binder.bindSingleton(DashboardRenderer)
        binder.bindSingleton(DashboardSpriteRenderer)
        binder.bindSingleton(DashboardTextRenderer)
        binder.bindSingleton(EnemyAnimationCollection)
        binder.bindSingleton(EnemyLifeBarRenderer)
        binder.bindSingleton(EnemyModel3dFactory)
        binder.bindSingleton(EnemyRenderCollection)
        binder.bindSingleton(EnemyRenderer)
        binder.bindSingleton(PlayerBloodStainRenderCollection)
        binder.bindSingleton(PlayerBloodStainRenderer)
        binder.bindSingleton(PlayerBloodStainRenderMeshFactory)
        binder.bindSingleton(PowerupModel3dFactory)
        binder.bindSingleton(PowerupRenderCollection)
        binder.bindSingleton(PowerupRenderer)
        binder.bindSingleton(GameScreenInitializer)
        binder.bindSingleton(GameScreenRenderer)
        binder.bindSingleton(BulletHoleRenderCollection)
        binder.bindSingleton(BulletHoleRenderer)
        binder.bindSingleton(BulletModel3dFactory)
        binder.bindSingleton(BulletRenderCollection)
        binder.bindSingleton(BulletRenderer)
        binder.bindSingleton(BulletTraceRenderer)
        binder.bindSingleton(CrosshairRenderer)
        binder.bindSingleton(PlasmaShineBulletRenderer)
        binder.bindSingleton(ShineBulletRenderer)
        binder.bindSingleton(SniperCrosshairRenderer)
        binder.bindSingleton(LauncherBulletTraceRenderer)
        binder.bindSingleton(RailgunBulletTraceRenderer)
        binder.bindSingleton(RayBulletTraceRenderer)
        binder.bindSingleton(RifleBulletTraceRenderer)
        binder.bindSingleton(SniperBulletTraceRenderer)
        binder.bindSingleton(WeaponFlashRenderCollection)
        binder.bindSingleton(WeaponFlashRenderer)
        binder.bindSingleton(WeaponFlashRenderMeshFactory)
        binder.bindSingleton(WeaponModel3dFactory)
        binder.bindSingleton(WeaponRenderCollection)
        binder.bindSingleton(WeaponRenderer)
