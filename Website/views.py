from flask import Blueprint,request,render_template,url_for,redirect
from . import db
from .models import Task
views = Blueprint('views',__name__)

@views.route('/')
def showindex():
    from .models import Task
    tasks = Task.query.all() 
    return render_template('index.html',tasks = tasks)

@views.route('/add',methods=['GET','POST'])
def add():
    
    if request.method == "POST": 
        content = request.form.get("content")
        if content:
            new_task = Task(content=content)
            db.session.add(new_task)
            db.session.commit()
            return redirect(url_for('views.showindex'))
    else:
        return "failure"
    
@views.route('/update_task/<int:id>',methods=['POST'])
def update_task(id):
    task = Task.query.get_or_404(id)
    new_content = request.form.get("content")
    if new_content:
        task.content = new_content
        db.session.commit()
        return redirect(url_for('views.showindex'))
    else:
        return "<h2><center>no new content written</center></h2>"

@views.route('/delete_task/<int:id>')
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('views.showindex'))