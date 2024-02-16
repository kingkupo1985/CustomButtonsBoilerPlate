from tkinter import *
from CustomButtonOldBroken import CustomButton
from tkinter.ttk import Progressbar

class LoadingWindow():
    def __init__(self, window):
        # CREATING GUI WINDOW
        height = 430
        width = 530
        self.window = window
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry("{}x{}+{}+{}".format(width, height, x, y))
        self.window.resizable(0, 0)
        self.window.config(background="Black")
        self.window.overrideredirect(1)
        self.center_window(self.window, height=height, width=width)

        # BUTTON STUFF
        self.login_btn = CustomButton(self.window, button_name='Login', command=self.button_clicked)
        self.login_btn.place(x=50, y=50)
        Label(self.window,
              text="Welcome to the Password Manager App",
              background="Black",
              foreground="Yellow",
              ).place(x=135, y=20)

    def exit_window(self):
        self.window.destroy()

    def button_clicked(self):
        print("Button Clicked")

    def center_window(self, window, width, height):  # this function can be removed when added to main app
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        x_position = (screen_width - width) // 2
        y_position = (screen_height - height) // 2

        window.geometry(f"{width}x{height}+{x_position}+{y_position}")
