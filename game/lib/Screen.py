import ctypes


class Screen:

    @staticmethod
    def getWidthAndHeight():
        user32 = ctypes.windll.user32
        user32.SetProcessDPIAware()
        return (user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))
