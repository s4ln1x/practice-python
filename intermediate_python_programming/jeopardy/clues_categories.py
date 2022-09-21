import sqlite3

connection = sqlite3.connect("jeopardy.sqlite")
cursor = connection.cursor()

# Get a random game
cursor.execute("SELECT id, name FROM category ORDER BY RANDOM() LIMIT 1")

results = cursor.fetchall()
category_id, category_name = results[0]
print(category_name)

# Get the categories for that game
query = """SELECT text, answer, value FROM clue
WHERE category={0} LIMIT 10""".format(category_id)
cursor.execute(query)
results = cursor.fetchall()

for clue in results:
    question, answer, value = clue

    # Format
    # [$200]
    # Question: stuff
    # Answer: What if 'stuff'

    print(f'[${value}]')
    print(f'Question: {question}')
    print(f"Answer: What if '{answer}'\n")

connection.close()
