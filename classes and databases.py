import sqlite3
class Person:

    first: str

    def __init__(self, idno=-1, first="", last="", age=-1):
        self.idno = idno
        self.first = first
        self.last = last
        self.age = age
        self.connection = sqlite3.connect('mydata.db')
        self.cursor = self.connection.cursor()    #have to say self.connection since connection isn't defined
#normally in a database you have a unique identifier (eg national insurance number)

    def load_person(self,idno):   #can use the database to load in a specific person, see the code below
        self.cursor.execute("""
        SELECT * FROM persons
        WHERE id = {}
        """.format(idno))

        results = self.cursor.fetchone()
        if results is None:
            raise ValueError(f"No person found with id {idno}")
        self.idno = idno
        self.first = results[1]
        self.last = results[2]
        self.age = results[3]

    def insert_person(self):  #insert a person into the database from the class Person
        self.cursor.execute("""
        INSERT INTO persons VALUES
        ({}, '{}', '{}', '{}')   #you need quotation marks around the placeholders for strings/text, same thing happens in the database
        """.format(self.idno, self.first, self.last, self.age))
        self.connection.commit()  #you need this every time to do anything, it won't work otherwise
        self.connection.close()

    def remove_person(self):  #removing the specific person before adding them back in prevents the database dieing
        self.cursor.execute(f"""
        DELETE FROM persons WHERE id = {self.idno}
        """)
        self.connection.commit() #close() as sql can't act on a closed db
#standard code for the databse(32 lines)
'''connection = sqlite3.connect('mydata.db')
cursor = connection.cursor()
cursor.execute("DELETE FROM persons")
cursor.execute("DROP TABLE IF EXISTS persons") #'CREATE TABLE IF NOT EXISTS' does nothing if it's already created, therefore
#you can't edit the table or add columns and stuff if the table already exists without deleting the table first. kinda clunky tbh
cursor.execute("""
CREATE TABLE IF NOT EXISTS persons (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    age INTEGER
)
""")

cursor.execute("""
INSERT INTO persons (id, first_name, last_name, age) VALUES
(1, 'Paul', 'Jones', 28),
(2, 'Mark', 'Smith', 46),
(3, 'Gemma', 'McFarlane', 34),
(4, 'James', 'Smith', 26)
""")

cursor.execute("""
SELECT * FROM persons
WHERE last_name = 'Smith'
""")

rows = cursor.fetchall()
print(rows)
connection.commit()
connection.close()'''
#code to retrieve a person from the database (5 lines)
'''
p1 = Person()
p1.load_person(1) #loads the person with idno 1
print(p1.first, p1.last, p1.age, p1.idno)
connection = sqlite3.connect('mydata.db')
connection.close()
'''
#code to add/remove people from the db (10 lines)
'''
p1 = Person(7, "Alex", "Robinson", 30)
p1.remove_person()
p1.insert_person()
connection = sqlite3.connect('mydata.db')
cursor = connection.cursor()

cursor.execute("SELECT * FROM persons")
results = cursor.fetchall()
print(results)
connection.close()
'''