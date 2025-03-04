# 🐍 Debugging Tricks with Python

## The Problem: Stop Debugging Like It’s 1999
Are you tired of debugging by:

- ❌ Adding **tons of print statements**? → **Inefficient**
- ❌ Copy/pasting code into **IPython** randomly? → **Dangerous** (breaks execution order)

There's a **better way**: **Debugging directly inside your code**.
It’s **magical**, powerful, and will change how you debug forever. 

## Why Use **IPython** for Debugging?
**IPython** is an enhanced interactive Python shell that provides features like tab completion, rich history, magic commands, and built-in debugging, making it more powerful than the default Python. 

### **IPython vs Jupyter Notebooks**
| Feature | IPython | Jupyter Notebooks |
|---------|---------|------------------|
| **Execution Order Control** | ✅ Always preserved | ❌ Can run cells out of order |
| **Lightweight** | ✅ Minimal dependencies | ❌ Requires full Jupyter setup |
| **Execute .py Scripts** | ✅ Yes! | ❌ Not directly |
| **Inline Debugging** | ✅ Supports `ipdb` | ⚠️ Limited |

**TL;DR**: **Use IPython** if you're debugging scripts in a controlled, lightweight environment.  
Jupyter notebooks are great for prototyping, but **bad for structured debugging**.

### Install
```bash
pip install ipython
```
### Execute Script
```bash
ipython my_script.py
```
#### Or alternatively:
```bash
ipython
```
followed by:
```bash
run my_script.py
```

## The `debug` Command
If an error occurs, you can use the **`debug` command** in IPython:  
```python
debug
```

### **Debugging Options**
| Command | Description |
|---------|-------------|
| `l` | **List 11 lines** around the current execution line |
| `c` | **Continue execution** until you hit a **breakpoint** or `set_trace()` |
| `s` | **Step into** a function (move deeper into execution) |
| `n` | **Next line** (executes current line & moves forward) |
| `u` | **Move up** the stack (view caller function) |
| `d` | **Move down** the stack (view deeper execution level) |
| `q` or `exit` | **Exit debugger** |


## Setting Breakpoints Manually
Instead of running the entire script, set **breakpoints** where needed. 
Python ``debug`` supports this, but there is a better way of doing this setting a trace.

## **The Pro Debugging Trick: `set_trace()`**
Instead of breakpoints, use `set_trace()` **inside your code**:
```python
import ipdb; ipdb.set_trace()
```
Now, **execution pauses at this line**, and you can inspect variables live!

### ✅ **Advantages**
- Works inside scripts & functions (not just interactive sessions)  
- Lets you analyze variables at runtime 
- Doesn't require knowing line number

### ❌ **Disadvantages**
- Forget to remove it? Your script stops unexpectedly! In Production!
- Solution? Use a pre-commit hook to catch `set_trace()` in your code.

## **Final Takeaways**
Stop using print debugging – embrace **interactive debugging**
Use **IPython**, not Jupyter, for structured debugging
Learn the `debug` **commands** (`c`, `s`, `n`, `u`, `d`)
Use `ipdb.set_trace()` for **deeper debugging & live variable analysis**

### Want More?
- **[Official Python Debugging Docs](https://docs.python.org/3/library/pdb.html)**
- **[IPython Debugging Guide](https://ipython.readthedocs.io/en/stable/interactive/reference.html#debugging)**
