from game.engine.GameState import GameState
from game.lib.Numeric import Numeric


class CameraScopeChecker:

    def __init__(self, gameData: GameState):
        self.gameData = gameData
        self.width = 0
        self.height = 0

    def isPointInCamera(self, px, py, pz, scale=1.0):
        # проецируем точку на экран
        # и проверяем что она попадает в его пределы

        m = self.gameData.camera.viewProjectionMatrix

        # для оптимизации, чтобы не создавать промежуточные обьекты Vector3 и Vector4
        # умножение матрицы на вектор делаем тут

        w = m.items[3] * px + m.items[7] * py + m.items[11] * pz + m.items[15] * 1.0
        if w == 0.0:
            return False

        x = m.items[0] * px + m.items[4] * py + m.items[8] * pz + m.items[12] * 1.0
        y = m.items[1] * px + m.items[5] * py + m.items[9] * pz + m.items[13] * 1.0
        z = m.items[2] * px + m.items[6] * py + m.items[10] * pz + m.items[14] * 1.0

        # convert to Normalized Device Coordinates
        x /= w
        y /= w
        z /= w

        return Numeric.between(x, -scale, scale) and Numeric.between(y, -scale, scale) and Numeric.between(z, -scale, scale)
