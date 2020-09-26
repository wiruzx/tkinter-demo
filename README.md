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
tkinter.Tk.__doc__ # Will print doc for Tk
```
