import tkinter as tk

class First(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # If you want to change text of the Label after it was created, 
        # you need to create a separate variable of type StringVar and call `set` method on it.
        self.label_text = tk.StringVar()
        # Pass it to the Label initializer
        self.label = tk.Label(self, textvariable = self.label_text)
        # if you don't want to change the text, you can just do:
        # self.label = tk.Label(self, text = "First label")

        # pass your function to `command`, and it will be called when you press the button
        self.button = tk.Button(self, text = "First button", command = self.did_press_button)

        self.input = tk.Entry(self)

        # I prefer to have a separate function for setting up the position of views
        self.setup_layout()

    def setup_layout(self):
        views = [self.label, self.button, self.input]
        # enumerate will return new a new array with enumerated elements
        # example: a = ["apple", "banana", "orange"]
        # enumerate(a) = [(0, "apple", (1, "banana"), (2, "orange")]
        for index, view in enumerate(views):
            # sticky here is direction of the compass. North, South, East, West.
            # From Documentation:
            # What to do if the cell is larger than widget. By default, with sticky='', widget is centered in its cell. sticky may be the string concatenation of zero or more of N, E, S, W, NE, NW, SE, and SW, compass directions indicating the sides and corners of the cell to which widget sticks.
            view.grid(row=index, sticky="we")

        # same as:

        # for i in range(len(views)):
        #     view = views[i]
        #     view.grid(row=index, sticky="we")

        # same as:

        # self.label.grid(row=0, sticky="we")
        # self.button.grid(row=1, sticky="we")
        # self.input.grid(row=2, sticky="we")

    def did_press_button(self):
        # `get` will return current text in the input field
        my_input = self.input.get()
        # formatting the string
        new_text = "Your input is: {}".format(my_input)
        # update the text of the label
        # Remember, we're changing the text of StringVar, and the label will get updated automatically
        self.label_text.set(new_text)

