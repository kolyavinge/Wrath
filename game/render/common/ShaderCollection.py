from game.gl.Shader import ShaderType
from game.gl.ShaderCompiler import ShaderCompiler
from game.lib.Environment import Environment


class ShaderCollection:

    def __init__(self, shaderCompiler):
        self.shaderCompiler = shaderCompiler

    def init(self):
        path = Environment.programRootPath + "\\game\\shaders\\"

        self.mainSceneLightComponentsVertex = self.shaderCompiler.compile(path + "mainSceneLightComponents.vert", ShaderType.vertex)
        self.mainSceneLightComponentsFragment = self.shaderCompiler.compile(path + "mainSceneLightComponents.frag", ShaderType.fragment)

        self.mainSceneShadowVolumesVertex = self.shaderCompiler.compile(path + "mainSceneShadowVolumes.vert", ShaderType.vertex)
        self.mainSceneShadowVolumesGeometry = self.shaderCompiler.compile(path + "mainSceneShadowVolumes.geom", ShaderType.geometry)
        self.mainSceneShadowVolumesFragment = self.shaderCompiler.compile(path + "mainSceneShadowVolumes.frag", ShaderType.fragment)

        self.mainSceneComposeVertex = self.shaderCompiler.compile(path + "mainSceneCompose.vert", ShaderType.vertex)
        self.mainSceneComposeFragment = self.shaderCompiler.compile(path + "mainSceneCompose.frag", ShaderType.fragment)

        self.crosshairVertex = self.shaderCompiler.compile(path + "crosshair.vert", ShaderType.vertex)
        self.crosshairFragment = self.shaderCompiler.compile(path + "crosshair.frag", ShaderType.fragment)

        self.textureVertex = self.shaderCompiler.compile(path + "texture.vert", ShaderType.vertex)
        self.textureFragment = self.shaderCompiler.compile(path + "texture.frag", ShaderType.fragment)


def makeShaderCollection(resolver):
    return ShaderCollection(resolver.resolve(ShaderCompiler))
