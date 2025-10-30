from game.gl.Shader import ShaderType
from game.gl.ShaderCompiler import ShaderCompiler
from game.lib.Environment import Environment


class ShaderCollection:

    def __init__(self, shaderCompiler: ShaderCompiler):
        self.shaderCompiler = shaderCompiler

    def init(self):
        path = Environment.programRootPath + "\\game\\shaders\\"

        self.mainSceneLightComponentsVertex = self.shaderCompiler.compile(path + "mainSceneLightComponents.vert", ShaderType.vertex)
        self.mainSceneLightComponentsFragment = self.shaderCompiler.compile(path + "mainSceneLightComponents.frag", ShaderType.fragment)

        self.mainSceneShadowVolumesVertex = self.shaderCompiler.compile(path + "mainSceneShadowVolumes.vert", ShaderType.vertex)
        self.mainSceneShadowVolumesGeometry = self.shaderCompiler.compile(path + "mainSceneShadowVolumes.geom", ShaderType.geometry)
        self.mainSceneShadowVolumesFragment = self.shaderCompiler.compile(path + "mainSceneShadowVolumes.frag", ShaderType.fragment)

        self.mainSceneStencilMaskVertex = self.shaderCompiler.compile(path + "mainSceneStencilMask.vert", ShaderType.vertex)
        self.mainSceneStencilMaskFragment = self.shaderCompiler.compile(path + "mainSceneStencilMask.frag", ShaderType.fragment)

        self.mainSceneComposeVertex = self.shaderCompiler.compile(path + "mainSceneCompose.vert", ShaderType.vertex)
        self.mainSceneComposeFragment = self.shaderCompiler.compile(path + "mainSceneCompose.frag", ShaderType.fragment)

        self.crosshairVertex = self.shaderCompiler.compile(path + "crosshair.vert", ShaderType.vertex)
        self.crosshairFragment = self.shaderCompiler.compile(path + "crosshair.frag", ShaderType.fragment)

        self.meshVertex = self.shaderCompiler.compile(path + "mesh.vert", ShaderType.vertex)
        self.meshFragment = self.shaderCompiler.compile(path + "mesh.frag", ShaderType.fragment)

        self.meshExtVertex = self.shaderCompiler.compile(path + "meshExt.vert", ShaderType.vertex)
        self.meshExtFragment = self.shaderCompiler.compile(path + "meshExt.frag", ShaderType.fragment)

        self.shineCircleVertex = self.shaderCompiler.compile(path + "shineCircle.vert", ShaderType.vertex)
        self.shineCircleFragment = self.shaderCompiler.compile(path + "shineCircle.frag", ShaderType.fragment)

        self.rayVertex = self.shaderCompiler.compile(path + "ray.vert", ShaderType.vertex)
        self.rayFragment = self.shaderCompiler.compile(path + "ray.frag", ShaderType.fragment)

        self.plainColorVertex = self.shaderCompiler.compile(path + "plainColor.vert", ShaderType.vertex)
        self.plainColorFragment = self.shaderCompiler.compile(path + "plainColor.frag", ShaderType.fragment)

        self.vignetteVertex = self.shaderCompiler.compile(path + "vignette.vert", ShaderType.vertex)
        self.vignetteFragment = self.shaderCompiler.compile(path + "vignette.frag", ShaderType.fragment)

        self.launcherBulletTraceVertex = self.shaderCompiler.compile(path + "launcherBulletTrace.vert", ShaderType.vertex)
        self.launcherBulletTraceFragment = self.shaderCompiler.compile(path + "launcherBulletTrace.frag", ShaderType.fragment)
