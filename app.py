from utils import see_all_contacts, add_a_contact, delete_a_contact, search_for_a_contact

def start_routine():
    print('''premere :
          1 per vedere tutti i contatti
          2 per aggiungere un contatto
          3 per eliminare un contatto
          4 per cercare un contatto''')
    
    n = int(input())

    if (n==1):
        see_all_contacts()
    elif(n==2):
        nome = input('inserisci il nome: ')
        cognome = input('inserisci il cognome: ')
        telefono = input('inserisci il telefono: ')
        add_a_contact(nome, cognome, telefono) 
    elif (n==3):
        id=int(input())
        delete_a_contact(id)  
    elif (n==4):
        nome = input()
        cognome = input()
        search_for_a_contact(nome, cognome)
    else:
        print('inserisci un numero valido')
        start_routine()

if __name__ == "__main__":
    start_routine()

