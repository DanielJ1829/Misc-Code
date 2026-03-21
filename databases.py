#databases are the way to store data in computer science
#sql means structured query language

#we're using sqlite3 here but mysql/mongodb are really useful (i'll probs use these more in future)

import sqlite3

#need to a create a database
#we can create a connection to a database
#if a database already exists the connection connects, if not
#it creates a new database

connection = sqlite3.connect('mydata.db')  #creates a file called mydata.db in my python practice folder
#(if i run this for a 2nd,3rd etc it just connects to the database)

#to execute sql queries we need a 'cursor' - this is the object/interface to the database

cursor = connection.cursor()
#pretty much everything now is pure sql, yikes
#create a table
#This statement below creates
#a table (empty) with 3 columns with their corresponding datatypes written after
cursor.execute("""
CREATE TABLE IF NOT EXISTS persons (
    first_name TEXT, 
    last_name TEXT,
    age INTEGER
)
""")
#create table if not exists allows us to create the table and is sql syntax
#if you rerun the code you need the if not exists to not get an error

#insert some data into the table
cursor.execute("DELETE FROM persons")  #due to the re executing code
#continually adding insert code in, this is here to keep only one line in

cursor.execute("""
INSERT INTO persons VALUES
('Paul', 'Jones', 28),
('Mark', 'Smith', 46),
('Gemma', 'McFarlane', 34),
('James', 'Smith', 26)
""")

#select some rows from the table and print them out:
#( '*' denotes everything)
# if you keep re executing the code it just keeps adding stuff in
cursor.execute("""
SELECT * FROM persons
WHERE last_name = 'Smith'
""")

rows = cursor.fetchall()
print(rows)

#we can try loading the database entries into our script as objects and vice versa




#everything you execute isn't applied until you commit
#cursor executes the statement and the statement is in the connection but you need
#connection.commit to apply it to the database
connection.commit()
connection.close()   #remember commit(), it is really important !!!!!!!!