def show_menu():
    print('1. Распечатать справочник'
          '2. Найти телефон по фамилии'
          '3. Изменить номер телефона'
          '4. Удалить запись'
          '5. Найти абонента по номеру телефона'
          '6. Добавить абонента в справочник'
          '7. Закончить работу', sep = '\n')
    choice=int(input())
    return choice

def work_with_phonebook():
    choice=show_menu()
    phone_book = read_txt('phonebook.txt')
    while (choice!=7):
        if choice==1:
            print(phone_book)
        elif choice==2:
            last_name=input('lastname ')
            print(find_by_lastname(phone_book,last_name))
        elif choice==3:
            last_name=input('lastname ')
            new_number=input('new number ')
            print(change_number(phone_book,last_name,new_number))
        elif choice==4:
            lastname=input('lastname ')
            print(delete_by_lastname(phone_book,lastname))
        elif choice==5:
            number=input('number ')
            print(find_by_number(phone_book,number))
        elif choice==6:
            user_data=input('new data ')
            add_user(phone_book,user_data)
            write_txt('phonebook.txt', phone_book)

        choice=show_menu()
 
Иванов,	Иван,	111,	описаниеИванова
Петров,	Петр,	222,	описаниеПетрова
Васичкина,	Василиса,	333,	описаниеВасичкиной
Питонов,	Антон,	777,	умеет_вПитон
       
def read_txt(filename):
    phone_book=[]
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
    print(list(zip(fields)))    
    with open(filename,'w', encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields,  line.split(',')))
            data.append(record)
            print(record)
    return phone_book

print()
  
def write_txt(filename , phone_book):
    with open('phonebook.txt','w',encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                
                s = s + v + ','
                
            phout.write(f'{s[:-1]}\n')
work_with_phonebook() 

n = int(input('введите номер копируемой строки: '))
def copy_txt(filename , phone_book):
    with open('phonebook.txt', encoding='utf-8') as source, open ('phonebook_1.txt', 'w', encoding='utf-8') as destination:
        for line in source:
            if line.strip(n):
                destination.write(line)
                phone_book_2 = read_txt('phonebook_1.txt')
                print(phone_book_2)
