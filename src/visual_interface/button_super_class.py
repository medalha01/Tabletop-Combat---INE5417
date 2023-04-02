import tkinter as tk


class AppButton:
    def __init__(self, tkGui, imagePath):
        self.relief = [tk.SUNKEN, tk.RAISED, tk.GROOVE, tk.RIDGE, tk.FLAT]
        self.buttonImage = tk.PhotoImage(file=imagePath)
        self.tkGui = tkGui
        self.buttonBody = tk.Button(
            tkGui,
            text="Virtual Table Top test",
            image=self.buttonImage,
            compound=tk.LEFT,
            command=self.disableBtn,
        )

    def createBtn(self):
        btn = tk.Button(self.tkGui, text=self.relief[0], relief=self.relief[0])
        btn.pack(padx=50, pady=50, side=tk.LEFT)
        return btn

    def disableBtn(self):

        self.returnBtn().config(state=tk.DISABLED)

    def returnBtn(self):

        return self.buttonBody
