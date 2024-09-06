from flask import Flask,render_template,redirect,url_for,request
import sqlite3

con = sqlite3.connect('todos.db', check_same_thread=False)


con.row_factory = sqlite3.Row
cursor = con.cursor()


app = Flask(__name__)

def dict_todos():
    con.row_factory = sqlite3.Row
    cursor.execute('select * from todos')
    todos = [dict(r) for r in cursor.fetchall()]
    return todos



@app.route("/", methods=["GET","POST"])
@app.route("/home", methods=["GET","POST"])
def home():
    if(request.method== "POST"):
        todo_name = request.form["todo_name"]
        res = con.execute("select max(id) from todos")
        rows= res.fetchall()
        cur_id = rows[0]
        last_id = cur_id[0]+1


        cursor.execute(""" INSERT INTO todos(id, name, checked) VALUES(?,?,?) """,(last_id,todo_name,False))    
        con.commit()

        return redirect(url_for('home'))
    return render_template("index.html",items=dict_todos())

@app.route("/checked/<int:todo_id>", methods=["POST"])
def checked(todo_id):
    todos = dict_todos()
    for todo in todos:
        if todo['id'] == todo_id:      
            upd_id = todo['id']   
            check_bol = not todo['checked']
            cursor.execute(""" UPDATE todos SET checked  = ? WHERE id = ? """, (check_bol,upd_id,))
            con.commit()
            break
    return redirect(url_for("home"))


@app.route("/delete/<int:todo_id>", methods=["POST"])
def delete(todo_id):
    todos = dict_todos()
    for todo in todos:
        if todo['id'] ==todo_id:
            del_id = todo["id"]
            cursor.execute(""" DELETE FROM todos WHERE id= ? """, (del_id,))
            con.commit()
    return redirect(url_for("home"))



if __name__ == '__main__':
    app.run(debug=True)