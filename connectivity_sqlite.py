import sqlite3
cursor=sqlite3.connect('mydb.db')
cursor.execute('CREATE TABLE stud(roll int, name varchar)')
print('table created')
cursor.execute(""" INSERT INTO stud  VALUES (1,'SUNDAY') ,(2,'monday'), (3,'saturday')""")
cursor.commit()
t=cursor.execute("SELECT * FROM stud")
for i in t:
    print(i)
cursor.execute("UPDATE stud SET name ='wednesday' WHERE roll =1")
t=cursor.execute("SELECT * FROM stud")
for i in t:
    print(i)
cursor.execute("delete from stud WHERE roll=1")
t=cursor.execute("SELECT * FROM stud")
for i in t:
    print(i)