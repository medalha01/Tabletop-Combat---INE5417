from VirtualTableTop.game_logic.visual_interface.Widget import Widget
import tkinter as tk
import random


class CharAction(Widget):
    def __init__(self, window, action) -> None:
        super().__init__(window)
        self._text = tk.Label(self.frame, text=f"{action['name']}\n{action['dices'][0]}d{action['dices'][1]}", font=("arial", 10))
        self._text.bind("<Button-1>", lambda event, t="a", p="blz?": tk.messagebox.askquestion(t,p))
        self._text.pack(side="top", anchor="w")

    