from flask import Flask, render_template, request, redirect, jsonify
import random

app = Flask(__name__)

# In-memory task list
tasks = []

# Home page
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

# Add manual task
@app.route('/add', methods=['POST'])
def add_task():
    task_text = request.form['task']
    if task_text:
        tasks.append({'task': task_text, 'done': False})
    return redirect('/')

# Toggle task done
@app.route('/update/<int:task_id>')
def update_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]['done'] = not tasks[task_id]['done']
    return redirect('/')

# Delete task
@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect('/')

# AI Suggest Task
@app.route('/suggest', methods=['GET'])
def suggest_task():
    suggestions = [
        "Read 10 pages of a book",
        "Practice Python coding",
        "Go for a 10-minute walk",
        "Organize your study desk",
        "Review notes for tomorrow’s class",
        "Write in your journal",
        "Do a quick meditation session"
    ]
    task_text = random.choice(suggestions)
    tasks.append({'task': task_text, 'done': False})  # Save in backend
    return jsonify({"suggestion": task_text})

if __name__== '__main__':
    app.run(debug=True)
