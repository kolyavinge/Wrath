from game.anx.CommonConstants import CommonConstants
from game.calc.TransformMatrix4Builder import TransformMatrix4Builder


class WeaponFlash:

    def __init__(self):
        self.weapon = None
        self.weaponType = None
        self.alpha = 0
        self.isVisible = True

    def update(self):
        pass

    def getModelMatrix(self):
        return (
            TransformMatrix4Builder()
            .translate(self.weapon.barrelPosition.x, self.weapon.barrelPosition.y, self.weapon.barrelPosition.z)
            .rotate(self.weapon.yawRadians, CommonConstants.zAxis)
            .rotate(self.weapon.pitchRadians, CommonConstants.xAxis)
            .resultMatrix
        )
