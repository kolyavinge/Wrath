import ctypes

from game.anx.CommonConstants import CommonConstants


class Screen:

    @staticmethod
    def isWindowFocused():
        user32 = ctypes.windll.user32
        windowHwnd = user32.FindWindowW(None, CommonConstants.gameTitleU)
        return windowHwnd == user32.GetFocus()

    @staticmethod
    def getWidthAndHeight():
        user32 = ctypes.windll.user32
        user32.SetProcessDPIAware()
        return (user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))

    @staticmethod
    def getCenterWindowPosition(windowWidth, windowHeight):
        screenWidth, screenHeight = Screen.getWidthAndHeight()
        x = int((screenWidth - windowWidth) / 2)
        y = int((screenHeight - windowHeight) / 2)

        return (x, y)
