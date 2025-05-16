from game.calc.TransformMatrix4 import TransformMatrix4
from game.model.weapon.Weapon import Weapon


class NullWeapon(Weapon):

    def __init__(self):
        super().__init__(None)

    def getModelMatrix(self):
        matrix = TransformMatrix4()
        matrix.setZero()

        return matrix


NullWeapon.instance = NullWeapon()
