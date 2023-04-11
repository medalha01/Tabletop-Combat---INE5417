

import tkinter as tk
from tkinter import *
from CharacterSidebar import CharacterSidebar


class VirtualTableTopGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Virtual Table Top")
        self.geometry("800x600")

        self.setMenu()
        self.setBar()
        self.setGrid(10)

    def setMenu(self):
        appMenubar = Menu(self)

        self.config(menu=appMenubar)

        file_menu = Menu(appMenubar)
        matchMenu = Menu(appMenubar)
        characterMenu = Menu(appMenubar)

        file_menu.add_command(label="Connect", command=self.destroy)
        file_menu.add_command(label="Disconnect", command=self.destroy)

        matchMenu.add_command(label="Start Match", command=self.destroy)
        matchMenu.add_command(label="Configure Match", command=self.destroy)

        characterMenu.add_command(label="Add Character", command=self.destroy)
        characterMenu.add_command(label="Load Character", command=self.destroy)

        appMenubar.add_cascade(label="Conectar", menu=file_menu)
        appMenubar.add_cascade(label="Match", menu=matchMenu)
        appMenubar.add_cascade(label="Personagem", menu=characterMenu)

    def setBar(self):

        self._sidebar_char = CharacterSidebar(self)

        #sidebar_char = tk.Frame(self, bg="#3B3B3B", width=200)
        self._sidebar_char.frame.pack(side="left", fill="y")

        sidebar_init = tk.Frame(self, bg="#3B3B3B", width=100)
        sidebar_init.pack(side="right", fill="y")

    """         self.button1 = tk.Button(
            sidebar_char,
            text="Botão 1",
            font=("Helvetica", 14),
            bg="#535353",
            fg="white",
            relief="flat",
            command=self.on_button1_click,
        )
        self.button1.pack(pady=10, padx=20, fill="x")

        self.button2 = tk.Button(
            sidebar_char,
            text="Botão 2",
            font=("Helvetica", 14),
            bg="#535353",
            fg="white",
            relief="flat",
            command=self.on_button2_click,
        )
        self.button2.pack(pady=10, padx=20, fill="x")

        self.button3 = tk.Button(
            sidebar_char,
            text="Botão 3",
            font=("Helvetica", 14),
            bg="#535353",
            fg="white",
            relief="flat",
            command=self.on_button3_click,
        )
        self.button3.pack(pady=10, padx=20, fill="x") """

    def setGrid(self, size: int):
        grid_frame = tk.Frame(self)
        grid_frame.pack(side="right", fill="both", expand=True)

        self.cells = []
        for i in range(size):
            row = []
            for j in range(size):
                cell = tk.Label(
                    grid_frame,
                    text=f"{i}, {j}",
                    font=("Helvetica", 14),
                    bg="#F7F7F7",
                    fg="#333",
                    relief="solid",
                    width=9,
                    height=4,
                )
                cell.grid(row=i, column=j, padx=1, pady=1)
                row.append(cell)
            self.cells.append(row)

    def on_button1_click(self):
        self.button1.config(bg="#32a852")
        self.button2.config(bg="#535353")
        self.button3.config(bg="#535353")
        self.update_cells_text("Botão 1 clicado")

    def on_button2_click(self):
        self.button1.config(bg="#535353")
        self.button2.config(bg="#32a852")
        self.button3.config(bg="#535353")
        self.update_cells_text("Botão 2 clicado")

    def on_button3_click(self):
        self.button1.config(bg="#535353")
        self.button2.config(bg="#535353")
        self.button3.config(bg="#32a852")
        self.update_cells_text("Botão 3 clicado")

    def update_cells_text(self, text):
        for row in self.cells:
            for cell in row:
                cell.config(text=text)


appFrame = VirtualTableTopGUI()
appFrame.mainloop()
