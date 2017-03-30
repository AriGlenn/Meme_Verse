import sqlite3 as lite

con = lite.connect('test43.db')

cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS Contacts")
cur.execute("CREATE TABLE Contacts (First Name TEXT, Last Name TEXT, Phone TEXT, Email TEXT);")

con.commit()


cur.execute("INSERT INTO Contacts VALUES (?, ?, ?, ?);", ('firstname', 'lastname', 'phone', 'email'))
con.commit()





cursor = con.execute("SELECT First Name, Last Name, Phone, Email  from Contacts")
for row in cursor:
   print("First Name = ", row[0])
   print("Last Name = ", row[1])
   print("Phone = ", row[2])
   print("Email = ", row[3], "\n")

con.close()
