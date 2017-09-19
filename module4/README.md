# Python Debugging, Modules, Packages and Testing
* [Debugging](https://docs.python.org/2/library/pdb.html)
* [Modules](https://docs.python.org/3/tutorial/modules.html)
* [Unittest](https://docs.python.org/3/library/unittest.html)

## Modules and Packages
```python
if __name__ == '__main__':
  # Some code...
```
You'll see this in projects and should understand what it's doing. From [StackOverflow](https://stackoverflow.com/questions/419163/what-does-if-name-main-do):

Before executing the code, it will define a few special variables. For example, if the python interpreter is running that module (the source file) as the main program, it sets the special `__name__` variable to have a value "__main__". If this file is being imported from another module, `__name__` will be set to the module's name.

### What does this `__init__.py` file doing?
The __init__.py files are required to make Python treat the directories as containing packages.

For example consider this folder contents:
```
__init__.py
mypackage.py
```
From here
