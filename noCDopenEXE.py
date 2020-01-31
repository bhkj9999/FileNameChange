import os
from nameChange import GetFile, wowDisk, PatchDisk, noPatchWords, haveCDPatchWords, patchWords

os.chdir(PatchDisk)


def noCDOpen():
    patchFile = GetFile()[0]
    anotherPatchFile = GetFile()[1]
    # os.rename(str(patchFile), 'patch-zhCN-2.MPQ')

    if anotherPatchFile == haveCDPatchWords:
        return
    if anotherPatchFile == noPatchWords:
        os.rename(patchWords, haveCDPatchWords)
        os.rename(noPatchWords, patchWords)
        return


def openWowFile():
    filePlace = wowDisk
    os.startfile(filePlace + '\Wow.exe')


if __name__ == '__main__':
    noCDOpen()
    openWowFile()