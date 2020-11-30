import wx
import threading
import block
import subprocess
import random

class Frame(wx.Frame) : # 프레임 생성
    def __init__(self):
        wx.Frame.__init__(self, None, title="Login", style=wx.CLOSE_BOX)
        self.panel = wx.Panel(self, size=(1920, 720))
        self.panel.SetBackgroundColour((0, 0, 0))
        self.index = 0
        self.correct = [8, 5, 6, 9] # 비밀번호 설정
        self.click = []
        self.failCount = 3

        thread = threading.Thread(target=block.cursor, args=(self,), daemon=True)
        thread.start()

        # self.button = wx.Button(self.panel, 0, label="닫기", pos=(100, 100), size=(300, 40))
        # self.Bind(wx.EVT_BUTTON, self.onClose, id=0)
        self.p = []
        count = 1

        self.label = [1, 2, 3, 6, 5, 4, 7, 8, 9]
        random.shuffle(self.label)

        for i in range(400, 601, 100) :
            for j in range(800, 1001, 100) :
                self.p.append(wx.Button(self.panel, count, label=str(self.label[count-1]), pos=(j, i), size=(50, 50)))
                self.Bind(wx.EVT_BUTTON, self.onClick, id=count)
                count += 1

    def onClick(self, event):
        id = event.GetId()
        if id == self.correct[self.index] :
            self.click.append(id)
            self.index += 1
            if self.correct == self.click :
                self.Destroy()
        else :
            self.index = 0
            self.click = []
            self.failCount -= 1

            if(self.failCount == 0) :
                subprocess.call(["shutdown", "-f", "-r", "-t", "1"])

        random.shuffle(self.label)
        for i in range(10):
            self.p[i].SetLabel(str(self.label[i]))

    # def onClose(self, event):  # 닫기버튼
    #     self.Destroy()

app = wx.App(False)

frame = Frame()
print("frame")

frame.SetTransparent(500)
frame.SetWindowStyle(wx.STAY_ON_TOP)
frame.Maximize()

frame.Show()

binput = block.blockInput()
binput.block()

taskThread = threading.Thread(target=block.disTask, daemon=True)
taskThread.start()

app.MainLoop()

