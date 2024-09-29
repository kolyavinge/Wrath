from game.gl.Shader import ShaderType
from game.gl.ShaderCompiler import ShaderCompiler
from game.lib.Environment import Environment


class ShaderCollection:

    def __init__(self, shaderCompiler):
        self.shaderCompiler = shaderCompiler

    def init(self):
        path = Environment.programRootPath + "\\game\\shaders\\"

        self.mainSceneVertex = self.shaderCompiler.compile(path + "mainScene.vert", ShaderType.vertex)
        self.mainSceneFragment = self.shaderCompiler.compile(path + "mainScene.frag", ShaderType.fragment)

        self.mainSceneLightComponentsVertex = self.shaderCompiler.compile(path + "mainSceneLightComponents.vert", ShaderType.vertex)
        self.mainSceneLightComponentsFragment = self.shaderCompiler.compile(path + "mainSceneLightComponents.frag", ShaderType.fragment)

        self.mainSceneShadowVolumesVertex = self.shaderCompiler.compile(path + "mainSceneShadowVolumes.vert", ShaderType.vertex)
        self.mainSceneShadowVolumesGeometry = self.shaderCompiler.compile(path + "mainSceneShadowVolumes2.geom", ShaderType.geometry)
        self.mainSceneShadowVolumesFragment = self.shaderCompiler.compile(path + "mainSceneShadowVolumes.frag", ShaderType.fragment)

        self.mainSceneComposeVertex = self.shaderCompiler.compile(path + "mainSceneCompose.vert", ShaderType.vertex)
        self.mainSceneComposeFragment = self.shaderCompiler.compile(path + "mainSceneCompose.frag", ShaderType.fragment)


def makeShaderCollection(resolver):
    return ShaderCollection(resolver.resolve(ShaderCompiler))
