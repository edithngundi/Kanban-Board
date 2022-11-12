# Kanban board

## Description

A Kanban board is a simple form of task management. Every task that you add can
be in one of three states:

1. To do
2. Doing
3. Done

Your assignment is to write a flask application which provides the functionality
associated with a Kanban board. This includes:
1. Creating a new task
2. Moving tasks to different states
3. Deleting tasks

Please find a few example Kanban board websites and use them so that you have a
clear idea of what is needed. (Note that the professional versions look much
nicer and have many more bells and whistles than are asked for in this
assignment!)

**(Optional)** As an extension, make a personalizable Kanban board. This means
that every user has their own account, and can see only their own tasks.  For
this you will need to create users, and be able to log them in and out.  Each
task will also need to be associated with a particular user.

## Submission
Your primary submission must be a pdf listing of your python code, but you must
also include a zip file containing all the code and documentation. Your readme
must include a short description of the structure of the project. Be sure to
highlight any extra features that you’ve implemented.

## Installation
As part of your submission you must include a zip file with all the necessary
code and html, a requirements.txt file, and a `README.md` file. To get your
application to run should only require the following steps:

### MacOS
```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 app.py
```

### Windows
```bash
python3 -m venv venv
venv\Scripts\activate.bat
pip3 install -r requirements.txt
python3 app.py
```

Please make sure that the virtual environment `venv` is **not** included in 
the zip file. (Virtual environments are not portable, and if you installed it 
on your laptop then it is unlikely to work anywhere else.)

## Testing
The project must also include appropriate unit tests. These unit tests should be
run using the following command (while in the project’s root directory):

```bash
python3 -m unittest discover test
```
