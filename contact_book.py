#a contact book Program
#we will be able:
# 1) add a contact
# 2)view all contacts
# 3)search contact by Name
# 4)Delete a contact
# 5)quit the program
contacts=[]
menu=('1. Add a contact','2. View Contacts','3. Search contact by name','4. Delete a contact','q to quit')
running=True
while running:
    print('--------------MENU------------')
    for item in menu:
        print(item)
    print('-------------------------------')
    choice=input('Input: ').strip()
    if choice=='1':
        print('--------------------Add contact-------------')
        while True:
            name=input('Enter name(q to quit): ').strip()
            if name=='q':
                break
            else:
                number=input('Enter number: ')
                print('Contact added!')
                contacts.append({"name":name,"number":number})
                print('----------------------------')
            
    elif choice=='2':
        if not contacts:
            print('No Contacts Yet!')
        else:
            for contact in contacts:
                print(f'Name: {contact['name']}' )
                print(f'Telephone: {contact['number']}')
                
        
    elif choice=='3':
        print('--------SEARCH A CONTACT------------')
        found_1=False
        while True:
            srch_contact=input('Enter name of contact(q to quit): ').strip()
            if srch_contact.lower()=='q':
                break
            else:
                found_1=False
                for contact in contacts:
                    if srch_contact  in contact:
                        for key, value in contact.items():
                            print(f'{key} : {value}')
                            print('-------')
                        found_1=True
                        break
            if not found_1:
                print(f'{srch_contact} is not a contact')
        
    elif choice=='4':
        print('--------DELETE A CONTACT------------')

        while True:
            del_name=input('Enter name of contact to delete(q to quit): ')
            if del_name.lower()=='q':
                break
            else:
                found_2=False
                for contact in contacts:
                    if del_name  in contact:
                        contacts.remove(contact)
                        print(f'{del_name} has been deleted')
                        found_2=True
                        break
            if not found_2:
                print(f'{del_name} is not a contact')
                        
    elif choice=='q':
        running=False
    else:
        print('Invalid Choice')
