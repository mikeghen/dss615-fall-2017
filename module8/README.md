# Module 8: Creating Python Projects

# Starting a New Project
1. Start fresh in a clean directory. It's important to keep your file system well organized and to keep projects separate.

:hammer_and_wrench: I always place my projects in a `Projects` directory in my `Documents` directory. When working on a _personal project_ the path the project is always `~/Documents/Projects/project_name`. For companies, I create a company folder and place projects in side that folder, for example: `~/Documents/BenefitsDataTrust/Projects/project_name`.

2. Always create a `README.md` file and write some specifications or _specs_ for your project.

:hammer_and_wrench: As you develop you're project, expand on your `README.md` file. Include information that will allow another programmer read, understand, and get started working with your project. Even if you don't plan to share this project, it will help you when you come back 6 months later and revisit the project.

3. Create a `requirements.txt` file and list out all of the packages you're going to use.

:hammer_and_wrench: This lets you do `pip install -r requirements.txt` to install all the requirements for the project. I think Anaconda has something similar.

4. Have a file that is the entry point to your project (e.g. `main.py`, `server.py`, `app.py`).

:hammer_and_wrench: Projects should be run from the command line: `python main.py` or `python server.py`  

# Subbing Out Your Projects Structure
## Single File Projects
These are not Projects they're just _scripts_.

## Small Projects
For small projects, you can create all your files at the root directory of you project. Consider the file structure for our ETL application:
```
/Documents
  /Projects
    /project_name
      __init__.py
      main.py
      etl.py
```
And you can run the applicaiton like so: `python main.py`. Inside of main.py, we would have something like this:
```python
from etl import tools

# Use tools...
```

## Larger Projects (with reusable logic)
For larger projects, consider creating a _library_ or `lib` directory to store all of your custom python classes and functions. Consider a file structure for a larger ETL application:
```
/Documents
  /Projects
    /project_name
      main.py
      /lib
        etl.py
        database.py
        translator.py
```
In this case, we have a lot of custom code which we could reuse in other project so we store that code in a _library_. Sometimes you need to let the system know where to look for your logic like this (in `main.py`):
```python
# main.py
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)),"lib"))
import etl
import database
import translator

# Use etl, database, translator
```
A little sketchy, I'm sure there's a better way...
