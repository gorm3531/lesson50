import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
print('~' * 20)
print('!Библиотека pandas!')
print('~' * 20)
print(' ')
d = {'apples': [3, 2, 0, 1], 'oranges': [8, 5, 9, 1]}
pan = pd.DataFrame(d)
print(pan)
print('-' * 20)

data = pd.read_csv('123.csv')
print(data.head())
print("-" * 20)

data = pd.DataFrame({'год': [2020, 2021, 2022], 'зарплата': [51083, 54687, 61794]})
data.plot(x="год", y="зарплата")
print(data)
plt.show()
print("~" * 20)

print('!Библиотека numpy!')

print('~' * 20)

print(' ')

a = np.array([1, 2, 3, 7, 9])
print(a)
print("-" * 20)
print(a.dtype)
print("-" * 20)
print(a + 3)
print("-" * 20)
print(a * 5)
print("-" * 20)
print(np.mean(a))
print("-" * 20)
print(np.min(a))
print("-" * 20)
print(np.max(a))
print('~' * 20)
print('!Библиотека numpy!')
print('~' * 20)
print(' ')
vals = [55, 16, 13, 12, 11]
labels = ['Lada Granta', 'Haval Jolion', 'Lada Niva travel', 'Lada vesta', 'Chery Tiggo 7 pro max']
plt.pie(vals, labels=labels, autopct='%1.1f%%')
plt.title('Топ 5 машин купленных в России 2023')
plt.show()



