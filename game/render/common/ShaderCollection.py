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


def makeShaderCollection(resolver):
    return ShaderCollection(resolver.resolve(ShaderCompiler))
