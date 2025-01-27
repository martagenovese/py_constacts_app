import sqlite3
connection = sqlite3.connect('data.db')


def see_all_contacts():
    ...

def add_a_contact(nome, cognome, telefono):
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO contatti (nome, cognome, telefono) VALUES (?, ?, ?)", (nome, cognome, telefono))
    connection.commit()
    
def delete_a_contact():
    ...

def search_for_a_contact():
    ...