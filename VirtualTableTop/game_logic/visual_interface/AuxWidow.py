import tkinter as tk
from abc import ABC


class AuxWindow(ABC):
    def __init__(self, window) -> None:
        super().__init__()

    def __init__(self):
        self.textbox_entries = {}

    def open_window(self):
        window = tk.Toplevel()
        self.set_window_properties(window)
        self.create_textboxes(window)
        self.create_retrieve_button(window)
        return window

    def set_window_properties(self, window):
        window.title(title)
        window.geometry(self.get_window_geometry())
        return window

    @abstractmethod
    def get_window_title(self):
        pass

    @abstractmethod
    def get_window_geometry(self):
        pass

    def create_textboxes(self, window):
        # Create the textboxes in the window
        status = self.get_status_labels()
        for i, label in enumerate(status):
            label_frame = tk.Frame(window, bg="#3B3B3B", padx=5, pady=5)
            label_frame.pack(side="top", fill="x")

            textbox_label = tk.Label(
                label_frame,
                text=label,
                font=("helvetica", 12),
                bg="#3B3B3B",
                fg="#e3e3e3",
                width=10,
            )
            textbox_label.pack(side="left")

            textbox = tk.Entry(label_frame)
            textbox.pack(side="right", expand=True, fill="x", padx=5)

            self.textbox_entries[label] = textbox

    def create_retrieve_button(self, window):
        # Create the retrieve button in the window
        button_frame = tk.Frame(window, bg="#3B3B3B", padx=5, pady=5)
        button_frame.pack(side="top", fill="x")

        retrieve_button = tk.Button(
            button_frame,
            text="Retrieve Values",
            command=lambda: self.retrieve_values(window),
        )
        retrieve_button.pack(side="bottom", pady=10)

    def retrieve_values(self, window):
        # Retrieve the values from the textbox entries
        for label, entry in self.textbox_entries.items():
            value = entry.get()
            print(f"{label}: {value}")

        # Close the window
        window.destroy()

    def notifyInvalidValue(self, mensagem):
        messagebox.showinfo("Warning", mensagem)
