import tkinter as tk

class Second(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        photo_image = tk.PhotoImage(file="image.gif")
        self.image_label = tk.Label(self, image = photo_image)
        self.image_label.photo_image = photo_image
        self.setup_layout()

    def setup_layout(self):
        self.image_label.grid(row = 0, column = 0)
