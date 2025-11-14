from game.render.common.ShaderCollection import ShaderCollection
from game.render.shaderprogram.BlurShaderProgram import BlurShaderProgram
from game.render.shaderprogram.CrossshairShaderProgram import CrossshairShaderProgram
from game.render.shaderprogram.LauncherBulletTraceShaderProgram import *
from game.render.shaderprogram.MainSceneComposeShaderProgram import *
from game.render.shaderprogram.MainSceneLightComponentsShaderProgram import *
from game.render.shaderprogram.MainSceneShadowVolumesShaderProgram import *
from game.render.shaderprogram.MainSceneStencilMaskShaderProgram import *
from game.render.shaderprogram.MeshExtShaderProgram import MeshExtShaderProgram
from game.render.shaderprogram.MeshShaderProgram import MeshShaderProgram
from game.render.shaderprogram.PlainColorShaderProgram import PlainColorShaderProgram
from game.render.shaderprogram.PlasmaExplosionShaderProgram import *
from game.render.shaderprogram.RayShaderProgram import RayShaderProgram
from game.render.shaderprogram.ShineCircleShaderProgram import ShineCircleShaderProgram
from game.render.shaderprogram.VignetteShaderProgram import VignetteShaderProgram


class ShaderProgramCollection:

    def __init__(self, shaderCollection: ShaderCollection):
        self.shaderCollection = shaderCollection

    def init(self):
        self.mainSceneLightComponents = MainSceneLightComponentsShaderProgram(
            [
                self.shaderCollection.mainSceneLightComponentsVertex,
                self.shaderCollection.mainSceneLightComponentsFragment,
            ]
        )

        self.mainSceneShadowVolumes = MainSceneShadowVolumesShaderProgram(
            [
                self.shaderCollection.mainSceneShadowVolumesVertex,
                self.shaderCollection.mainSceneShadowVolumesGeometry,
                self.shaderCollection.mainSceneShadowVolumesFragment,
            ]
        )

        self.mainSceneStencilMask = MainSceneStencilMaskShaderProgram(
            [
                self.shaderCollection.mainSceneStencilMaskVertex,
                self.shaderCollection.mainSceneStencilMaskFragment,
            ]
        )

        self.mainSceneCompose = MainSceneComposeShaderProgram(
            [
                self.shaderCollection.mainSceneComposeVertex,
                self.shaderCollection.mainSceneComposeFragment,
            ]
        )

        self.crosshair = CrossshairShaderProgram(
            [
                self.shaderCollection.crosshairVertex,
                self.shaderCollection.crosshairFragment,
            ]
        )

        self.mesh = MeshShaderProgram(
            [
                self.shaderCollection.meshVertex,
                self.shaderCollection.meshFragment,
            ]
        )

        self.meshExt = MeshExtShaderProgram(
            [
                self.shaderCollection.meshExtVertex,
                self.shaderCollection.meshExtFragment,
            ]
        )

        self.shineCircle = ShineCircleShaderProgram(
            [
                self.shaderCollection.shineCircleVertex,
                self.shaderCollection.shineCircleFragment,
            ]
        )

        self.ray = RayShaderProgram(
            [
                self.shaderCollection.rayVertex,
                self.shaderCollection.rayFragment,
            ]
        )

        self.plainColor = PlainColorShaderProgram(
            [
                self.shaderCollection.plainColorVertex,
                self.shaderCollection.plainColorFragment,
            ]
        )

        self.vignette = VignetteShaderProgram(
            [
                self.shaderCollection.vignetteVertex,
                self.shaderCollection.vignetteFragment,
            ]
        )

        self.launcherBulletTrace = LauncherBulletTraceShaderProgram(
            [
                self.shaderCollection.common,
                self.shaderCollection.launcherBulletTraceVertex,
                self.shaderCollection.launcherBulletTraceFragment,
            ]
        )

        self.blur = BlurShaderProgram(
            [
                self.shaderCollection.blurVertex,
                self.shaderCollection.blurFragment,
            ]
        )

        self.plasmaExplosion = PlasmaExplosionShaderProgram(
            [
                self.shaderCollection.plasmaExplosionVertex,
                self.shaderCollection.plasmaExplosionFragment,
            ]
        )
