# Лабораторна робота №3
# Варіант №14

# Використовувати файл bike.csv

# Перелік завдань:
#   Завдання №1:
#     Вивести інформацію про набір даних, основні статистичні характеристики, типи ознак. 
#     Які ознаки є категоріальними, а які – кількісними?
#   Завдання №2:
#     За допомогою зрізів зробити копію частини набору даних і зберегти до нового об’єкту DataFrame. 
#     Призначити йому власні індекси рядків та стовпців. Додати новий рядок.
#   Завдання №3:
#     Використовуючи початковий DataFrame:
#       а) Знайти мінімальний дохід для кожного рівня освіти;
#       б) Скільки людей віку 40+, що живуть не далі двох миль від роботи, мають машину? Вивести їх дані.
#       в) Додати новий стовпець, який містить дохід на кожного члена сім’ї.
#       г) Додати новий стовпець, який містить максимальний дохід для регіону.

import pandas as pd

# Завантаження даних
bike_data = pd.read_csv('bike.csv')

print("\n==================================================================================================================================================================================================================")
print("Bike Data:")
print(bike_data) 

# Завдання №1:
#   Вивести інформацію про набір даних, основні статистичні характеристики, типи ознак. 
#   Які ознаки є категоріальними, а які – кількісними?
print("\n==================================================================================================================================================================================================================")
print("Завдання №1")

# Інформація про набір даних
print("\nІнформація про набір даних DataFrame та їх типи:")
print("( bike_data.info() )")
print(bike_data.info())

print("\nОсновні статистичні характеристики DataFrame:")
print("( bike_data.describe() )")
print(bike_data.describe())


# Завдання №2:
#   За допомогою зрізів зробити копію частини набору даних і зберегти до нового об’єкту DataFrame. 
#   Призначити йому власні індекси рядків та стовпців. Додати новий рядок.
print("==================================================================================================================================================================================================================")
print("Завдання №2")

# Копія частини набору даних
bike_data_copy = bike_data.iloc[5:10].copy()
bike_data_copy.index = range(100, 105)  # Власні індекси рядків
bike_data_copy.columns = ['col_' + str(i) for i in range(len(bike_data.columns))]  # Власні індекси стовпців
bike_data_copy.loc[105] = bike_data.iloc[0]  # Додавання нового рядку
print("\nКопія DataFrame 'bike_data':")
print(bike_data_copy) 

# Завдання №3:
#   Використовуючи початковий DataFrame:
print("==================================================================================================================================================================================================================")
print("Завдання №3")

#   а) Знайти мінімальний дохід для кожного рівня освіти;
print("\nА:")

print("Мінімальний дохід для кожного рівня освіти:")
print("( bike_data.groupby('Education')['Income'].min() )")
print(bike_data.groupby('Education')['Income'].min())


#   б) Скільки людей віку 40+, що живуть не далі двох миль від роботи, мають машину? Вивести їх дані.
print("\nБ:")

# Виконання порівняння
people = bike_data[(bike_data['Age'] > 40) & ((bike_data['Commute Distance'] == "0-1 Miles") | (bike_data['Commute Distance'] == "0-2 Miles") | (bike_data['Commute Distance'] == "1-2 Miles")) & (bike_data['Cars'] > 0)]
print("Дані людей віку 40+, що живуть не далі двох миль від роботи, мають машину:")
print(people)

#   в) Додати новий стовпець, який містить дохід на кожного члена сім’ї.
print("\nВ:")

print("DataFrame 'bike_data' з доданим стовпцем, який містить дохід на кожного члена сім’ї:")
bike_data['Income per Family Member'] = bike_data['Income'] / (bike_data['Children'] + 2)  # +2, бо враховуємо батьків
print(bike_data) 

#   г) Додати новий стовпець, який містить максимальний дохід для регіону.
print("\nГ:")

print("DataFrame 'bike_data' з доданим стовпцем, який містить максимальний дохід для регіону:")
max_income_by_region = bike_data.groupby('Region')['Income'].transform('max')
bike_data['Max Income by Region'] = max_income_by_region
print(bike_data) 
print("==================================================================================================================================================================================================================")