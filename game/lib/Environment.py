import ctypes


class Environment:

    programRootPath = ""

    @staticmethod
    def shutdown():
        ctypes.windll.user32.PostQuitMessage(0)
