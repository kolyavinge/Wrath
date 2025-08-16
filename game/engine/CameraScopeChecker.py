from game.calc.Vector4 import Vector4
from game.engine.GameData import GameData
from game.lib.Numeric import Numeric


class CameraScopeChecker:

    def __init__(self, gameData: GameData):
        self.gameData = gameData
        self.width = 0
        self.height = 0

    def isPointInCamera(self, point):
        # проецируем точку на экран
        # и проверяем что она попадает в его пределы

        v = self.gameData.camera.viewProjectionMatrix.mulVector4(Vector4(point.x, point.y, point.z, 1.0))
        if v.w == 0.0:
            return False

        v.toNDC()

        return Numeric.between(v.x, -1.0, 1.0) and Numeric.between(v.y, -1.0, 1.0)
