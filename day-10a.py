import sqlite3
from pathlib import Path
import json

# movies = json.loads(Path("movies.json").read_text())
# print(movies)

# with sqlite3.connect("db.sqlite3") as conn:
#     command = "INSERT INTO Movies VALUES(?, ?, ?)"
#     for movie in movies:
#         conn.execute(command, tuple(movie.values()))
#     conn.commit()


with sqlite3.connect("db.sqlite3") as conn:
    command = "SELECT * FROM Movies"
    cursor = conn.execute(command)

    # for row in cursor:
    #     print(row)
    movies = cursor.fetchall()
    print(movies)
