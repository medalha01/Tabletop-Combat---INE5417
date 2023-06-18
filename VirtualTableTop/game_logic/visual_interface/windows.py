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
        self.create_window_button(window)

    def create_window_button(self, parent_window):
        button = tk.Button(parent_window, text="Add Actions", command=self.create_action_window)
        button.pack()

    def create_action_window(self):
        window = CreateAction()
        window.run_window()

class SettingWindow(AuxWindow):
    def get_window_title(self):
        return "Settings Window"

    def get_window_geometry(self):
        return "500x200"

    def get_status_labels(self):
        return ["Size \nof board", "Background \nImage"]

    def create_checkbox(self, window):
        checkbox_frame = tk.Frame(window, bg="#3B3B3B", padx=5, pady=5)
        checkbox_frame.pack(side="top", fill="x")

        # checkbox_label = tk.Label(
        #     checkbox_frame,
        #     text="Are you the DM?",
        #     font=("helvetica", 12),
        #     bg="#3B3B3B",
        #     fg="#e3e3e3",
        #     width=10,
        # )
        # checkbox_label.pack(side="left")

        # checkbox = tk.Checkbutton(checkbox_frame, variable=self.checkbox_value)
        # checkbox.pack(side="right", padx=5)

    def open_window(self):
        self.window = tk.Toplevel()
        self.set_window_properties()
        self.create_textboxes()
        self.create_retrieve_button()
        self.create_checkbox()

    def get_values(self):
        return self.textbox_entries

    def retrieve_values(self):
        settings = {"board_size" : int(self.textbox_entries["Size \nof board"].get()), 
                    "filename": self.textbox_entries["Background \nImage"].get()}
        self.interface.send_match_settings(settings)
        self.window.destroy()

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
        return ["Number \nof Players", "Are you \nthe DM?"]

    def open_window(self):
        self.window = tk.Toplevel()
        self.set_window_properties()
        self.create_textboxes()
        self.create_retrieve_button()
    
    def retrieve_values(self):
        print(bool(self.textbox_entries["Are you \nthe DM?"].get()), int(self.textbox_entries["Number \nof Players"].get()))
        self.interface.start_match(bool(self.textbox_entries["Are you \nthe DM?"].get()), int(self.textbox_entries["Number \nof Players"].get()))
        self.window.destroy()
