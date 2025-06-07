import time


class Stopwatch:

    def __init__(self):
        self.elapsed = 0

    def start(self):
        self.startedAt = time.time()

    def stop(self):
        self.stopedAt = time.time()
        self.elapsed += self.stopedAt - self.startedAt

    def printElapsed(self):
        print(f"{self.elapsed:.8}")
