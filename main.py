import tkinter as tk

from first import *
from second import *

# tk.Frame - Similar to TPanel.
# I prefer to create Frame for each logical and visual combination of the views.
# I also have main Frame for the whole application

# Here we create a subclass of tk.Frame called Application.
# Application will have all the methods and properties of Frame, but we can also add our own
class Application(tk.Frame):
    def __init__(self, parent):
        # We need to call the same method on super.
        # Super is a way to call methods on your supercalss.
        super().__init__(parent)
        self.create_widgets()
        self.setup_layout()

    def create_widgets(self):
        self.first = First(self)
        self.second = Second(self)

    def setup_layout(self):
        self.first.grid(row = 0)
        self.second.grid(row = 1)

main_window = tk.Tk()

app = Application(main_window)
app.pack()

app.mainloop()
