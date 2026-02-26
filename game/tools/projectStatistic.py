# print some project statistics

import os

bigFileLinesCount = 200

pyFilesCount = 0
linesCount = 0
classesCount = 0
bigFilesCount = 0
bigFileNames = []


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
    global bigFilesCount
    _, extension = os.path.splitext(filePath)
    if extension == ".py":
        pyFilesCount += 1
        with open(filePath, "r") as file:
            lines = file.readlines()
            codeLines = 0
            for line in lines:
                if isCodeLine(line):
                    codeLines += 1
                    if line.startswith("class "):
                        classesCount += 1
            linesCount += codeLines
            if codeLines >= bigFileLinesCount:
                bigFilesCount += 1
                bigFileNames.append(filePath)


def analyzeProjectDir(parentPath):
    for childName in os.listdir(parentPath):
        childPath = os.path.join(parentPath, childName)
        if os.path.isfile(childPath):
            analyzeFile(childPath)
        else:
            analyzeProjectDir(childPath)


analyzeProjectDir("D:\\Projects\\Wrath\\game")

print(f"python files count: {pyFilesCount}.")
print(f"python files lines count: {linesCount:,d}.")
print(f"classes count: {classesCount}.")
print(f"big files count: {bigFilesCount}.")
if len(bigFileNames) > 0:
    print(bigFileNames)
