import os
import re


def renameFileSuffix(filePath):
    files = os.listdir(filePath)
    for fileName in files:
        os.chdir(filePath)
        portion = os.path.splitext(fileName)
        prefix = re.sub(u"\\(.*?\\)|\\{.*?}|\\[.*?]", "", portion[0])
        try:
            if portion[1] == ".下载":
                # 例： a(1).js.下载 -> a.js
                newName = prefix + ""
                os.rename(fileName, newName)
            else:
                newName = prefix + portion[1]
                os.rename(fileName, newName)
        except FileExistsError:
            pass


if __name__ == "__main__":
    #递归所有文件夹
    rootPath = "C:\\Users\weixuan.ge\\Desktop\\泛微"
    for i in os.walk(rootPath):
        for dir in i[1]:
            abspath = i[0] + "\\" + dir
            print("处理目录： ", abspath)
            renameFileSuffix(abspath)
