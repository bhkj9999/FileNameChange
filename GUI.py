import PySimpleGUI as sg
import haveCDopenEXE, noCDopenEXE

# Create some widgets
# wowText = sg.Text("输入魔兽世界目录（即根目录）")
wowText = sg.Text("魔兽世界公共cd（patch-zhcn-2）切换器")
# wowtext_entry = sg.InputText()
ok_btn = sg.Button('打开无共CD版魔兽世界')
ok2_btn = sg.Button('打开有共CD版魔兽世界')
cancel_btn = sg.Button('关闭软件')
# fileBrowser = sg.FolderBrowse()

# Test
# testButton = sg.Button('测试输入')


layout = [
    # [wowText, wowtext_entry, fileBrowser],
    [ok_btn, ok2_btn, cancel_btn]
]
 
# Create the Window
window = sg.Window('魔兽世界公共CD版本选择器', layout)
 
# Create the event loop
while True:
    event, values = window.read()
    if event in (None, '关闭软件'):
        # User closed the Window or hit the Cancel button
        break
    if event in ('打开无共CD版魔兽世界'):
        noCDopenEXE.noCDOpen()
        noCDopenEXE.openWowFile()
    if event in ('打开有共CD版魔兽世界'):
        haveCDopenEXE.HaveCdOpen()
        haveCDopenEXE.openWowFile()
    if event in ('测试输入'):
        print(values['Browse'])
 
window.close()