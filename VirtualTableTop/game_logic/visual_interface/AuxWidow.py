import tkinter as tk
from abc import ABC


class AuxWindow(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.checkbox_value = None
        self.textbox_entries = {}

    def open_window(self):
        self.window = tk.Toplevel()
        self.set_window_properties()
        self.create_textboxes()
        self.create_retrieve_button()
        return self.window

    def set_window_properties(self):
        self.window.title(self.get_window_title())
        self.window.geometry(self.get_window_geometry())
        return self.window

    def get_status_labels(self):
        pass
    
    def get_window_title(self):
        pass

    def get_window_geometry(self):
        pass

    def set_interface(self, interface):
        self.interface = interface

    def create_textboxes(self):
        status = self.get_status_labels()
        for i, label in enumerate(status):
            label_frame = tk.Frame(self.window, bg="#3B3B3B", padx=5, pady=5)
            label_frame.pack(side="top", fill="x", padx=10, expand=True)  # ???

            textbox_label = tk.Label(
                label_frame,
                text=label,
                font=("helvetica", 12),
                bg="#3B3B3B",
                fg="#e3e3e3",
                width=10,
                anchor="w"  # ancora no canto esquerdo
            )
            textbox_label.pack(side="left", padx=(0, 10))  # Ajustar X como necessario

            textbox = tk.Entry(label_frame)
            textbox.pack(side="right", expand=True, fill="x", padx=5)


            self.textbox_entries[label] = textbox
            self.window.configure(bg=textbox_label["bg"])

    def create_retrieve_button(self):
        # Create the retrieve button in the window
        button_frame = tk.Frame(self.window, bg="#3B3B3B", padx=5, pady=5)
        button_frame.pack(side="top", fill="x")

        retrieve_button = tk.Button(
            button_frame,
            text="Retrieve Values",
            command=lambda: self.retrieve_values(),
        )
        retrieve_button.pack(side="bottom", pady=10)

    def retrieve_values(self):
        # Retrieve the values from the textbox entries
        for label, entry in self.textbox_entries.items():
            value = entry.get()
            print(f"{label}: {value}")

        # Close the window
        self.window.destroy()
        return self.textbox_entries

    def notify_invalid_value(self, mensagem):
        tk.messagebox.showinfo("Warning", mensagem)
