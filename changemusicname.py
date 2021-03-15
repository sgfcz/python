import os
import re

os.chdir(r"F:\音乐")
print(os.getcwd())
firstDir = os.getcwd()
firstDirList = os.listdir()

os.chdir(firstDir + "\\" + firstDirList[0])
rockMusic = os.getcwd()
print(rockMusic)

rockMusicList = os.listdir()

for oldFile in rockMusicList:
    newFilename = re.sub("\d\d ", "", oldFile)
    newFilename = re.sub("【有间音乐】", "", newFilename)
    newFilename = re.sub(" \[mqms2\]", "", newFilename)
    newFilename = re.sub("\[weiyun\]", "", newFilename)
    newFilename = re.sub("【妙语视听中心】", "", newFilename)
    os.rename(oldFile, newFilename)

os.chdir(firstDir + "\\" + firstDirList[1])
popMusic = os.getcwd()
print(popMusic)
popMusicList = os.listdir()

for oldFile in popMusicList:
    newFilename = re.sub("\d\d ", "", oldFile)
    newFilename = re.sub("\d\d\.", "", newFilename)
    newFilename = re.sub("【有间音乐】", "", newFilename)
    newFilename = re.sub(" \[mqms2\]", "", newFilename)
    newFilename = re.sub("\[weiyun\]", "", newFilename)
    newFilename = re.sub("【捌零无损音乐】", "", newFilename)
    print(newFilename)
    os.rename(oldFile, newFilename)