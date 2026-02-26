from game.lib.Environment import Environment
from game.lib.FileSystem import FileSystem
from game.lib.sys import warn


class ConfigManager:

    def __init__(
        self,
        fileSystem: FileSystem,
    ):
        self.fileSystem = fileSystem
        self.setDefault()

    def setDefault(self):
        self.clientAddress = "127.0.0.1"
        self.serverAddress = "127.0.0.1"
        self.serverPort = 6464

    def readConfig(self):
        configFIlePath = f"{Environment.programRootPath}\\app.config"
        if not self.fileSystem.fileExists(configFIlePath):
            raise Exception("Config.app file doesn't exist.")

        lines = self.fileSystem.readAllLines(configFIlePath)
        for line in lines:
            split = line.split("=")
            name = split[0].strip()
            value = split[1].strip()
            value = self.convertValue(name, value)
            if hasattr(self, name):
                setattr(self, name, value)
            else:
                warn(f"Wrong setting name '{name}'")

    def convertValue(self, name, value):
        if type(getattr(self, name)) == int:
            return int(value)

        return value
