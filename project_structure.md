Команда: "tree /A /F"


Структура папок
Серийный номер тома: 0A1D-0703
C:.
|   .gitignore
|   alembic.ini
|   install-poetry.py
|   poetry.lock
|   project_structure.md
|   pyproject.toml
|   README.md
|   test.db
|
+---.idea
|   |   .gitignore
|   |   misc.xml
|   |   modules.xml
|   |   project.iml
|   |   vcs.xml
|   |   workspace.xml
|   |
|   \---inspectionProfiles
|           profiles_settings.xml
|
+---nomad_task_manager
|       __init__.py
|
\---src
    |   main.py
    |   __init__.py
    |
    +---config
    |   |   database.py
    |   |   __init__.py
    |   |
    |   +---migration
    |   |       env.py
    |   |
    |   \---__pycache__
    |           database.cpython-312.pyc
    |           __init__.cpython-312.pyc
    |
    +---frontend
    |   +---static
    |   |   +---css
    |   |   |       style.css
    |   |   |
    |   |   \---js
    |   |           app.js
    |   |
    |   \---templates
    |           index.html
    |
    +---migration
    |   |   env.py
    |   |   README
    |   |   script.py.mako
    |   |   __init__.py
    |   |
    |   \---versions
    +---users
    |   |   models.py
    |   |   routers.py
    |   |   schemas.py
    |   |   __init__.py
    |   |
    |   \---__pycache__
    |           models.cpython-312.pyc
    |           routers.cpython-312.pyc
    |           schemas.cpython-312.pyc
    |           __init__.cpython-312.pyc
    |
    \---__pycache__
            main.cpython-312.pyc
            __init__.cpython-312.pyc
