from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

#set up the application
app = Flask(__name__)

#location of database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['DEBUG'] = True

#initialize database
db = SQLAlchemy(app)
db.init_app(app)

#data added as placeholders
@app.before_first_request
def write_data():
    db.drop_all()
    db.create_all()
    db.session.add(Todo(content= "Call mom and cry", status="todo"))
    db.session.add(Todo(content= "Go to the park with Aroma and Richie", status="doing"))
    db.session.add(Todo(content= "Do the dishes", status="todo"))
    db.session.add(Todo(content= "Go to Pride", status="done"))
    db.session.add(Todo(content= "Clean the living room", status="todo"))
    db.session.add(Todo(content= "Leetcode", status="doing"))
    db.session.add(Todo(content= "Exercise", status="todo"))
    db.session.add(Todo(content= "Get flowers", status="todo"))
    db.session.commit()

#create model
class Todo(db.Model):
    #task id
    id = db.Column(db.Integer, primary_key=True)
    #task description
    content = db.Column(db.String(200), nullable=False)
    #time task is created
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    #status of task
    status = db.Column(db.String(5), nullable = False)


@app.route('/', methods=['POST', 'GET'])
def index():
    '''
    Function that creates the homepage and new tasks
    '''
    tasks = None

    if request.method == 'POST':
        #pass id of content to be accessed
        task_content = request.form['content']
        
        #new task instance and status
        new_task = Todo(content=task_content, status = 'todo')
        
        #db contents inorder of creation
        tasks = Todo.query.order_by(Todo.date_created).all()

        try:
            #add
            db.session.add(new_task)
            #commit
            db.session.commit()
            #back to homepage
            return redirect(url_for('index'))
        #if there is an error
        except Exception:
           return "Error encountered when pushing task"

    #assign appropriate status to tasks
    todo = Todo.query.filter_by(status='todo').all()
    doing = Todo.query.filter_by(status ='doing').all()
    done = Todo.query.filter_by(status = 'done').all()
    return render_template('index.html', todo = todo, doing = doing, done=done, tasks = tasks)

@app.route('/delete/<int:id>')
def delete(id):
    '''
    Function that deletes tasks
    '''
    #find task
    #if task not found, return 404 error
    task_to_delete = Todo.query.get_or_404(id)

    try:
        #delete
        db.session.delete(task_to_delete)
        #commit
        db.session.commit()
        #back to homepage
        return redirect(url_for('index'))
    #if there is an error
    except Exception:
        return "Error encountered when deleting task"

@app.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id):
    '''
    Function that edits tasks
    '''
    #find task
    task_to_update = Todo.query.get(id)
    
    if request.method == 'POST':
        #add the update to task list
        task_to_update.content = request.form['content']

        #update from database
        try:
            #commit
            db.session.commit()
            #go back to homepage
            return redirect(url_for('index'))

        #if there is an error
        except Exception:
            return "Error encountered when editing task"
    else:
        #document that the app reads from
        return render_template('update.html', task=task_to_update)

@app.route('/move_to_todo/<int:id>',methods=['POST', 'GET'])
def move_to_todo(id):
    '''
    Function that moves tasks from doing to todo
    '''

    #find task
    #if task not found, return 404 error
    task_to_move_to_todo = Todo.query.get_or_404(id)

    #change status from doing to todo
    if task_to_move_to_todo.status == 'doing':
        task_to_move_to_todo.status = 'todo'

        #commit
        db.session.commit()

        #back to homepage
        return redirect(url_for('index'))

    return redirect(url_for('index'))


@app.route('/move_to_doing/<int:id>',methods=['POST', 'GET'])
def move_to_doing(id):
    '''
    Function that moves tasks to and from doing
    '''

    #find task
    #if task not found, return 404 error
    task_to_move_to_doing = Todo.query.get_or_404(id)

    #change status from todo to doing
    if task_to_move_to_doing.status == 'todo':
        task_to_move_to_doing.status = 'doing'
        db.session.commit()
        return redirect(url_for('index'))

    #change status from done to doing
    elif task_to_move_to_doing.status == 'done':
        task_to_move_to_doing.status = 'doing'
        db.session.commit()
        return redirect(url_for('index'))

    return redirect(url_for('index'))

@app.route('/move_to_done/<int:id>',methods=['POST', 'GET'])
def move_to_done(id):
    '''
    Function that moves tasks from doing to done 
    '''

    #find task
    #if task not found, return 404 error
    task_to_move_to_done = Todo.query.get_or_404(id)

    #change status from doing to done
    if task_to_move_to_done.status == 'doing':
        task_to_move_to_done.status = 'done'
        db.session.commit()
        return redirect(url_for('index'))

    return redirect(url_for('index'))


if __name__ == "__main__":
    #incase of errors, the webpage will display them
    app.run(debug=True)