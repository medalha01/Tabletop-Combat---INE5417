from VirtualTableTop.game_logic.visual_interface.AuxWidow import AuxWindow
import tkinter as tk


class CreateCharWindow(AuxWindow):
    def get_window_title(self):
        return "Character Creation"

    def get_window_geometry(self):
        return "400x500"

    def get_status_labels(self):
        return ["Name", "Color", "Position", "Level", "HP", "Initiative", "CA", "Speed"]

    def open_window(self):
        self.textbox_entries["actions"] = []
        self.window = tk.Toplevel()
        self.set_window_properties()
        self.create_textboxes()
        self.create_window_button()
        self.create_retrieve_button()

    def create_window_button(self, ):
        button = tk.Button(self.window, text="Add Actions", command=self.create_action_window)
        button.pack()

    def create_action_window(self):
        window = CreateAction()
        window.run_window(self)
    
    def retrieve_values(self):
        char = {"name": self.textbox_entries["Name"].get(), "color": self.textbox_entries["Color"].get(), "position": tuple(map(int, self.textbox_entries["Position"].get().split(','))), 
                "level": self.textbox_entries["Level"].get(), "hp_max": int(self.textbox_entries["HP"].get()), 
                "initiative": int(self.textbox_entries["Initiative"].get()), "ca": int(self.textbox_entries["CA"].get()), 
                "speed": float(self.textbox_entries["Speed"].get()), "actions": self.textbox_entries["actions"]}
        self.interface.make_character(char)
        self.window.destroy()

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
        # self.create_checkbox()

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
        return "400x500"

    def get_status_labels(self):
        return ["Name", "Type", "Dices", "Roll\nBonus", "Effect\nBonus", "Range", "Area of\nEffect", "Number of\nUses"]

    def run_window(self, char_wind):
        self.char_wind = char_wind
        self.window = tk.Toplevel()
        self.set_window_properties()
        self.create_textboxes()
        self.create_retrieve_button()
    
    def retrieve_values(self):
        action = {"name": self.textbox_entries["Name"].get(), "type": self.textbox_entries["Type"].get(), 
                  "dices": list(map(int, self.textbox_entries["Dices"].get().split(','))), "roll_bonus": int(self.textbox_entries["Roll\nBonus"].get()), 
                  "dmg_bonus": int(self.textbox_entries["Effect\nBonus"].get()), "range": float(self.textbox_entries["Range"].get()), 
                  "aoe_radius": int(self.textbox_entries["Area of\nEffect"].get()), "max_amount": int(self.textbox_entries["Number of\nUses"].get())}
        self.char_wind.textbox_entries["actions"].append(action)
        self.window.destroy()
        


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
