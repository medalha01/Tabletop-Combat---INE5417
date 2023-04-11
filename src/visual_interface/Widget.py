

import tkinter as tk
from abc import ABC


class Widget(ABC):
    def __init__(self, window) -> None:
        super().__init__()

        self._frame = tk.Frame(window, bg="#3B3B3B")
    
    @property
    def frame(self):
        return self._frame