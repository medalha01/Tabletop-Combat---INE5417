from AuxWidow import AuxWindow


class CreateCharWindow(AuxWindow):
    def get_window_title(self):
        return "Character Creation"

    def get_window_geometry(self):
        return "300x300"

    def get_status_labels(self):
        return ["Name", "Level", "HP", "Initiative", "CA", "Speed"]

    def run_window(self):
        window = tk.Toplevel()
        self.set_window_properties(window)
        self.create_textboxes(window)
        self.create_retrieve_button(window)

    def get_values(self):
        return self.textbox_entries


class SettingWindow(AuxWindow):
    def get_window_title(self):
        return "Settings Window"

    def get_window_geometry(self):
        return "300x300"

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

    def run_window(self):
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

    def get_values(self):
        return self.textbox_entries


class StartMatchWindow(AuxWindow):
    def get_window_title(self):
        return "Start Match Window"

    def get_window_geometry(self):
        return "300x300"

    def get_status_labels(self):
        return ["AAA"]

    def run_window(self):
        window = tk.Toplevel()
        self.set_window_properties(window)
        self.create_textboxes(window)
        self.create_retrieve_button(window)

    def get_values(self):
        return self.textbox_entries

    def get_match_info(self):
        return self.textbox_entries
