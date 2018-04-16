## 3. Connecting to the Database ##

import sqlite3 
conn = sqlite3.connect('jobs.db')



## 6. Creating a Cursor and Running a Query ##

import sqlite3
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

query = "select * from recent_grads;"
cursor.execute(query)
results = cursor.fetchall()
print(results[0:2])

query = "select major from recent_grads"
cursor.execute(query)
majors = cursor.fetchall()
print(majors[:3])

## 8. Fetching a Specific Number of Results ##

import sqlite3
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()
cursor.execute("select Major, Major_category from recent_grads")
five_results = cursor.fetchmany(5)

## 9. Closing the Database Connection ##

conn = sqlite3.connect("jobs.db")
conn.close()

## 10. Practice ##

import sqlite3

class dbopen(object):
    def __init__(self, path):
        self.path = path
        self.conn = None
        self.cursor = None 
    
    def __enter__(self):
        self.conn = sqlite3.connect(self.path)
        self.cursor = self.conn.cursor() 
        return self.cursor
    
    def __exit__(self, exc_class, exc, traceback):
        self.conn.commit()
        self.conn.close()
        
reverse_alphabetical = list()        

with dbopen('jobs2.db') as c:
    c.execute("SELECT Major FROM recent_grads ORDER BY Major DESC")
    reverse_alphabetical = c.fetchall()
    