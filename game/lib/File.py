class File:

    @staticmethod
    def readAllFile(filePath):
        f = open(filePath, "r")
        return f.read()
