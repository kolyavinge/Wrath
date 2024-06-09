from game.model.VelocityFunc import VelocityFunc


class Person:

    def __init__(self):
        self.hasMoved = False
        self.movingTime = 0
        self.movingTimeDelta = 0.1
        self.velocityFunc = VelocityFunc()

    def getVelocity(self):
        return self.velocityFunc.getValue(self.movingTime)
