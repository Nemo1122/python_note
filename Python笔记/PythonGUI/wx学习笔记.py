#hello world

import wx


app = wx.App()
window = wx.Frame(None, title='Python学习', size=(400,300))
panel = wx.Panel(window)

label = wx.StaticText(panel, label='Hello world', pos=(100,100))
window.Show(True)
app.MainLoop()

