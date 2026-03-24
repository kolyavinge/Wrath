from game.lib.DecrementCounter import DecrementCounter
from game.model.weapon.Bullet import Bullet


# граната в своем поведении почти не отличается от пули
class Grenade(Bullet):

    def __init__(self, traceType=None, explosionType=None):
        super().__init__(traceType, explosionType)
        self.isVisible = True
        self.ricochetPossibility = 1.0
        self.detonationTimeout = DecrementCounter()
