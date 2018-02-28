# TDT4140: Group 95
[![Build Status](https://travis-ci.org/Strand94/Munin.svg?branch=master)](https://travis-ci.org/Strand94/Munin)
[![Coverage Status](https://coveralls.io/repos/github/Strand94/TDT4140/badge.svg)](https://coveralls.io/github/Strand94/TDT4140)
[![Munin: Version](https://img.shields.io/badge/munin-v1.0.0-blue.svg)](https://github.com/Strand94/TDT4140)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

<br>
Group work in TDT4140 Software development.

To start the application you need to download the ZIP file and unzip it.
Open the project in an IDE (we have been using PyCharm).

Make a pyhton virtual enviroment (virtualenv), with the name venv, and place it in the project folder.

Navigate to the project map in the terminal and run:
```bash
cd venv/Scripts/
activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt
```
Make sure you have the virtual enviroment activated (It should say (venv) on the far left of you terminal)
To activate venv run:
```cd venv/scripts/ activate.bat ```

If you want to run the server from the commandline run:
```python manage.py runserver```
