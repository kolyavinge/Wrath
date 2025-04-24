import time


class Stopwatch:

    def start(self):
        self.startedAt = time.time()

    def stop(self):
        self.stopedAt = time.time()
        self.elapsed = self.stopedAt - self.startedAt

    def printElapsed(self):
        print(f"{self.elapsed:.8}")
