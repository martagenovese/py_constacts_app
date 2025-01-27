def see_all_contacts():
    ...

def add_a_contact():
    ...

def delete_a_contact():
    ...

def search_for_a_contact():
    ...

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
        add_a_contact() 
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

