import sqlite3

db_filename = '/tmp/SourceScores.db'
connection = sqlite3.connect(db_filename)
cursor = connection.cursor()
