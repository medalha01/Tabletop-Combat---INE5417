

from Widget import Widget
import tkinter as tk
import random


class CharAction(Widget):
    def __init__(self, window) -> None:
        super().__init__(window)
        self._text = tk.Label(self.frame, text=f"thingamajing {random.random()}")
        self._text.pack(side="top", anchor='w')