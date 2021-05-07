import pandas as pd
import numpy as np

data=pd.Series(['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado'],
          index=[1,2,3,4,5,6])
print(data)

data1=pd.Series({'Computadora': 4000, 'Laptop': 35000, 'Setup': 45000})
print(data1)

data2=pd.Series(np.random.rand(10))
print(data2)
print("Los 5 primero son: ")
print(data2.head())
print("Los 5 ultimos son: ")
print(data2.tail())
print("Los 2 primero son: ")
print(data2.head(2))
print("Los 2 ultimos son: ")
print(data2.tail(2))