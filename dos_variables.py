import wx

class MiPanel(wx.Panel):
    # Acá el boton es child de MiPanel
    def __init__(self, parent):
        super().__init__(parent)
        boton = wx.Button(self, label='Apretá')

class MiFrame(wx.Frame):
    # Acá la instancia de MiPanel es child de MiFrame
    def __init__(self):
        super().__init__(None, title='Implemento un botón')
        panel = MiPanel(self)
        self.Show()

if __name__ == '__main__':
    app = wx.App(redirect=False)
    frame = MiFrame()
    app.MainLoop()