import os


class FileSystem:

    def fileExists(self, filePath):
        return os.path.isfile(filePath)

    def readAllFile(self, filePath):
        if filePath is None or len(filePath) == 0:
            raise Exception("Path cannot be empty.")

        with open(filePath, "r") as f:
            return f.read()

    def getDirectoryName(self, path):
        return os.path.dirname(path)

    def getFilesInDirectory(self, path):
        if path is None or len(path) == 0:
            raise Exception("Path cannot be empty.")

        return [f"{path}\\{file}" for file in os.listdir(path)]

    def findFilesByExtension(self, path, extension):
        if path is None or len(path) == 0:
            raise Exception("Path cannot be empty.")
        if extension is None or len(extension) == 0:
            raise Exception("Extension cannot be empty.")

        return [f"{path}\\{file}" for file in os.listdir(path) if file.endswith(extension)]
