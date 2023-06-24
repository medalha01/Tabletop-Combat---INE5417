

from VirtualTableTop.game_logic.visual_interface.AuxWidow import AuxWindow
import tkinter as tk


class StartMatchWindow(AuxWindow):
    def get_window_title(self):
        return "Start Match Window"

    def get_window_geometry(self):
        return "300x300"

    def get_status_labels(self):
        return ["Number \nof Players", "Are you \nthe DM?"]
    
    def create_textboxes(self):
        status = self.get_status_labels()
        self.dropDownList = []
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
            textbox_label.pack(side="left", padx=(0, 10))
            if label == "Are you \nthe DM?":
                options = ["Yes", "No"]
                dropdown = tk.StringVar(label_frame)
                dropdown.set('Yes')
                dropdown_menu = tk.OptionMenu(label_frame, dropdown, *options)
                dropdown_menu.pack(side="top", fill="x", padx=10, expand=True)
                self.dropDownList.append(dropdown)
            else:
                textbox = tk.Entry(label_frame)
                textbox.pack(side="right", expand=True, fill="x", padx=5)
                self.textbox_entries[label] = textbox
                self.window.configure(bg=textbox_label["bg"])

    def open_window(self):
        self.window = tk.Toplevel()
        self.set_window_properties()
        self.create_textboxes()
        self.create_retrieve_button()
    
    def retrieve_values(self):
        try:
            if (self.dropDownList[0].get() == 'Yes'):
                isMaster = True
            else:
                isMaster = False
            self.interface.start_match(isMaster, int(self.textbox_entries["Number \nof Players"].get()))
            self.window.destroy()
        except Exception as exc:
            self.notify_invalid_value(f"Invalid value: {exc}")

class SettingWindow(AuxWindow):
    def get_window_title(self):
        return "Settings Window"

    def get_window_geometry(self):
        return "500x200"

    def get_status_labels(self):
        return ["Size \nof board", "Background \nImage"]
    
    def create_textboxes(self):
        status = self.get_status_labels()
        self.dropDownList = []
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
            textbox_label.pack(side="left", padx=(0, 10))
            if label == "Background \nImage":
                options = ["stone.jpg", "grass.jpg", "dirty.png", "sand.png", "wood.png"]
                dropdown = tk.StringVar(label_frame)
                dropdown.set("grass.jpg")
                dropdown_menu = tk.OptionMenu(label_frame, dropdown, *options)
                dropdown_menu.pack(side="top", fill="x", padx=10, expand=True)
                self.dropDownList.append(dropdown)
            else:
                textbox = tk.Entry(label_frame)
                textbox.pack(side="right", expand=True, fill="x", padx=5)
                self.textbox_entries[label] = textbox
                self.window.configure(bg=textbox_label["bg"])

    def open_window(self):
        self.window = tk.Toplevel()
        self.set_window_properties()
        self.create_textboxes()
        self.create_retrieve_button()

    def retrieve_values(self):
        try:
            settings = {"board_size" : int(self.textbox_entries["Size \nof board"].get()), 
                        "filename": self.textbox_entries["Background \nImage"].get()}
            self.interface.send_match_settings(settings)
            self.window.destroy()
        except Exception as exc:
            self.notify_invalid_value(f"Invalid value: {exc}")

class CreateCharWindow(AuxWindow):
    def get_window_title(self):
        return "Character Creation"

    def get_window_geometry(self):
        return "400x500"

    def get_status_labels(self):
        return ["Name", "Color", "Position", "Level", "HP", "Initiative", "CA", "Speed"]
    
    def create_textboxes(self):
        status = self.get_status_labels()
        self.dropDownList = []
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
            textbox_label.pack(side="left", padx=(0, 10))
            if label == "Color":
                options = ["Red", "Blue", "Purple", "Yellow", "Green", "Orange", "Pink", "Brown", "Black", "White", "Gray"]
                dropdown = tk.StringVar(label_frame)
                dropdown.set('Red')
                dropdown_menu = tk.OptionMenu(label_frame, dropdown, *options)
                dropdown_menu.pack(side="top", fill="x", padx=10, expand=True)
                self.dropDownList.append(dropdown)
            else:
                textbox = tk.Entry(label_frame)
                textbox.pack(side="right", expand=True, fill="x", padx=5)
                self.textbox_entries[label] = textbox
                self.window.configure(bg=textbox_label["bg"])

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
        window.open_window(self)
    
    def retrieve_values(self):
        try:
            char = {"name": self.textbox_entries["Name"].get(), "color": self.dropDownList[0].get(), "position": tuple(map(int, self.textbox_entries["Position"].get().split(','))), 
                    "level": self.textbox_entries["Level"].get(), "hp_max": int(self.textbox_entries["HP"].get()), 
                    "initiative": int(self.textbox_entries["Initiative"].get()), "ca": int(self.textbox_entries["CA"].get()), 
                    "speed": float(self.textbox_entries["Speed"].get()), "actions": self.textbox_entries["actions"]}
            self.interface.make_character(char)
            self.window.destroy()
        except Exception as exc:
            self.notify_invalid_value(f"Invalid value: {exc}")

class CreateAction(AuxWindow):
    def get_window_title(self):
        return "Create Action Window"

    def get_window_geometry(self):
        return "400x500"

    def get_status_labels(self):
        return ["Name", "Type", "Dices", "Roll\nBonus", "Effect\nBonus", "Range", "Area of\nEffect", "Number of\nUses"]

    def open_window(self, char_wind):
        self.char_wind = char_wind
        self.window = tk.Toplevel()
        self.set_window_properties()
        self.create_textboxes()
        self.create_retrieve_button()
    
    def create_textboxes(self):
        status = self.get_status_labels()
        self.dropDownList = []
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
            textbox_label.pack(side="left", padx=(0, 10))
            if label == "Type":
                options = ["Attack", "Heal"]
                dropdown = tk.StringVar(label_frame)
                dropdown.set("Attack")
                dropdown_menu = tk.OptionMenu(label_frame, dropdown, *options)
                dropdown_menu.pack(side="top", fill="x", padx=10, expand=True)
                self.dropDownList.append(dropdown)
            else:
                textbox = tk.Entry(label_frame)
                textbox.pack(side="right", expand=True, fill="x", padx=5)
                self.textbox_entries[label] = textbox
                self.window.configure(bg=textbox_label["bg"])

    def retrieve_values(self):
        try:
            action = {"name": self.textbox_entries["Name"].get(), "type": self.dropDownList[0].get().lower(), 
                    "dices": list(map(int, self.textbox_entries["Dices"].get().split(','))), "roll_bonus": int(self.textbox_entries["Roll\nBonus"].get()), 
                    "dmg_bonus": int(self.textbox_entries["Effect\nBonus"].get()), "range": float(self.textbox_entries["Range"].get())+1, 
                    "aoe_radius": int(self.textbox_entries["Area of\nEffect"].get()), "max_amount": int(self.textbox_entries["Number of\nUses"].get())}
            self.char_wind.textbox_entries["actions"].append(action)
            self.window.destroy()
        except Exception as exc:
            self.notify_invalid_value(f"Invalid value: {exc}")
