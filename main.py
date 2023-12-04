import pymongo

# Підключення до сервера MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Створення бази даних
db = client["database"]

# Створення колекції (еквівалент таблиці в реляційних базах даних)
collection = db["expenses"]

# Додавання документів (еквівалент записів в таблиці)
data1 = {"name": "Кафе та ресторани", "time": "2023-12-02 16:23:08", "amount": 620}
data2 = {"name": "Одяг та взуття", "time": "2023-12-03 18:43:23", "amount": 6810}
data3 = {"name": "Зоотовари", "time": "2023-12-02 12:44:48", "amount": 270}

# Вставка документів
inserted_data1 = collection.insert_one(data1)
inserted_data2 = collection.insert_one(data2)
inserted_data3 = collection.insert_one(data3)

# Оновлення документа
query = {"name": "Зоотовари"}
new_data = {"$set": {"amount": 310}}
collection.update_one(query, new_data)

# Видалення документа
delete_query = {"name": "Кафе та ресторани"}
collection.delete_one(delete_query)

#Пошук документа
search_query = {"name": "Одяг та взуття"}
print("Знайдено книгу:")
for document in collection.find(search_query):
    print(document)

# Зчитування документів після оновлення та видалення
print("Після оновлення та видалення:")
for document in collection.find():
    print(document)

# Закриття підключення
client.close()
