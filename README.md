Запускаем приветствие: print( "Добро пожаловать в телефонную книгу") 
 
Создаём файл .json для хранения контактной информации 

filename = "phonebook.json" 
myfile = open(filename, "a+") 
myfile.close 
 
Оформляем главное меню

 def main_menu(): 
    print( "\nМЕНЮ\n") 
    print( "1. Показать все контакты") 
    print( "2. Добавить новый контакт") 
    print( "3. Поиск контакта") 
    print( "4. Выход") 
    choice = input("Введите пункт меню: ") 
    if choice == "1": 
        myfile = open(filename, "r+") 
        filecontents = myfile.read() 
        if len(filecontents) == 0: 
            print( "В телефонной книге такого контакта нет") 
        else: 
            print(filecontents) 
        myfile.close 
        enter = input("Нажмите Enter для продолжения ...") 
        main_menu() 
    elif choice == "2": 
        newcontact() 
        enter = input("Нажмите Enter для продолжения ...") 
        main_menu() 
    elif choice == "3": 
        searchcontact() 
        enter = input("Нажмите Enter для продолжения ...") 
        main_menu() 
    elif choice == "4": 
        print("До свидания!") 
    else: 
        print( "Пожалуйста введите корректные данные\n") 
        enter = input( "Нажмите Enter для продолжения ...") 
        main_menu() 
 
 
Задаём определение функции поиска         

def searchcontact(): 
    searchname = input( "Введите имя для поиска контакта: ") 
    remname = searchname[1:] 
    firstchar = searchname[0] 
    searchname = firstchar.upper() + remname 
    myfile = open(filename, "r+") 
    filecontents = myfile.readlines() 
      
    found = False 
    for line in filecontents: 
        if searchname in line: 
            print( "Ваш контакт:", end = " ") 
            print( line) 
            found = True 
            break 
    if found == False: 
        print( "Данный контакт недоступен в телефонной книге", searchname) 
 
Задаём Имя

def input_firstname(): 
    first = input( "Введите имя: ") 
    remfname = first[1:] 
    firstchar = first[0] 
    return firstchar.upper() + remfname 
 
Задаём Фамилию

def input_lastname(): 
    last = input( "Введите фамилию: ") 
    remlname = last[1:] 
    firstchar = last[0] 
    return firstchar.upper() + remlname 
 
Сохраняем новые контактные данные

def newcontact(): 
    firstname = input_firstname() 
    lastname = input_lastname() 
    phoneNum = input( "Введите номер телефона: ") 
    emailID = input( "Введите email: ") 
    contactDetails =("[" + firstname + " " + lastname + ", " + phoneNum + ", " + emailID +  "]\n") 
    myfile = open(filename, "a") 
    myfile.write(contactDetails) 
    print( "Контактная инфформация:\n " + contactDetails + "\успешно сохранена!") 

main_menu()
