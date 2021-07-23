import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE Credentials (id int, username text, password text)"
cursor.execute(create_table)
# To insert/ store single user in the database
user = (5, "Nimish", "ravimotu")
insert_data = "INSERT INTO Credentials VALUES (?, ?, ?)"
cursor.execute(insert_data, user)

# To insert/ store multiple users/ tuples in the database
users = [
    (10, "Papa", "Hemalata_P"),
    (8, "Neha", "Sudhu")
]
cursor.executemany(insert_data, users)

# How to reterive data from the database
select_query = "SELECT * From Credentials"
for row in cursor.execute(select_query):
    print(row)

connection.commit()

connection.close()