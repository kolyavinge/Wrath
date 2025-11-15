import os

pyFilesCount = 0
linesCount = 0
classesCount = 0


def isCodeLine(line):
    line = line.strip()
    if len(line) == 0:
        return False
    if line[0] == "#":
        return False

    return True


def analyzeFile(filePath):
    global pyFilesCount
    global linesCount
    global classesCount
    _, extension = os.path.splitext(filePath)
    if extension == ".py":
        pyFilesCount += 1
        with open(filePath, "r") as file:
            lines = file.readlines()
            for line in lines:
                if isCodeLine(line):
                    linesCount += 1
                    if line.startswith("class "):
                        classesCount += 1


def analyzeDir(parentPath):
    for childName in os.listdir(parentPath):
        childPath = os.path.join(parentPath, childName)
        if os.path.isfile(childPath):
            analyzeFile(childPath)
        else:
            analyzeDir(childPath)


analyzeDir("D:\\Projects\\Wrath\\game")

print(f"python files count: {pyFilesCount}")
print(f"python files lines count: {linesCount:,d}")
print(f"classes count: {classesCount}")
