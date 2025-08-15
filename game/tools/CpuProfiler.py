import cProfile
import os
import pstats
import time


class CpuProfiler:

    root = "misc\\tmp\\profiler"
    profiler = None
    started = False

    @staticmethod
    def init():
        CpuProfiler.profiler = cProfile.Profile()
        CpuProfiler.profileName = time.time()

    @staticmethod
    def start():
        CpuProfiler.profiler.enable()
        CpuProfiler.started = True

    @staticmethod
    def stop():
        CpuProfiler.profiler.disable()

    @staticmethod
    def makeResult():
        if CpuProfiler.profiler is not None and CpuProfiler.started:
            stats = pstats.Stats(CpuProfiler.profiler).sort_stats(-1)
            statName = f"{CpuProfiler.root}\\output_{CpuProfiler.profileName}.pstats"
            stats.dump_stats(statName)
            os.system(f"gprof2dot -f pstats {statName} | dot -Tpng -o {statName}.png")


def cpuProfile(func):
    def wrapper(*args, **kwargs):
        CpuProfiler.start()
        result = func(*args, **kwargs)
        CpuProfiler.stop()

        return result

    return wrapper
