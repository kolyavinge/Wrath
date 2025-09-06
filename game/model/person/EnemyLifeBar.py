from game.calc.TransformMatrix4 import TransformMatrix4
from game.lib.DecrementCounter import DecrementCounter


class EnemyLifeBar:

    def __init__(self):
        self.fadeRemain = DecrementCounter()
        self.fadeRemain.set(1)
        self.alpha = 0
        self.isVisible = False
        self.modelMatrix = TransformMatrix4()
