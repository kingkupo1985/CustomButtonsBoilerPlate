import tkinter as tk
from PIL import Image, ImageTk
from os.path import join
from button_images import button_images
class CustomButton(tk.Canvas):
    def __init__(self, master=None, button_name=None, corner_radius=8, command=None, **kwargs):
        super().__init__(master, bd=0, highlightthickness=0, relief="flat", **kwargs)
        self.button_name = button_name
        self.corner_radius = corner_radius
        self.photo_image = None
        self.load_images()
        self.current_image = self.base_image
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        self.bind("<Button-1>", self.on_press)
        self.bind("<ButtonRelease-1>", self.on_release)
        # self.width, self.height = self.base_image.width(), self.base_image.height()
        # self.config(width=self.width, height=self.height)

    def load_images(self):
        images = button_images.get(self.button_name)
        print(self.button_name)
        for i in images.items():
            print(f"Key: {i[0]}, Value: {i[1]}")
        self.base_image = self.load_image(images['base'])
        self.hover_image = self.load_image(images['hover'])
        self.pressed_image = self.load_image(images['pressed']) if images['pressed'] else self.hover_image

    def load_image(self, filename):
        path = join("images", filename)
        image = Image.open(path)
        image = image.resize((self.winfo_reqwidth(), self.winfo_reqheight()))
        self.photo_image = ImageTk.PhotoImage(image)
        self.create_image(0, 0, anchor="nw", image=self.photo_image)
        self.create_rounded_rectangle(0, 0, self.winfo_reqwidth(), self.winfo_reqheight(), fill="", outline="")
        return ImageTk.PhotoImage(image)

    def create_rounded_rectangle(self, x1, y1, x2, y2, **kwargs):
        radius = self.corner_radius
        self.create_arc(x1, y1, x1 + 2*radius, y1 + 2*radius, start=90, extent=90, **kwargs)
        self.create_arc(x2 - 2*radius, y1, x2, y1 + 2*radius, start=0, extent=90, **kwargs)
        self.create_arc(x1, y2 - 2*radius, x1 + 2*radius, y2, start=180, extent=90, **kwargs)
        self.create_arc(x2 - 2*radius, y2 - 2*radius, x2, y2, start=270, extent=90, **kwargs)
        self.create_rectangle(x1 + radius, y1, x2 - radius, y2, **kwargs)
        self.create_rectangle(x1, y1 + radius, x2, y2 - radius, **kwargs)

    def update_image(self, image):
        self.current_image = image

    def on_enter(self, event):
        self.update_image(self.hover_image)

    def on_leave(self, event):
        self.update_image(self.base_image)

    def on_press(self, event):
        self.update_image(self.pressed_image)

    def on_release(self, event):
        self.update_image(self.base_image)
