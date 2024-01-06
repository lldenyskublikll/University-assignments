import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import GridSearchCV

data = pd.read_csv('glass.csv')

# перетворення типів скла на бінарні класи: 0 для всіх типів, крім 7, і 1 для типу 7
data['Type'] = data['Type'].apply(lambda x: 1 if x == 7 else 0)

# розділяємо дані на ознаки та цільову змінну
X = data.drop('Type', axis=1)
y = data['Type']

# навчальний та тестові набори
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# навчання
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = LogisticRegression(class_weight='balanced', random_state=0, max_iter=5000)
model.fit(X_train, y_train)

# робимо пронгнози на тестовому наборі
y_pred = model.predict(X_test)

# обчисляємо матрицю помилок
conf_mat = confusion_matrix(y_test, y_pred)
print(f'Confusion Matrix:\n{conf_mat}')

# звіт про класифікацію
report = classification_report(y_test, y_pred)
print(f'Classification Report:\n{report}')


# визначаємо параметри для GridSearchCV
param_grid = {'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000], 'penalty': ['l1', 'l2']}

# створюємо модель GridSearchCV
grid_model = GridSearchCV(LogisticRegression(class_weight='balanced', random_state=0, solver='liblinear', max_iter=5000), param_grid)

# навчаємо модель
grid_model.fit(X_train, y_train)

# виводимо найкращі параметри
print(f'Best Parameters: {grid_model.best_params_}')

# робимо прогнози на тестовому наборі з використанням найкращої моделі
y_pred_grid = grid_model.predict(X_test)

# обчислюємо матрицю помилок
conf_mat_grid = confusion_matrix(y_test, y_pred_grid)
print(f'Confusion Matrix (GridSearchCV):\n{conf_mat_grid}')

# звіт про класифікацію
report_grid = classification_report(y_test, y_pred_grid)
print(f'Classification Report (GridSearchCV):\n{report_grid}')