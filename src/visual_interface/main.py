import tkinter as tk
from tkinter import *


class VirtualTableTopGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Virtual Table Top")
        self.geometry("800x400")
        self.resizable(True, True)
        self["bg"] = "blue"

        self.setMenu()
        self.setGrid()

    def setMenu(self):
        appMenubar = Menu(self)

        self.config(menu=appMenubar)

        file_menu = Menu(appMenubar)
        matchMenu = Menu(appMenubar)
        characterMenu = Menu(appMenubar)

        file_menu.add_command(label="Connect", command=self.destroy)
        file_menu.add_command(label="Disconnect", command=self.destroy)

        matchMenu.add_command(label="Start Match", command=self.destroy)
        matchMenu.add_command(label="Load Match", command=self.destroy)

        characterMenu.add_command(label="Add Character", command=self.destroy)
        characterMenu.add_command(label="Load Character", command=self.destroy)

        appMenubar.add_cascade(label="Conectar", menu=file_menu)
        appMenubar.add_cascade(label="Match", menu=matchMenu)
        appMenubar.add_cascade(label="Personagem", menu=characterMenu)

    def setGrid(self):
        self.boardView = []
        for i in range(10):
            viewTier = []
            for j in range(10):
                aLabel = Label(
                    self,
                    bd=1,
                    relief="solid",
                    border=1,
                    width=11,
                    height=3,
                    bg="white",
                )
                aLabel.grid(row=i, column=j)
                aLabel.bind("<Button-1>")
                viewTier.append(aLabel)
            self.boardView.append(viewTier)


appFrame = VirtualTableTopGUI()
appFrame.mainloop()
