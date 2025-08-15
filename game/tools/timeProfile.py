from game.lib.Stopwatch import Stopwatch


def timeProfile(title):

    def decorator(func):
        def wrapper(*args, **kwargs):
            sw = Stopwatch()
            sw.start()

            result = func(*args, **kwargs)

            sw.stop()
            print(f"{title}: {sw.elapsed:.8}")

            return result

        return wrapper

    return decorator
