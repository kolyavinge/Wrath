from game.lib.Environment import Environment
from game.lib.FileSystem import FileSystem
from game.lib.sys import warn


class ConfigManager:

    def __init__(
        self,
        fileSystem: FileSystem,
    ):
        self.fileSystem = fileSystem
        self.setDefaultValues()
        self.readConfigOrCreateDefault()

    def readConfigOrCreateDefault(self):
        configFilePath = self.getConfigFilePath()
        if self.fileSystem.fileExists(configFilePath):
            self.readConfig(configFilePath)
        else:
            warn("File config.app doesn't exist. Create default.")
            self.createDefault()

    def readConfig(self, configFilePath):
        lines = self.fileSystem.readAllLines(configFilePath)
        for line in lines:
            split = line.split("=")
            name = split[0].strip()
            value = split[1].strip()
            value = self.convertValue(name, value)
            if hasattr(self, name):
                setattr(self, name, value)
            else:
                warn(f"Wrong setting name '{name}'")

    def createDefault(self):
        content = ""
        for name, value in self.getDefaultValues().items():
            content += f"{name}={value}\n"
        configFilePath = self.getConfigFilePath()
        self.fileSystem.createFileWithContent(configFilePath, content)

    def getDefaultValues(self):
        return {
            "clientAddress": "127.0.0.1",
            "serverAddress": "127.0.0.1",
            "serverPort": 6464,
        }

    def setDefaultValues(self):
        for name, value in self.getDefaultValues().items():
            setattr(self, name, value)

    def convertValue(self, name, value):
        if type(getattr(self, name)) == int:
            return int(value)

        return value

    def getConfigFilePath(self):
        return f"{Environment.programRootPath}\\app.config"
