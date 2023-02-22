# приветствие 
print( "Добро пожаловать в телефонную книгу") 

filename = "phonebook.json" 
myfile = open(filename, "a+") 
myfile.close 
 
# создание файла .txt для хранения контактной информации 

# def save():
#     with open("phonebook.json","w",encoding="utf-8") as fh:
#         fh.write(json.dumps(phonebook,ensure_ascii=False))
#         print("Наш справочник был успешно сохранен в файле phonebook.json")
# def load():
#     global phonebook
#     with open("phonebook.json","r",encoding="utf-8") as fh:
#         phonebook = json.load(fh)
#     print("Справочник был успешно загружен!")

# Главное меню
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
 
# Определение функции поиска         
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
 
# Имя
def input_firstname(): 
    first = input( "Введите имя: ") 
    remfname = first[1:] 
    firstchar = first[0] 
    return firstchar.upper() + remfname 
 
# Фамилия 
def input_lastname(): 
    last = input( "Введите фамилию: ") 
    remlname = last[1:] 
    firstchar = last[0] 
    return firstchar.upper() + remlname 
 
# Сохранение новых контактных данных
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