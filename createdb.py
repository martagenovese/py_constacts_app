import sqlite3

#
# Establishing connection
#

# open a SQLite connection
# a database file called data.db will be created,
# if it does not exist
connection = sqlite3.connect('data.db')

# create a database cursor
cur = connection.cursor()

#
# Creating the table
#

# create the database table if it doesn't exist
table_schema = """
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome varchar(30) NOT NULL,
    cognome varchar(30) NOT NULL,
    telefono char(10) NOT NULL UNIQUE
);
"""
cur.execute(table_schema)

#
# Cleaning up
#

# close the cursor
cur.close()

# close the connection
connection.close()