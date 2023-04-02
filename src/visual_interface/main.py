import tkinter as tk
from button_super_class import AppButton


class VirtualTableTopGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        button = AppButton(self, "../../assets/python.gif")
        self.btn = button.returnBtn()
        self.btn.pack(padx=50, pady=50, side=tk.LEFT)

    def sayhi(self):
        print("hi")


app = VirtualTableTopGUI()
app.title("Virtual Table Top")
app.mainloop()
