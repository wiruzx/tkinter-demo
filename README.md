# How to import code from other files in Python:

**apple.py**
```python
def latest_iphone():
    return "iPhone 11 Pro"
```

**google.py**
```python
import apple # just put the name of the file without .py extension

def search(str):
    if str == "What is the latest iPhone version":
        return apple.latest_iphone()
    ...
```

# But what if I don't want to type name of the module every time

If you don't want to type name of the module every time you create an object or call a function, instead of `import apple` you can do:

```python
from apple import *
```

this will make all the classes and functions from `apple` module available right away:

```python
# instead of
apple.latest_iphone()
# you can just write
latest_iphone()

```

# How to get all methods of a class:

Imagine you have a class `Tk` in the module `tkinter`

You can get all the methods that class `Tk` has by using `dir` function:

```python
dir(tkinter.Tk) # will return list of all class names
```

```python
dir(tkinter) # will return list of all classes and functions in the module
```

Some classes have `__doc__` property, so you can get more detailed documentation:

```python
tkinter.Tk.__doc__ # Will return doc for Tk
```

Although sometimes documentation is not very useful:
> ```python
> tkinter.Tk.mainloop.__doc__ #'Call the mainloop of Tk.'
> ```
