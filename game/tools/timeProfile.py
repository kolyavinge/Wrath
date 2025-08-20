import sys

from game.lib.Stopwatch import Stopwatch
from game.lib.sys import warn


def timeProfile(title, limitSec=sys.float_info.max, showOnlyLimited=False):

    def decorator(func):
        def wrapper(*args, **kwargs):
            sw = Stopwatch()
            sw.start()

            result = func(*args, **kwargs)

            sw.stop()
            if sw.elapsed > limitSec:
                warn(f"{title}: {sw.elapsed:.8}")
            elif not showOnlyLimited:
                print(f"{title}: {sw.elapsed:.8}")

            return result

        return wrapper

    return decorator
