import sqlite3

connection = sqlite3.connect("jeopardy.sqlite")
cursor = connection.cursor()

# Get a random game
cursor.execute("SELECT game FROM category ORDER BY RANDOM() LIMIT 1")

results = cursor.fetchall()
game_id = results[0][0]
print(f'Categories for game #{game_id}:')

# Get the categories for that game

query = """SELECT name, round FROM category WHERE game={0} ORDER BY
round""".format(game_id)
cursor.execute(query)
results = cursor.fetchall()

for result in results:
    name, round_ = result

    print(f'Round {round_}: {name}')

connection.close()
