import sqlite3

connection = sqlite3.connect("jeopardy.sqlite")
cursor = connection.cursor()

cursor.execute("SELECT text, answer, value FROM clue LIMIT 10")

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
