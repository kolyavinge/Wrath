import time


class Stopwatch:

    def __init__(self):
        self.elapsed = 0

    def start(self):
        self.startedAt = time.perf_counter()

    def stop(self):
        self.stopedAt = time.perf_counter()
        self.elapsed += self.stopedAt - self.startedAt

    def printElapsed(self):
        print(f"{self.elapsed:.8}.")
