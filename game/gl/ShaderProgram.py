from OpenGL.GL import *


class ShaderProgram:

    def __init__(self, shaders):
        self.id = glCreateProgram()
        for shader in shaders:
            glAttachShader(self.id, shader.id)
        glLinkProgram(self.id)

    def use(self):
        glUseProgram(self.id)

    def unuse(self):
        glUseProgram(0)

    def setUniform(self, name, value):
        location = glGetUniformLocation(self.id, name)
        glUniformMatrix4fv(location, 1, GL_FALSE, value)
