import random
fi=input("Введите название файла 'books.csv' или 'books-en.csv':")
if fi!='books-en.csv' and fi!="books.csv":
    print("Неверно указано название файла")
f=open(fi)
test=open('test.txt',"w")
head=f.readline()#Считываем заголовок
a=[]#Вводим список для информации про книги
spisok=[]
for s in f:#Проходим по файлу
    i=f.readline()#Считываем информацию про книги
    i=i.split("\n")#Разделяем информацию по строчкам
    a.append(i)#Добавляем все книги в список
for i in range(len(a)-1):# Проходим по списку книг, не считая последний элемент,т.к. он пустой
    q=a[i][0].split(";")#Разделяем информацию про книгу на отдельные элементы
    spisok.append(q)#Добавляем информацию про книгу в список
inf=''#Создаём строчку с информацией для вноса в текстовый документ
for i in range(20):#Выбираем 20 книг
    rand_int=random.randint(1,len(spisok))#Выбираем случайную книгу
    if fi=="books.csv":
        avt=spisok[rand_int][4]#Автор
        naz=spisok[rand_int][1]#Название
        year=spisok[rand_int][6][6:10]#Год
    else:
        avt=spisok[rand_int][2]
        naz=spisok[rand_int][1]
        year=spisok[rand_int][3]
    if avt=='':#Проверка на наличие автора в таблице
        avt="Автор не найден"
    inf=str(i+1)+")"+avt+". "+naz+" - "+year#Добавляем инфромацию про книгу
    file=open('test.txt','a')#Добавляем в конец файла информацию
    file.write(inf+"\n")#Записываем информацию
print("Файл создан, см. test.txt")

