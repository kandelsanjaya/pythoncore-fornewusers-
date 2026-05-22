## 1. Installing python

**Windows/macOS/Linux:** Download from [python.org](https://www.python.org/downloads/)

## 2. Installing 'uv'

Type the following commands to install the _uv_ package manager for python.
#### Windows (Powershell)
_irm [https://astral.sh/uv/install.ps1](https://astral.sh/uv/install.ps1) | iex_

#### macOS and Linux (Terminal)
_curl -LsSf [https://astral.sh/uv/install.sh](https://astral.sh/uv/install.sh) | sh_

# 3. Creating project Environment

First, create a new folder/directory for the project.
Now, inside the newly created folder, open terminal -> [Alt + D -> type 'cmd']

**In the terminal, type the command:**
_python -m venv .venv_

Now activate the environment with the command:

**Windows:** 
_.venv\Scripts\activate_
**macOS/Linux**: 
_source .venv/bin/activate_

# 4. Installing Django
In the same terminal window:
Write the command:
_uv pip install django_

# 5. Creating the Django Project

First, create the Django project structure by using the command:
_django-admin startproject my_project ._

Then, to create an app in the project, use:
_python manage.py startapp core_

# 6. Initializing the project with migrations

After creating the project, the first migrations need to be performed in order to launch the server.
**Use these commands in succession:**

_python manage.py makemigrations_
_python manage.py migrate_

After the migrations are done, you will see a 'db.sqlite3' file in project's root directory. This means the server is ready for launch.

**Launch the development server with:**
_python manage.py runserver_

**Visit [localhost:8000 or 127.0.0.1:8000] to access the django launch page.**

You have successfully created a Django Project.










