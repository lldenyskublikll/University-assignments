# Лабораторна робота №7
# Варіант №14

# Використовувати файл Real estate.csv. 

# Завдання:
#   1) Використати будь-яку комбінацію незалежних ознак (не менше двох), щоб спрогнозувати ціну будинку. 
#   2) Виконати кластерний аналіз на даних, описати результати.


# Імпорт необхідних бібліотек
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score, explained_variance_score, mean_absolute_error, mean_squared_error, median_absolute_error
from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score

# Створення DataFrame з даними
df = pd.read_csv('RealEstate.csv')

# Виадлення рядку з датами транзакцій (не потрібен у прогнозі)
df = df.drop('transaction date', axis=1)

# Заміна NaN значень на середнє значення
df = df.fillna(df.mean())

# Розділення даних на навчальний та тестовий набори
X = df[['house age', 'distance to the nearest MRT station', 'number of convenience stores', 'latitude', 'longitude']]
y = df['house price of unit area']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Створення та навчання моделі лінійної регресії
model = LinearRegression()
model.fit(X_train, y_train)

# Прогнозування ціни будинку
y_pred = model.predict(X_test)

for i in range(len(X_test)):
    print(f"Для будинку з параметрами:\n{X_test.iloc[i]}\nПрогнозована ціна за одиницю площі: {y_pred[i]}\n")

# Оцінка моделі лінійної регресії:
print("\nОцінка моделі лінійної регресії")
#   Коефіцієнт детермінації (R²)
r_squared = r2_score(y_test, y_pred)
print(f"-- Коефіцієнт детермінації (R²): {r_squared}")

#   Оцінка поясненої дисперсії (EVS)
evs = explained_variance_score(y_test, y_pred)
print(f"-- Оцінка поясненої дисперсії (EVS): {evs}")

#   Оцінка середньої абсолютної похибки (MAE)
mae = mean_absolute_error(y_test, y_pred)
print(f"-- Середня абсолютна похибка (MAE): {mae}")

#   Оцінка середньоквадратичної помилки (RMSE)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"-- Корінь середньоквадратичної помилки (RMSE): {rmse}")

#   Оцінка медіани абсолютної похибки (Median AE)
median_ae =  median_absolute_error(y_test, y_pred)
print(f"-- Медіана абсолютної похибки: {median_ae}\n\n\n")


# Виконання кластерного аналізу
kmeans = KMeans(n_clusters=3, random_state=0)
kmeans.fit(X)

# Додавання міток кластерів до датафрейму
df['cluster'] = kmeans.labels_

# Візуалізація результатів кластеризації
plt.scatter(df['longitude'], df['latitude'], c=df['cluster'])
plt.xlabel('longitude')
plt.ylabel('latitude')
plt.show()

# Опис результатів
print(df.groupby('cluster').mean()) 

# Оцінка кластерної моделі:
print("\nОцінка кластерної моделі")
#   Оцінка коефіцієнта силуету
silhouette = silhouette_score(X, kmeans.labels_)
print(f"-- Коефіцієнт силуету: {silhouette}")

#   Оцінка індексу Девіса-Болдіна
davies_bouldin = davies_bouldin_score(X, kmeans.labels_)
print(f"-- Індекс Девіса-Болдіна: {davies_bouldin}")

#   Оцінка індексу Калінського-Харабаса
calinski_harabasz = calinski_harabasz_score(X, kmeans.labels_)
print(f"-- Індекс Калінського-Харабаса: {calinski_harabasz}\n\n")