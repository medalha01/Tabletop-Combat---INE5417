from VirtualTableTop.game_logic.visual_interface.AuxWidow import AuxWindow
import tkinter as tk


class CreateCharWindow(AuxWindow):
    def get_window_title(self):
        return "Character Creation"

    def get_window_geometry(self):
        return "300x300"

    def get_status_labels(self):
        return ["Name", "Level", "HP", "Initiative", "CA", "Speed"]

    def open_window(self):
        window = tk.Toplevel()
        self.set_window_properties(window)
        self.create_textboxes(window)
        self.create_retrieve_button(window)


class SettingWindow(AuxWindow):
    def get_window_title(self):
        return "Settings Window"

    def get_window_geometry(self):
        return "500x200"

    def get_status_labels(self):
        return ["Number of Players", "Are you the DM?"]

    def create_checkbox(self, window):
        checkbox_frame = tk.Frame(window, bg="#3B3B3B", padx=5, pady=5)
        checkbox_frame.pack(side="top", fill="x")

        checkbox_label = tk.Label(
            checkbox_frame,
            text="Are you the DM?",
            font=("helvetica", 12),
            bg="#3B3B3B",
            fg="#e3e3e3",
            width=10,
        )
        checkbox_label.pack(side="left")

        checkbox = tk.Checkbutton(checkbox_frame, variable=self.checkbox_value)
        checkbox.pack(side="right", padx=5)

    def open_window(self):
        window = tk.Toplevel()
        self.set_window_properties(window)
        self.create_textboxes(window)
        self.create_retrieve_button(window)
        self.create_checkbox(window)

    def get_values(self):
        return self.textbox_entries


class CreateAction(AuxWindow):
    def get_window_title(self):
        return "Create Action Window"

    def get_window_geometry(self):
        return "300x300"

    def get_status_labels(self):
        return ["Name", "Description", "Damage", "Type", "Range", "Number of Uses"]

    def run_window(self):
        window = tk.Toplevel()
        self.set_window_properties(window)
        self.create_textboxes(window)
        self.create_retrieve_button(window)


class StartMatchWindow(AuxWindow):
    def get_window_title(self):
        return "Start Match Window"

    def get_window_geometry(self):
        return "300x300"

    def get_status_labels(self):
        return ["AAA"]

    def open_window(self):
        window = tk.Toplevel()
        self.set_window_properties(window)
        self.create_textboxes(window)
        self.create_retrieve_button(window)
