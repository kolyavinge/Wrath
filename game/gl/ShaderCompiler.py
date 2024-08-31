from OpenGL.GL import *

from game.gl.Shader import Shader
from game.lib.File import File


class ShaderCompiler:

    def compile(self, shaderFileFullPath, shaderType):
        shaderSourceCode = File.readAllFile(shaderFileFullPath)
        shaderId = glCreateShader(shaderType)
        glShaderSource(shaderId, shaderSourceCode)
        glCompileShader(shaderId)
        isCompiled = glGetShaderiv(shaderId, GL_COMPILE_STATUS)
        if isCompiled == GL_TRUE:
            shader = Shader(shaderId, shaderType)
            return shader
        else:
            error = glGetShaderInfoLog(shaderId)
            glDeleteShader(shaderId)
            raise Exception(error)


def makeShaderCompiler(resolver):
    return ShaderCompiler()
