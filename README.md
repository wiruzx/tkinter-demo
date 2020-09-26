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
