# Лабораторна робота №5
# Варіант №1

# Використовувати файл Delhi_Climate.csv

# Перелік завдань:
#   Завдання №1:
#     Побудувати графік зміни середніх денних температур: 
#       а) загальний; 
#       б) за 2014 рік; 
#       в) за квітень 2013 року; 
#       г) за листопад 2013 – травень 2015; 
#       д) за 2015 та 2016 на одному графіку (паралельно).
#   Завдання №2:
#     Знайти середні значення вологості: 
#       а) за 2016 рік; 
#       б) за кожний місяць; 
#       в) за кожні два тижні весни та літа 2014 року. 
#       г) Розрахувати і зобразити зміни вологості у відсотках за кожен день впродовж літа 2015 року. 
#       д) Знайти та зобразити графічно ковзне середнє вологості за 2013 рік з вікном в місяць.

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns

# Зчитування інформації з файлу
temp_data = pd.read_csv('Delhi_Climate.csv')
temp_data_1 = pd.read_csv('Delhi_Climate.csv', index_col=['date'], parse_dates=True)

# Конвертація колонки дат у тип datetime
temp_data['date'] = pd.to_datetime(temp_data['date'])


# Завдання №1:
#   Побудувати графік зміни середніх денних температур: 

#   а) загальний; 
temp_data_1.plot(y = 'meantemp', legend= False)
plt.title('Зміни середніх денних температур')
plt.xlabel('Рік')
plt.ylabel('Середня температура')
plt.show()

#plt.figure(figsize = (10, 6))
#plt.plot(temp_data['date'], temp_data['meantemp'])
#plt.title('Зміни середніх денних температур')
#plt.xlabel('Дата')
#plt.ylabel('Температура')
#plt.show()

#   б) за 2014 рік; 
temp_data_1.loc['2014'].plot(y = 'meantemp', legend= False)
plt.title('Зміни середніх денних температур у 2014')
plt.xlabel('Місяць')
plt.ylabel('Середня температура')
plt.show()

#data_2014 = temp_data[temp_data['date'].dt.year == 2014]
#plt.figure(figsize = (10, 6))
#plt.plot(data_2014['date'], data_2014['meantemp'])
#plt.title('Зміни середніх денних температур у 2014')
#plt.xlabel('Дата')
#plt.ylabel('Температура')
#plt.show()

#   в) за квітень 2013 року; 
temp_data_1.loc['2013-04'].plot(y = 'meantemp', legend= False)
plt.title('Зміни середніх денних температур у квітні 2013')
plt.xlabel('День')
plt.ylabel('Середня температура')
plt.show()

#data_april_2013 = temp_data[(temp_data['date'].dt.year == 2013) & (temp_data['date'].dt.month == 4)]
#plt.figure(figsize = (10, 6))
#plt.plot(data_april_2013['date'], data_april_2013['meantemp'])
#plt.title('Зміни середніх денних температур у квітні 2013')
#plt.xlabel('Дата')
#plt.ylabel('Температура')
#plt.show()

#   г) за листопад 2013 – травень 2015; 
temp_data_1.loc['2013-11':'2015-05'].plot(y = 'meantemp', legend= False)
plt.title('Зміни середніх денних температур (листопад 2013 – травень 2015)')
plt.xlabel('Рік, Місяць')
plt.ylabel('Середня температура')
plt.show()

#   д) за 2015 та 2016 на одному графіку (паралельно).
# ---------- ПЕРШИЙ ВАРІАНТ (2014-2015) ----------
data_2015 = temp_data[temp_data['date'].dt.year == 2015]
data_2014 = temp_data[temp_data['date'].dt.year == 2014]

plt.plot(data_2015['date'], data_2015['meantemp'], color = 'orange', label = 'Середні денні температури у 2015')
plt.plot(data_2015['date'], data_2014['meantemp'], color = 'green', label = 'Середні денні температури у 2014')

plt.title('Зміни середніх денних температур у 2015 та 2014')
plt.xlabel('Місяць')
plt.ylabel('Середня температура') 
plt.legend()
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b'))

# ---------- ДРУГИЙ ВАРІАНТ (2015-2016) ----------
data_2015_1 = temp_data[temp_data['date'].dt.year == 2015]
data_2016_1 = temp_data[temp_data['date'].dt.year == 2016]
plt.figure(figsize = (10, 6))

plt.subplot(2,1,1)
plt.plot(data_2015_1['date'], data_2015_1['meantemp'], color = 'orange', label = 'Середні денні температури у 2015')
plt.title('Зміни середніх денних температур у 2015 та 2016')
plt.xlabel('Місяць')
plt.ylabel('Середня температура') 
plt.legend()
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b'))

plt.subplot(2,1,2)
plt.plot(data_2016_1['date'], data_2016_1['meantemp'], color = 'green', label = 'Середні денні температури у 2016')
plt.xlabel('Місяць')
plt.ylabel('Середня температура')
plt.legend()
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b'))

plt.show()


# Завдання №2:
#   Знайти середні значення вологості: 

#   а) за 2016 рік; 
avg_humidity_2016 = temp_data_1['humidity'].loc['2016-01':'2016-12'].mean()
#avg_humidity_2016 = temp_data[temp_data['date'].dt.year == 2016]['humidity'].mean()
print(f"\n\nСереднє значення вологості за 2016: {avg_humidity_2016:.2f}%")

#   б) за кожний місяць; 
avg_humidity_monthly = temp_data_1['humidity'].resample('1M').mean()
print("\n\nСереднє значення вологості за кожний місяць:")
print(avg_humidity_monthly)

#   в) за кожні два тижні весни та літа 2014 року. 
avg_2014 = temp_data_1['humidity'].loc['2014-03':'2014-08'].resample('2W').mean()
print("\n\nСередні значення вологості за кожні два тижні весни та літа 2014 року:")
print(avg_2014)

#   г) Розрахувати і зобразити зміни вологості у відсотках за кожен день впродовж літа 2015 року. 
temp_data_1['percent_humidity_change'] = temp_data_1['humidity'].pct_change() * 100
humidity_2013_percents = temp_data_1['percent_humidity_change'].loc['2015-06':'2015-08']

print("\n\nЗміни вологості у відсотках за кожен день літа 2015:")
print(humidity_2013_percents)

humidity_2013_percents.plot(y = 'percent_humidity_change', legend=False)
plt.title('Зміни вологості у відсотках за кожен день впродовж літа 2015 року')
plt.xlabel('Місяць')
plt.ylabel('Вологість, %')
plt.show()

#   д) Знайти та зобразити графічно ковзне середнє вологості за 2013 рік з вікном в місяць.
temp_data_1['humidity_rolling_30'] = temp_data_1['humidity'].rolling(30).mean()
temp_data_1.loc['2013'].plot(y = 'humidity_rolling_30', legend=False)
plt.title('Ковзне середнє вологості за 2013 рік (вікно 30 днів)')
plt.xlabel('Місяць')
plt.ylabel('Середня вологість')

#temp_data_1['humidity_rolling_2'] = temp_data_1['humidity'].rolling(2).mean()
#temp_data_1.loc['2013'].plot(y = 'humidity_rolling_2', legend=False)
#plt.title('Ковзне середнє вологості за 2013 рік (вікно 2 дні)')
#plt.xlabel('Місяць')
#plt.ylabel('Середня вологість')

plt.show()