

from Widget import Widget
import tkinter as tk


class InitiativeSidebar(Widget):
    def __init__(self, window) -> None:
        super().__init__(window)

        # Character Info

        self._initiave_text = tk.Label(self.frame, text="Initiative", bg="#3B3B3B", 
                                       font=("helvetica", 30), fg="#e3e3e3", padx=10)
        self._initiave_text.pack(side="top")
    
    def update_char_info(self, character_list, speed_used = '0.0'):
        pass
        #...
