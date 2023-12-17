# Лабораторна робота №4
# Варіант №14

# Використовувати файл Stars.csv

# Перелік завдань:
#   Завдання №1:
#     Побудувати стовпчикові діаграми, на яких відобразити 
#       а) кількість зірок різного кольору; 
#       б) медіанну температуру зірок різного кольору; 
#       в) середній радіус зірок різного кольору з розподілом за типом зірки.
#   Завдання №2:
#     Побудувати гістограму температури, загальну і в залежності від спектрального класу.
#   Завдання №3:
#     Побудувати діаграму розмаху світності (загальну і в залежності від кольору), визначити чи присутні викиди.
#   Завдання №4:
#     За допомогою діаграм розсіювання зробити висновки щодо залежності між
#       а) температурою і абсолютною величиною; 
#       б) радіусом та температурою. 
#     Порахувати коефіцієнт кореляції за допомогою відповідних функцій.
   

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Завантаження даних
stars_data = pd.read_csv('Stars.csv')

# Завдання №1:
#   Побудувати стовпчикові діаграми, на яких відобразити 

#   а) кількість зірок різного кольору; 
plt.figure(figsize = (12, 6))
sns.countplot(data = stars_data, x = 'Color', color = 'green')
plt.title('Кількість зірок різного кольору')
plt.xlabel('Колір')
plt.ylabel('Кількість зірок')
plt.show()


#   б) медіанну температуру зірок різного кольору; 
median_temp = stars_data.groupby('Color')['Temperature'].median().sort_values()
median_temp.plot(kind = 'bar', color = 'green', width = 0.8)
plt.title('Медіанна температура зірок різного кольору')
plt.xlabel('Колір')
plt.ylabel('Температура')
plt.show()

#sns.barplot(data = median_temp, color = 'green')
#plt.title('Медіанна температура зірок різного кольору')
#plt.xlabel('Колір')
#plt.ylabel('Температура')
#plt.show()

#   в) середній радіус зірок різного кольору з розподілом за типом зірки.
average_radius = stars_data.groupby(['Color', 'Type'])['R'].mean().unstack()
average_radius.plot(kind = 'bar', stacked = True)
plt.title('Середній радіус зірок різного кольору з розподілом за типом зірки')
plt.xlabel('Колір')
plt.ylabel('R')
plt.show()



# Завдання №2:
#   Побудувати гістограму температури, загальну і в залежності від спектрального класу.

# Гітограма температури (загальна)
#plt.hist(stars_data['Temperature'], bins = 30, color = 'green', edgecolor = 'black')
sns.histplot(stars_data, x = 'Temperature', color = 'green', bins = 30)
plt.title('Гістограма температури')
plt.xlabel('Температура')
plt.ylabel('Кількість зірок')
plt.show()

# Гістограма температури в залежності від спектрального класу
g = sns.FacetGrid(stars_data, col = 'Spectral_Class', col_wrap = 4, height = 4)
g.map(plt.hist, 'Temperature')
g.set_titles('Спектральний клас: {col_name}')
g.set_axis_labels('Температура', 'Кількість зірок')

plt.figure(figsize=(10, 6))
sns.histplot(stars_data, x = 'Temperature', hue = 'Spectral_Class', bins = 30)
plt.title('Гістограма температури за спектральним класом')
plt.xlabel('Температура')
plt.ylabel('Кількість зірок')
plt.show() 



# Завдання №3:
#   Побудувати діаграму розмаху світності (загальну і в залежності від кольору), визначити чи присутні викиди.

# Діаграма розмаху світності
sns.boxplot(data=stars_data, x = 'L')
plt.title('Діаграма розмаху світності')
plt.show()

# Діаграма розмаху світності в залежності від кольору
sns.boxplot(data=stars_data, x='Color', y='L')
plt.title('Діаграма розмаху світності в залежності від кольору')
plt.show()



# Завдання №4:
#  За допомогою діаграм розсіювання зробити висновки щодо залежності між:

#  а) температурою і абсолютною величиною; 
plt.figure(figsize=(15, 6))

plt.subplot(1, 2, 1)
sns.scatterplot(data = stars_data, x = 'Temperature', y = 'A_M')
plt.title('Залежність між температурою і абсолютною величиною')
plt.xlabel('Температура')
plt.ylabel('Абсолютна величина')

#  б) радіусом та температурою. 
plt.subplot(1, 2, 2)
sns.scatterplot(data = stars_data, x = 'R', y = 'Temperature')
plt.title('Залежність між радіусом та температурою')
plt.xlabel('Радіус')
plt.ylabel('Температура')

plt.show()

# Розрахунок коефіцієнта кореляції
corr_temp_am = stars_data['Temperature'].corr(stars_data['A_M'])
corr_radius_temp = stars_data['R'].corr(stars_data['Temperature'])
print(f'\n\nКоефіцієнт кореляції між температурою і абсолютною величиною: {corr_temp_am}')
print(f'\nКоефіцієнт кореляції між радіусом та температурою: {corr_radius_temp}\n\n')

corr_temp_am_1 = stats.pearsonr(stars_data['Temperature'], stars_data['A_M'])
corr_radius_temp_1 = stats.pearsonr(stars_data['R'], stars_data['Temperature'])
print(f'\n\nКоефіцієнт кореляції між температурою і абсолютною величиною: {corr_temp_am_1}')
print(f'\nКоефіцієнт кореляції між радіусом та температурою: {corr_radius_temp_1}\n\n')