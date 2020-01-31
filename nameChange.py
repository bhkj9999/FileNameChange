import os, sys

if sys.platform == 'win32':
    PatchDisk = os.getcwd() + r'\Data\zhCN'
    wowDisk = os.getcwd()

noPatchWords = 'NoCDpatch-zhCN-2.MPQ'
haveCDPatchWords = 'haveCDpatch-zhCN-2.MPQ'
patchWords = 'patch-zhCN-2.MPQ'

def GetFile():
    os.chdir(PatchDisk)

    files = os.listdir(os.getcwd())
    fileList = []

    try:
        for i in files:
            if ( patchWords in i ):
                p1 = i
            if ( noPatchWords in i ):
                p2 = i
            elif ( haveCDPatchWords in i ):
                p2 = i
    except Exception as e:
        return e

    fileList.append(p1)
    fileList.append(p2)

    return fileList

GetFile()