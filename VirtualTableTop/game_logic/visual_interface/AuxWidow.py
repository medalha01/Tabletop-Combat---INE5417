import tkinter as tk
from abc import ABC


class AuxWindow(ABC):
    def __init__(self, window) -> None:
        super().__init__()

    def setTopLevel(self, windowTitle, GeometryString):
        textboxes_window = Toplevel()
        textboxes_window.title(windowTitle)
        textboxes_window.geometry(GeometryString)

    def notifyInvalidValue(self, mensagem):
        messagebox.showinfo("Warning", mensagem)

    def setScreen(self):
        status = ["Name", "Level", "HP", "Initiative", "CA", "Speed"]
        for i in range(6):
            label_frame = tk.Frame(textboxes_window, bg="#3B3B3B", padx=5, pady=5)
            label_frame.pack(side="top", fill="x")

            textbox_label = tk.Label(
                label_frame,
                text=status[i],
                font=("helvetica", 12),
                bg="#3B3B3B",
                fg="#e3e3e3",
                width=10,
            )
            textbox_label.pack(side="left")

            textbox = tk.Entry(label_frame)
            textbox.pack(side="right", expand=True, fill="x", padx=5)
