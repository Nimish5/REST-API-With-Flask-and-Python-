# Section5 : Storing Resources in SQL Database
# Video 79, 80, 81
import sqlite3

connection = sqlite3.connect("sqldata.db")
cursor = connection.cursor()

table1 = "CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(table1)

# User = [
#     (5, 'Nimish', 'Sexynimish07'),
#     (8, 'Shubham', 'Jainbaba')
#     ]
# query = "INSERT INTO Users VALUES (?, ?, ?)"
# cursor.executemany(query, User)

table2 = "CREATE TABLE IF NOT EXISTS Mobiles (Name text, Mobile text, Company text, Price real, IMEI_No text)"
cursor.execute(table2)

row = ('Neha Pathak Rajvaidya!', 'Iphone-store', 'Apple', 200000, 'NEHAVSSUDS')
query = "INSERT INTO Mobiles VALUES (?, ?, ?, ?, ?)"
cursor.execute(query, row)

connection.commit()
connection.close()