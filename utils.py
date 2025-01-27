import sqlite3
connection = sqlite3.connect('data.db')


def see_all_contacts():
    ...

def add_a_contact():
    ...

def delete_a_contact(id):
    # create a database cursor
    cur = connection.cursor()

    # query the database for ALL data in the notes table
    cur.execute('DELETE FROM contacts WHERE id = ?', (id, ))

    # print the result
    result = cur.fetchall()
    print(result)

    # close the cursor
    cur.close()

def search_for_a_contact():
    ...