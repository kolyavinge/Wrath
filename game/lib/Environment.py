import ctypes
import os


class Environment:

    programRootPath = ""

    @staticmethod
    def shutdown():
        ctypes.windll.user32.PostQuitMessage(0)


Environment.programRootPath = os.getcwd()
