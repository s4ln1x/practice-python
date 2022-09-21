import sqlite3

connection = sqlite3.connect("jeopardy.sqlite")
cursor = connection.cursor()

cursor.execute("SELECT name FROM category LIMIT 10")

results = cursor.fetchall()

print("EXAMPLE categories: \n")

for category in results:
    print(category[0])

connection.close()
