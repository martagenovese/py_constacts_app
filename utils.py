import sqlite3
connection = sqlite3.connect('data.db')


def see_all_contacts():
    
    cur = connection.cursor()
    cur.execute('SELECT * FROM contacts;') #query per vedere tutti i contatti
    result = cur.fetchall()
    print(result)
    # close the cursor
    cur.close()

def add_a_contact():
    ...

def delete_a_contact():
    ...

def search_for_a_contact():
    ...