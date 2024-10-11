from OpenGL.GL import *

from game.gl.Shader import Shader
from game.lib.FileSystem import FileSystem
from game.lib.sys import warn


class ShaderCompiler:

    def __init__(self, fileSystem):
        self.fileSystem = fileSystem

    def compile(self, shaderFileFullPath, shaderType):
        shaderSourceCode = self.fileSystem.readAllFile(shaderFileFullPath)
        shaderId = glCreateShader(shaderType)
        glShaderSource(shaderId, shaderSourceCode)
        glCompileShader(shaderId)
        isCompiled = glGetShaderiv(shaderId, GL_COMPILE_STATUS)
        if isCompiled == GL_TRUE:
            log = glGetShaderInfoLog(shaderId)
            if len(log) > 0:
                warn(log)
            shader = Shader(shaderId, shaderType)
            return shader
        else:
            error = glGetShaderInfoLog(shaderId)
            glDeleteShader(shaderId)
            raise Exception(error)


def makeShaderCompiler(resolver):
    return ShaderCompiler(resolver.resolve(FileSystem))
