## App Description
A simple Kanban board for task management. Every task that you add can be in one of three states:
1. To do
2. Doing
3. Done

## App Walk-through
<img src="https://media.giphy.com/media/Ej0k1HDHPJiCsiUXn7/giphy.gif" width=800><br>

## App Features
- [x] 1. Create a new task
- [x] 2. Move tasks to different states
- [x] 3. Editing tasks
- [x] 4. Deleting tasks
- [ ] 5. Register, Log in and Log out features
- [ ] 6. Collaboration between users and each user can identify their tasks

## Running the App
To run my application, do the following steps in the terminal:

### MacOS
```bash
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
python3 app.py
```

### Windows
```bash
python3 -m venv env
env\Scripts\activate.bat
pip3 install -r requirements.txt
python3 app.py
```

## Testing
The tests.py file contains tests to the app features. To run the file, do the following step in the terminal:

```bash
python3 -m unittest discover tests
```
