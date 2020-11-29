import wx
import win32api
import threading

def cursor() :
    while True :
        position = win32api.GetCursorPos()
        if position[0] >= 1920 :
            win32api.SetCursorPos((1920, position[1]))

app = wx.App()

entries = [wx.AcceleratorEntry() for i in range(2)]

entries[0].Set(wx.ACCEL_ALT, wx.WXK_F4, 0, None)

accel = wx.AcceleratorTable(entries)

title = "Login"

frame = wx.Frame(parent = None, title = title, style=wx.CLOSE_BOX)

#frame.Bind(wx.EVT_LEAVE_WINDOW, wx.MessageBox('EVT_LEAVE_WINDOW','EVT_LEAVE_WINDOW',wx.OK))
# wx.MouseState().SetPosition(self=this, pos=wx.Point(0, 0)))

thread = threading.Thread(target=cursor)
thread.start()

frame.SetTransparent(1)
frame.SetAcceleratorTable(accel)
frame.SetWindowStyle(wx.STAY_ON_TOP)
frame.Maximize()

frame.Show()
app.MainLoop()