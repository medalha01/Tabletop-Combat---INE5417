import tkinter as tk
from tkinter import Menu
from tkinter import Grid


class VirtualTableTopGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Virtual Table Top")
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
        for i in range(10):
            for j in range(10):
                frame = tk.Frame(master=self, relief=tk.RAISED, borderwidth=1)
                frame.grid(row=i, column=j, padx=2, pady=2)
                label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
                label.pack()


appFrame = VirtualTableTopGUI()
appFrame.mainloop()
