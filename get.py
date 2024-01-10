import os

# Get the base directory of your Django project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Construct the path to your SQLite database file
database_path = os.path.join(BASE_DIR, 'db.sqlite3')

print(database_path)

