class File:

    @staticmethod
    def readAllFile(filePath):
        with open(filePath, "r") as f:
            return f.read()
