# На практиці існує три основні задачі, пов’язані з процесом попередньої
# обробки даних:
# • Очищення даних
# • Трансформація даних
# • Збагачення даних

# Основні завдання очищення даних наступні:
# • Перейменування
# • Сортування та переупорядкування
# • Перетворення типів даних
# • Обробка повторюваних даних
# • Виправлення відсутніх або недійсних даних
# • Фільтрація до потрібної підмножини даниx

import pandas as pd
from AD_LR_6_functions import *

# Зчитування даних з файлу
df = pd.read_html('Version14.html')[0]
df.rename(columns={
    'Warehouse_block': 'Warehouse_Block',
    'Mode_of_Shipment': 'Shipment_Mode',
    'Customer_care_calls': 'Customer_Calls',
    'Customer_rating': 'Customer_Rating',
    'Cost_of_the_Product': 'Product_Cost',
    'Prior_purchases': 'Prior_Purchases',
    'Product_importance': 'Product_Importance',
    'Gender': 'Customer_Gender',
    'Discount_offered': 'Discount_Offered',
    'Weight_in_gms': 'Product_Weight',
    'Reached.on.Time_Y.N': 'On_Time_Delivery'
}, inplace=True)

df = pd.DataFrame(df)
print(df.describe)

# Видалення дублікатів
df = df.drop_duplicates(subset='ID', keep='first')

# Операції з виправлення відсутніх даних 
df = df.dropna(thresh=3)          # видалення срок, де значення NaN >= 3
df = df.fillna(value=df.mean())   # заповнення відсутніх даних у строках, що залишились, середніми значеннями даних стовпців
print(df.describe)

# Сортування за 'Customer_Rating'
df = df.sort_values(by='Customer_Rating', ascending=True)
print(df)


# Перевірка на коректність значень у файлі
df = df.loc[df['ID'].apply(is_convertible_to_int)]
df['Warehouse_Block'] = df['Warehouse_Block'].apply(check_warehouse)

df['Shipment_Mode'] = df['Shipment_Mode'].apply(check_shipment)
df = df.loc[df['Customer_Calls'].apply(is_convertible_to_int)]
df = df.loc[(df['Customer_Calls'] >= 0 ) | (df['Customer_Calls'] <= 5 ) ]

df = df.loc[df['Customer_Rating'].apply(is_convertible_to_int)]
df = df.loc[(df['Customer_Rating'] >= 0 ) | (df['Customer_Rating'] <= 5 )]

df = df.loc[(df['Product_Cost'].apply(is_convertible_to_float))]
df = df.loc[(df['Product_Cost'] > 0)]

df = df.loc[(df['Prior_Purchases'].apply(is_convertible_to_int))]

df = df.loc[df['Product_Importance'].apply(check_importance)]
df = df.loc[df['Customer_Gender'].apply(check_gender)]
df = df.loc[df['Discount_Offered'].apply(is_convertible_to_float) | (df['Discount_Offered'] > 0) | (df['Discount_Offered'] <= df['Product_Cost'])]
df = df.loc[(df['Discount_Offered'] > 0) | (df['Discount_Offered'] <= df['Product_Cost'])]

df = df.loc[df['Product_Weight'].apply(is_convertible_to_float)]
df = df.loc[df['On_Time_Delivery'].apply(is_convertible_to_float)]

print(df)

# Перетворення типів даних
df = df.astype({
    'ID': 'int',
    'Warehouse_Block': 'category',
    'Shipment_Mode': 'category',
    'Customer_Calls': 'int',
    'Customer_Rating': 'int',
    'Product_Cost': 'float',
    'Prior_Purchases': 'int',
    'Product_Importance': 'category',
    'Customer_Gender': 'category',
    'Discount_Offered': 'float',
    'Product_Weight': 'float',
    'On_Time_Delivery': 'int'
})