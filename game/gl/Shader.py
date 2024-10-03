class ShaderType:

    # GL constants
    vertex = 0x8B31
    tessControl = 0x8E88
    tessEvaluation = 0x8E87
    geometry = 0x8DD9
    fragment = 0x8B30


class Shader:

    def __init__(self, id, type):
        self.id = id
        self.type = type
