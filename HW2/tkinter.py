import Tkinter as tk
import os


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit',
            command=self.quit)
        self.quitButton.grid()

root = tk.Tk()
root.attributes('-fullscreen', True)
root.configure(background='black')

app = Application()
app.master.title('Sample application')
app.mainloop()