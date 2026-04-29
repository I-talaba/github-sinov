"""API yaratish"""

from flask import Flask,jsonify,request

import sqlite3


app = Flask(__name__)
def get_db():
    return sqlite3.connect("todo.db")

# table yaratish
conn = sqlite3.connect('todo.db')
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS tasks (
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT,
status TEXT
)""")
conn.commit()
conn.close()

@app.route("/tasks", methods=['GET'])
def get_tasks():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")
    rows = cur.fetchall()
    conn.close()

    html = "<h1>Tasklar</h1>"
    for row in rows:
        if row[2] == "done":
            color = 'green'
            text = f"<s>{row[1]}</s>"
        else:
            color = 'black'
            text = row[1]
        html += f"""
        <p style="color:{color};">{text} ({row[2]})
                
                <a href="/update/{row[0]}">✅ Done</a>
                <a href="/delete/{row[0]}">❌ Delete</a>
        </p>
"""
    html += "<br><a href='/'>Orqaga</a>"
    return html


@app.route("/delete/<int:task_id>",methods=['GET'])
def delete_task(task_id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM tasks WHERE id = ?",(task_id,))
    conn.commit()
    conn.close()
    return jsonify({"message":"o'chirildi"})


@app.route("/update/<int:task_id>",methods=['GET'])
def update_task(task_id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("UPDATE tasks SET status = ? WHERE id = ?",("done",task_id))
    conn.commit()
    conn.close()
    return jsonify({"message":"Yangilandi"})

@app.route("/")
def home():
    return f"""
    <h1 style="color:blue;">ToDo App</h1>
    <form action="/add" method="post">
        <input type="text" name="title" placeholder="Task yozing">
        <button type="submit">Qo'shish</button>
        </form>
        <br>   
    
        <a href="/tasks">Tasklarni ko'rish</a>
    """

@app.route("/add",methods=["POST"])
def add_task():
    title = request.form.get("title")

    conn = get_db()
    cur = conn.cursor()

    cur.execute(
                "INSERT INTO tasks (title,status) VALUES (?,?)",(title,"pending"))
    conn.commit()
    conn.close()
    return "<h3>Qo'shildi✅</h3><a href='/'>Orqaga</a>"


@app.route("/tasks_html")
def tasks_html():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")
    rows = cur.fetchall()
    conn.close()

    html = "<h1>Tasks</h1>"
    for row in rows:
        html += f"<p>{row}</p>"
    return html


if __name__ == "__main__":
    app.run(debug=True)