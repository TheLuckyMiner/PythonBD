import sqlite3

db = sqlite3.connect("database.db")
     
#Создание курсора
c = db.cursor()

# c.execute("""CREATE TABLE articles (
#     title text,
#     full_text text,
#     views integer,
#     avtor text
# )""")

#Удаление записей
#c.execute("DELETE FROM articles WHERE title = 'Google'")

#Добавление информации в БД
#c.execute('INSERT INTO articles VALUES ("Google", "Google is really cool", 50, "TLM")')

#c.execute('INSERT INTO articles VALUES ("Яндекс", "Яндекс. Найдется всё", 100, "ЯМ")')

#Выборка данных
c.execute("SELECT * FROM articles WHERE views <= 270 ORDER BY 1 DESC" )
items = c.fetchall()

#Выбор ВСЕХ записей
#print(c.fetchall())

#Выбор n записей
#print(c.fetchmany(1))

#print(c.fetchone()[1])



#Изменение данных
c.execute("UPDATE articles SET avtor = 'Admin' WHERE title= 'Яндекс'")

for item in items:
    print(item[0] + "\n" + item[3])
db.commit()

db.close()

#https://habr.com/ru/articles/754400/
