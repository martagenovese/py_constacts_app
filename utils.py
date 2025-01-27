import sqlite3
connection = sqlite3.connect('data.db')


def see_all_contacts():
    
    cur = connection.cursor()
    cur.execute('SELECT * FROM contacts;') #query per vedere tutti i contatti
    result = cur.fetchall()
    print(result)
    # close the cursor
    cur.close()

def add_a_contact(nome, cognome, telefono):
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO contatti (nome, cognome, telefono) VALUES (?, ?, ?)", (nome, cognome, telefono))
    connection.commit()
    
def add_a_contact():
    ...

def delete_a_contact(id):
    # create a database cursor
    cur = connection.cursor()

    # query the database for ALL data in the notes table
    cur.execute('DELETE FROM contacts WHERE id = '+id+';')

    # print the result
    result = cur.fetchall()
    print(result)

    # close the cursor
    cur.close()

def search_for_a_contact():
    ...