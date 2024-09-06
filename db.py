import sqlite3

con = sqlite3.connect("todos.db")

cursor = con.cursor()

cursor.execute(
    """CREATE TABLE IF NOT EXISTS todos(
                                        id INTEGER PRIMARY KEY,
                                        name TEXT,
                                        checked BIT)"""
)

con.commit()


# todos = [
#     {
#         'id': 1,
#         'name': 'Write SQL',
#         'checked': False
#     },
#     {
#         'id': 2,
#         'name': 'Write Python',
#         'checked': True
#     }
# ]



# res = cursor.execute("select * from todos")
# res.fetchall()

#con.executemany(""" INSERT INTO todos(id ,name ,checked ) VALUES (:id, :name, :checked)""",todos)

con.commit()

