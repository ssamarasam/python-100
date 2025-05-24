# working with json

import json
from pathlib import Path

movies = [
    {"id": 1, "name": "Terminator", "year": 1989},
    {"id": 2, "name": "Titanic", "year": 1995},
]

data = json.dumps(movies)
print(data)

Path("movies.json").write_text(data)
