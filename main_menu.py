""""This is main Menu"""

from sort import sorter_starter
from addressbook import addressbook_starter #заглушка адресбука
from notebook import notes_starter  #функція записника заглушка

def menu():

    COMMANDS = [" 1  - AddressBook📒", " 2  - NoteBook📋", " 3  - Files sorter📂", " 0  - Exit❌"]

    while True:

        print("_"*34)
        print("| {:<3} {:^27}|".format("☰","Welcome to main menu"))
        print('|'+'_'*32 + '|')
        for el in COMMANDS:
            print('|{:<31}|'.format(el))
        print('|'+'_'*32 + '|')
        print('|{:<32}|'.format('Type number to start:  '))
        user_input = input("|✍️  " )
        print('|'+'_'*32 + '|')

        if user_input == '1':
            print("_"*34)
            print("|{:^30}|".format("✨ AddressBook Started! ✨"))
            print("|"+"_"*32 + "|")
    
            addressbook_starter()
        elif user_input == '2':
            print("_"*34)
            print("|{:^30}|".format("✨ NoteBook Started! ✨"))
            print("|"+"_"*32 + "|")
    
            notes_starter()
        elif user_input == '3':
            print("_"*34)
            print("|{:^30}|".format("✨ Files Sorter Started! ✨"))
            print("|"+"_"*32 + "|")

            result = sorter_starter()
            print(result)
        elif user_input == '0':
            print('Goodbye!')
            break
        else:
            print("_"*34)
            print("|{:^32}|".format("Wrong number... Try again..."))
            print("|"+"_"*32 + "|")


if __name__ == '__main__':
    menu()