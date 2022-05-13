import os


def printTextFileNames():
    fileDir = os.getcwd()
    fileExt = ".txt"

    for element in os.listdir(fileDir):
        if element.endswith(fileExt):
            fullPath = os.path.join(fileDir, element)
            mTime = os.path.getmtime(fullPath)
            print(str(element) + "\t" + str(mTime))


if __name__ == '__main__':
    printTextFileNames()
