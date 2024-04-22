# import mysql.connector
# mydb= mysql.connector.connect(host='localhost',user='root',password='')
# mycursor =mydb.cursor()

# mycursor.execute('SHOW DATABASES ')
# for i in mycursor:
#     print(i)


#using try and except is optional we can perform insert without using it.................

# import mysql.connector
# try:
#     mydb=mysql.connector.connect(host='localhost',user='root',password='',database='mypy')


# #create a table 
# # mycursor.execute('CREATE TABLE stud(roll int,name varchar(255))')

# #insert into the table
# # query=('INSERT INTO stud VALUES(%s,%s)')
# # record=[(1,'rahul'),(2,'yuvraj'),(3,'vidhey')]
#     query=('INSERT INTO stud VALUES(%s,%s)')
#     record=[(4,'ajay'),(5,'john')]
#     mycursor = mydb.cursor()
#     mycursor.executemany(query,record)  #for multiple record insert use executemany()
#     mydb.commit()
#     print('record inserted ')
# except mysql.connector.Error as error:
#     print('failed to insert ')
# finally:
#     if(mydb.is_connected()):
#         mycursor.close()
#         mydb.close()
#         print('sql is closed')

#----------------------------------------------------------------------------

import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='',database='mypy')
mycursor=mydb.cursor()

#display the data
# mycursor.execute('SELECT * FROM stud')
# result=mycursor.fetchall()
# for i in result:
#     print(i)

#update the data 
# mycursor.execute("UPDATE stud SET name='Ram' WHERE roll=1")
# mydb.commit()

#delete the data
mycursor.execute("DELETE FROM stud WHERE roll=2")
mydb.commit()