import os
from nameChange import GetFile, wowDisk, PatchDisk, noPatchWords, haveCDPatchWords, patchWords

os.chdir(PatchDisk)


def HaveCdOpen():
    patchFile = GetFile()[0]
    anotherPatchFile = GetFile()[1]
    # os.rename(str(patchFile), 'patch-zhCN-2.MPQ')

    if anotherPatchFile == noPatchWords:
        return
    if anotherPatchFile == haveCDPatchWords:
        os.rename(patchWords, noPatchWords)
        os.rename(haveCDPatchWords, patchWords)
        return


def openWowFile():
    filePlace = wowDisk
    os.startfile(filePlace + '\Wow.exe')


if __name__ == '__main__':
    HaveCdOpen()
    openWowFile()